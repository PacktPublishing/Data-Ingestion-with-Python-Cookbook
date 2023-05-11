from airflow import DAG
from airflow.models import Variable
from airflow.settings import AIRFLOW_HOME
from airflow.operators.python_operator import PythonOperator

import os
from datetime import datetime, timedelta

from operators.holiday_api_plugin import HolidayAPIIngestOperator

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


# Instantiate a DAG object
with DAG(
    dag_id='holiday_ingest',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
) as dag:

    filename_json = f"holiday_brazil.json"
    task = HolidayAPIIngestOperator(
        task_id="holiday_api_ingestion",
        filename=filename_json,
        secret_key=Variable.get("SECRET_HOLIDAY_API"),
        country="BR",
        year=2022
    )


task