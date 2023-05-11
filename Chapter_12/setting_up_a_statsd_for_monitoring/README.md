Follow the instructions on the recipe to insert it into the airflow properly

Add these lines to your docker-compose.yaml

    # StatsD configuration
    AIRFLOW__SCHEDULER__STATSD_ON: 'true'
    AIRFLOW__SCHEDULER__STATSD_HOST: statsd-exporter
    AIRFLOW__SCHEDULER__STATSD_PORT: 8125
    AIRFLOW__SCHEDULER__STATSD_PREFIX: airflow
    _PIP_ADDITIONAL_REQUIREMENTS: ${_PIP_ADDITIONAL_REQUIREMENTS:-apache-airflow[statsd]}


    statsd-exporter:
        image: prom/statsd-exporter
        container_name: statsd-exporter
        command: "--statsd.listen-udp=:8125 --web.listen-address=:9102"
        ports:
        - 9102:9102
        - 8125:8125/udp


