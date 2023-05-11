from airflow import DAG
from airflow.settings import AIRFLOW_HOME
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 22),
    'retry_delay': timedelta(minutes=5)
}


# Instantiate a DAG object
with DAG(
    dag_id='parallel_tasks_dag',
    default_args=default_args,
    schedule_interval="@once",
) as dag:


    t_0 = BashOperator(
            task_id="t_0",
            bash_command="echo 'This tasks will be executed first'",
        )
    
    t_1 = BashOperator(
            task_id="t_1",
            bash_command="echo 'This tasks no1 will be executed in parallel with t_2 and t_3'",
        )
    
    t_2 = BashOperator(
            task_id="t_2",
            bash_command="echo 'This tasks no2 will be executed in parallel with t_1 and t_3'",
        )
    
    t_3 = BashOperator(
            task_id="t_3",
            bash_command="echo 'This tasks no3 will be executed in parallel with t_1 and t_2'",
        )
    
    t_final = BashOperator(
        task_id="t_final",
        bash_command="echo 'Finished all tasks in parallel'",
    )

t_0 >> [t_1, t_2, t_3] >> t_final