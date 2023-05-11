Follow the instructions on the recipe to insert it into the airflow properly

Add this line to your docker-compose.yaml or airflow.cfg
AIRFLOW__LOGGING__LOG_FORMAT: "[%(asctime)s] [ %(process)s - %(name)s ] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"