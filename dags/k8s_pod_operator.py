from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('kubernetes_pod_operator_dag',
          default_args=default_args,
          description='A DAG using KubernetesPodOperator',
          schedule_interval=timedelta(days=1),
          catchup=False)

kubernetes_pod_operator = KubernetesPodOperator(
    namespace='airflow',
    image='python:3.8-slim',
    cmds=['python', '-c'],
    arguments=['print("Hello from the KubernetesPodOperator")'],
    name='airflow-kpo-task',
    task_id='kpo_demo',
    dag=dag
)

kubernetes_pod_operator
