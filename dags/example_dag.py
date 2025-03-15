#!/usr/bin/env python
# coding: utf-8

from datetime import datetime, timedelta
import time
import pendulum
from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from app import tryyy


def bouble_sort():
    tryyy()


def sleep_30s():
    time.sleep(5)


@dag(dag_id='bouble_sort_test',
     description='bouble_sort',
     default_args={"retries": 1, "retry_delay": timedelta(seconds=30)},
     start_date=datetime(
         2025, 3, 13, 10, 30, tzinfo=pendulum.timezone("Asia/Taipei")),
     schedule='30 10 13 * *',
     catchup=False,
     max_active_runs=1,
     tags=["bouble"]
     )
def run_bouble_sort():
    bouble_task_1 = PythonOperator(
        task_id='bouble_sort_task_1', python_callable=bouble_sort)
    sleep_task = PythonOperator(
        task_id='wait_task', python_callable=sleep_30s)
    bouble_task_2 = PythonOperator(
        task_id='bouble_sort_task_1', python_callable=bouble_sort)

    bouble_task_1 >> sleep_task >> bouble_task_2


ahrefs_dag = run_bouble_sort()
