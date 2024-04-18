from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

dag = DAG(
    'minio_write_dag',
    default_args=default_args,
    description='A DAG that writes to MinIO using KubernetesPodOperator',
    schedule_interval=None,
)

write_to_minio = KubernetesPodOperator(
    namespace='default',
    image='your_custom_image_with_minio_installed:latest',
    cmds=["python", "/scripts/minio_writer.py"],
    name="write-to-minio",
    task_id="write_to_minio_task",
    is_delete_operator_pod=True,
    in_cluster=True,
    env_vars={
        'MINIO_ENDPOINT': 'myminio-hl.minio-tenant1.svc.cluster.local:9000',
        'MINIO_ACCESS_KEY': '{{ var.value.MINIO_ACCESS_KEY }}',
        'MINIO_SECRET_KEY': '{{ var.value.MINIO_SECRET_KEY }}',
    },
    get_logs=True,
    dag=dag,
)

write_to_minio
