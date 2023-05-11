Follow the instructions on the recipe to insert it into the airflow properly

Add these lines to your docker-compose.yaml

    prometheus:
    image: prom/prometheus
    ports:
    - 9090:9090
    links:
        - statsd-exporter # Use the same name as your statsd container
    volumes:
        - ./prometheus:/etc/prometheus
    command:
        - '--config.file=/etc/prometheus/prometheus.yml'
        - --log.level=debug
        - --web.listen-address=:9090
        - --web.page-title='Prometheus - Airflow Metrics'


