from pyspark.sql import SparkSession

def spark():
    try:
        # Se já existe (Databricks)
        spark
        return spark
    except NameError:
        # Se não existe (local / VS Code)
        return (
            SparkSession.builder
            .getOrCreate()
        )