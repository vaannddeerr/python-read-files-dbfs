from pyspark.sql import functons as F
from spark_dataset import spark


df = (spark.read
           .format('csv')
           .option('header',True)
           .option('delimiter',',')
           .load('dbfs:/Volumes/workspace/default/landing/*.csv'))

df.writer.format('delta').saveAsTable('b_sttpt.base_clie_full')