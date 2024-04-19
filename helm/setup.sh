#!/bin/bash
export AIRFLOW_NAME="airflow"
export AIRFLOW_NAMESPACE="airflow"

kubectl create ns "$AIRFLOW_NAMESPACE"

kubectl apply -f secrets.yaml

helm install \
  "$AIRFLOW_NAME" \
  airflow-stable/airflow \
  --namespace "$AIRFLOW_NAMESPACE" \
  --version "8.8.0" \
  --values kubernetes_executor_chart/custom-values.yaml
