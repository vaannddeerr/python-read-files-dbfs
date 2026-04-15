# from pyspark.sql import functions as F
from spark_dataset import spark_session


spark = spark_session()


df = (spark.read
           .format('excel')
           .option('header','true')
           .option('delimiter',',')
           .option('inferSchema','true')
           .option('treatEmptyValuesAsNulls','true')
           .load('/Volumes/workspace/default/landing/*.xlsx'))

df.write.format('delta').mode('overwrite').saveAsTable('base_clie_full')