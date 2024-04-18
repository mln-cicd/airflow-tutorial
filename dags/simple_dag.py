# Example: simple_dag.py

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime

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

start = DummyOperator(
    task_id='start',
    dag=dag)

end = DummyOperator(
    task_id='end',
    dag=dag)

start >> end
