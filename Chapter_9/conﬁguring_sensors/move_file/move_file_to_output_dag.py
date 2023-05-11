from airflow import DAG
from airflow.settings import AIRFLOW_HOME
from airflow.operators.bash import BashOperator
from airflow.sensors.weekday import DayOfWeekSensor
from airflow.utils.weekday import WeekDay
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 3, 22),
    'retry_delay': timedelta(minutes=5)
}


# Instantiate a DAG object
with DAG(
    dag_id='sensors_move_file',
    default_args=default_args,
    schedule_interval="@once",
) as dag:

    move_file_on_saturdays = DayOfWeekSensor(
        task_id="move_file_on_saturdays", 
        timeout=3, 
        soft_fail=True, 
        week_day=WeekDay.SATURDAY
    ) 

    move_file_task = BashOperator(
            task_id="move_file_task",
            bash_command="mv $AIRFLOW_HOME/files_to_test/sensors_files/*.json $AIRFLOW_HOME/files_to_test/output_files/",
        )

move_file_on_saturdays.set_downstream(move_file_task)