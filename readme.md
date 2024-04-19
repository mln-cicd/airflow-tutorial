# Some title


### **Kubernetes**
Forwarding du port 8080 vers 8282
```bash
kubectl port-forward svc/airflow-webserver 8282:8080 --namespace airflow
```
Override de la helm chart Airflow `values.yaml` depuis repo-root:
```bash
helm upgrade airflow apache-airflow/airflow --namespace airflow -f ./helm/values.yaml
```


### **Git commands**
```bash
git clone git@github.com-cicd:mln-cicd/airflow-tutorial.git


```


Installation MinIO
```bash

helm repo add minio https://charts.min.io/
helm repo update
helm install my-minio minio/minio --set accessKey=mln,secretKey=8888,resources.requests.memory=2Gi

```

s