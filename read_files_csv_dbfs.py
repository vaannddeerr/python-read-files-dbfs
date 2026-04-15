# from pyspark.sql import functions as F
from spark_dataset import spark_session


spark = spark_session()


df = (spark.read
           .format('excel')
           .option('header',False)
           .option('delimiter',',')
           .option('inferSchema',True)
           .load('/Volumes/workspace/default/landing/*.xlsx'))

df.write.format('delta').mode('overwrite').saveAsTable('base_clie_full')