from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import get_current_context

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 4, 2),
    'end_date': datetime(2023, 4, 10),
    'schedule_interval': '@daily'
}


def my_task(execution_date=None, ti=None):
    print(f"execution_date:{execution_date}")
    print(f"task_instance:{ti}")

with DAG(
    'historical_data_dag',
    default_args=default_args,
    description='A simple ETL job using Python commands to retrieve historical data',
) as dag:

    p1 = PythonOperator(
                task_id="p1",
                python_callable=my_task,
                provide_context=True
        )

p1