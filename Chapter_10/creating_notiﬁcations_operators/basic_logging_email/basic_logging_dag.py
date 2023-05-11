from airflow import DAG
from airflow.operators.email import EmailOperator

from datetime import datetime, timedelta
import logging

# Defining the log configuration
logger = logging.getLogger("airflow.task")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 1),
    'email': ['g.esppen@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'basic_logging_dag',
    default_args=default_args,
    description='A simple ETL job using Python and Airflow',
    schedule_interval=timedelta(days=1),
)

def extract_data():
    logger.info("Let's extract data")
    pass

def transform_data():
    logger.info("Then transform data")
    pass

def load_data():
    logger.info("Finally load data")
    logger.error("Oh, where is the data?")
    pass

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

success_task = EmailOperator(
    task_id="success_task",
    to= "g.esppen@gmail.com",
    subject="The pipeline finished successfully!",
    html_content="<h2> Hello World! </h2>",
    dag=dag
)

extract_task >> transform_task >> load_task >> success_task
