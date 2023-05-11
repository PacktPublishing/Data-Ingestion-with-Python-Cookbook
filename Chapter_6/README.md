## Techinical Requirements

Use this SparkSesion configuration to run the recipe scripts 

    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("chapter6_schemas") \
        .config("spark.executor.memory", '3g') \
        .config("spark.executor.cores", '1') \
        .config("spark.cores.max", '1') \
        .getOrCreate()
