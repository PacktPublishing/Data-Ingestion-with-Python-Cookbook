Follow the instructions on the recipe to insert it into the airflow properly

Add this lines to your docker-compose.yaml or airflow.cfg

    AIRFLOW__LOGGING__REMOTE_LOGGING: "True"
    AIRFLOW__LOGGING__REMOTE_BASE_LOG_FOLDER: "s3://airflow-cookbook"
    AIRFLOW__LOGGING__REMOTE_LOG_CONN_ID: conn_s3
    AIRFLOW__LOGGING__ENCRYPT_S3_LOGS: "False"
