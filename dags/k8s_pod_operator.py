
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator


# KubernetesPodOperator example
kubernetes_pod_operator = KubernetesPodOperator(
    namespace='default',
    image='python:3.8-slim',
    cmds=['python', '-c'],
    arguments=['print("Hello from the KubernetesPodOperator")'],
    name='airflow-kpo-task',
    task_id='kpo_demo'
)

kubernetes_pod_operator.dry_run()

kubernetes_pod_operator