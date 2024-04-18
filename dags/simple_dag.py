# Example: simple_dag.py

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import os

def create_file():
    path = '/path/to/persistent/volume/dummy.txt'  # Ensure this path points to a mounted Persistent Volume
    with open(path, 'w') as file:
        file.write('This is a dummy file created by Airflow.')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('simple_dag',
          default_args=default_args,
          description='A simple tutorial DAG',
          schedule_interval=timedelta(days=1),
          catchup=False)

start = DummyOperator(task_id='start', dag=dag)
create_file_task = PythonOperator(
    task_id='create_file',
    python_callable=create_file,
    dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> create_file_task >> end