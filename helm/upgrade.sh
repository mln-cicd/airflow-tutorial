#!/bin/bash

helm upgrade airflow airflow-stable/airflow --namespace airflow --version 8.8.0 --values kubernetes_executor_chart/custom-values.yaml
