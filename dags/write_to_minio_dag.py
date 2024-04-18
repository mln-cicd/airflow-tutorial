import sys
print("Python path:")
print(sys.path)

print("Installed packages:")
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
print(installed_packages_list)

from minio import Minio

from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime, timedelta
from minio import Minio
import os



default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'minio_write_dag',
    default_args=default_args,
    description='A DAG that writes to MinIO using KubernetesPodOperator',
    schedule_interval=None,
)

def write_to_minio():
    # Retrieve credentials from environment variables
    minio_endpoint = os.getenv("MINIO_ENDPOINT")
    minio_access_key = os.getenv("MINIO_ACCESS_KEY")
    minio_secret_key = os.getenv("MINIO_SECRET_KEY")

    client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False
    )

    # Create bucket if it does not exist
    if not client.bucket_exists("bucket1"):
        client.make_bucket("bucket1")

    # Upload a file
    client.put_object(
        "my-bucket", "dummy.txt", data=b"Hello, world!", length=13,
    )

write_to_minio_task = KubernetesPodOperator(
    namespace='airflow',
    image='matthieujln/basic-python-executor:latest',
    cmds=["python", "-c"],
    arguments=["from minio import Minio; import os;" + write_to_minio.__code__.co_code],
    name="write-to-minio",
    task_id="write_to_minio_task",
    is_delete_operator_pod=True,
    in_cluster=True,
    env_vars={
        'MINIO_ENDPOINT': 'myminio-hl.minio-tenant1.svc.cluster.local:9000',
        'MINIO_ACCESS_KEY': '{{ var.value.minio_access_key }}',  # Make sure these are set in Airflow Variables
        'MINIO_SECRET_KEY': '{{ var.value.minio_secret_key }}',
    },
    get_logs=True,
    dag=dag,
)
