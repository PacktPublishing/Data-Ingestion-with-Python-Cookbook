## Technical Requirements

Use this SparkSesion configuration to run the recipe scripts 

    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("chapter7_analytical_data") \
        .config("spark.executor.memory", '3g') \
        .config("spark.executor.cores", '2') \
        .config("spark.cores.max", '2') \
        .getOrCreate()
