
from pyspark.sql import SparkSession

class spark():
    try:
        spark
        return spark
    
    except NameError:
        return (
            
            SparkSession.builder.getOrCreate()
                
               )


