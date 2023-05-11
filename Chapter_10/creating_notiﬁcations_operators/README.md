Follow the instructions on the recipe to insert it into the airflow properly

Add this lines to your docker-compose.yaml or airflow.cfg

    # SMTP settings
    AIRFLOW__SMTP__SMTP_HOST: "smtp.gmail.com"
    AIRFLOW__SMTP__SMTP_USER: "your_email_here"
    AIRFLOW__SMTP__SMTP_PASSWORD: "your_app_password_here"
    AIRFLOW__SMTP__SMTP_PORT: 587
