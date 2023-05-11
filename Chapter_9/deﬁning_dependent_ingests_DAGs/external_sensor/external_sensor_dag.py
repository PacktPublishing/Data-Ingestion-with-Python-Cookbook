from airflow import DAG
from airflow.settings import AIRFLOW_HOME
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor

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

def get_holiday_dates(filename_json):
    with open (filename_json, 'r') as f:
        json_hol = json.load(f)
        holidays = json_hol["holidays"]
    
    print([item['date'] for item in holidays])


# Instantiate a DAG object
with DAG(
    dag_id='external_sensor_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
) as dag:

    wait_holiday_api_ingest = ExternalTaskSensor(
        task_id='wait_holiday_api_ingest',
        external_dag_id='holiday_ingest',
        external_task_id='holiday_api_ingestion',
        allowed_states=["success"],
        execution_delta = timedelta(minutes=1),
        timeout=300,
    )

    filename_json = f"{AIRFLOW_HOME}/files_to_test/output_files/holiday_brazil.json"
    date_tasks = PythonOperator(
        task_id='date_tasks',
        python_callable=get_holiday_dates,
        op_args=[filename_json]
    )

wait_holiday_api_ingest >> date_tasks