from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import logging

# Defining the log configuration
logger = logging.getLogger("airflow.task")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'remote_logging_s3_dag',
    default_args=default_args,
    description='A simple job to log a message in a remote location',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    logger.info("Let's extract data")
    pass

def final_task():
    logger.info("Finishing task...")
    logger.error("This is error message")
    pass

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

final_task = PythonOperator(
    task_id='final_task',
    python_callable=final_task,
    dag=dag,
)

extract_task >> final_task
