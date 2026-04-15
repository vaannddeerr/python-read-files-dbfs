# from pyspark.sql import functions as F
from spark_dataset import spark_session


spark = spark_session()


df = (spark.read
           .format('csv')
           .option('header',True)
           .option('delimiter',',')
           .option('inferSchema',True)
           .load('/Volumes/workspace/default/landing/*.csv'))

df.write.format('delta').saveAsTable('b_sttpt.base_clie_full')