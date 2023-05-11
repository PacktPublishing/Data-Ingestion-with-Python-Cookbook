Follow the instructions on the recipe to insert it into the airflow properly

Add these lines to your docker-compose.yaml

    grafana:
    image: grafana/grafana:latest
    container_name: grafana
    environment:
        GF_SECURITY_ADMIN_USER: admin
        GF_SECURITY_ADMIN_PASSWORD: admin
        GF_PATHS_PROVISIONING: /grafana/provisioning
    links:
        - prometheus # use the same name of your Prometheus docker container
    ports:
        - 3000:3000
    volumes:
        - ./grafana/provisioning:/grafana/provisioning



