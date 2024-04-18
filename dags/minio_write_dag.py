from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from minio import Minio

def upload_file_to_minio():
    # Create a MinIO client
    client = Minio(
        "minio.minio-tenant1.svc.cluster.local:9000",
        access_key="your-access-key",
        secret_key="your-secret-key",
        secure=False  # Set to True if TLS is enabled
    )

    # File contents to write
    file_content = b"Hello, this is a test file from Airflow!"

    # Writing the file to MinIO
    client.put_object(
        "your-bucket-name",
        "dummy/dummy.txt",
        data=io.BytesIO(file_content),
        length=len(file_content)
    )

# Define the DAG
dag = DAG(
    'minio_file_upload',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2023, 1, 1),
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    },
    description='A simple DAG to upload files to MinIO',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Define the PythonOperator task
upload_task = PythonOperator(
    task_id='upload_to_minio',
    python_callable=upload_file_to_minio,
    dag=dag,
)