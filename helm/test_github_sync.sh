#!/bin/bash

echo "Creating test pod..."
kubectl run test-git-sync --image=k8s.gcr.io/git-sync/git-sync:v3.3.0 --restart=Never --namespace=airflow --command -- /bin/sh -c "git clone https://github.com/mln-cicd/airflow-tutorial.git"

echo "Waiting for the test pod to be ready..."
kubectl wait --for=condition=Ready pod/test-git-sync --namespace=airflow --timeout=60s

echo "Retrieving logs from the test pod..."
kubectl logs test-git-sync -n airflow

echo "Deleting the test pod..."
kubectl delete pod test-git-sync -n airflow