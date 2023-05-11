from airflow import DAG
from airflow.settings import AIRFLOW_HOME
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

import json
from datetime import datetime, timedelta

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def get_ids_from_json(filename_json):
    with open (filename_json, 'r') as f:
        git = json.loads(f.read())
    
    print([item['id'] for item in git])


# Instantiate a DAG object
with DAG(
    dag_id='simple_ids_ingest',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
) as dag:

    first_task = BashOperator(
            task_id="first_task",
            bash_command="echo $AIRFLOW_HOME",
        )

    filename_json = f"{AIRFLOW_HOME}/files_to_test/github_events.json"
    get_id_from_json = PythonOperator(
        task_id="get_id_from_json",
        python_callable=get_ids_from_json,
        op_args=[filename_json]
    ) 


first_task >> get_id_from_json