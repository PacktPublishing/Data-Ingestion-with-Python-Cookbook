from airflow import DAG
from airflow.settings import AIRFLOW_HOME
from airflow.providers.mongo.hooks.mongo import MongoHook
from airflow.operators.python import PythonOperator

import os
import json
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def get_mongo_collection():
    hook = MongoHook(conn_id ='mongodb')
    client = hook.get_conn()
    print(client)
    print(hook.get_collection(mongo_collection="reviews", mongo_db="db_airbnb"))


# Instantiate a DAG object
with DAG(
    dag_id='mongodb_check_conn',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
) as dag:

    mongo_task = PythonOperator(
        task_id='mongo_task',
        python_callable=get_mongo_collection
    )

mongo_task