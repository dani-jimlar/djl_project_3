# Databricks notebook source
#read csv from repo

import pandas as pd
my_db=pd.read_csv("contaminantes_2019.csv")
spark_db=spark.createDataFrame(my_db)

# COMMAND ----------

file_path=f'/FileStore/tables/{"contaminantes_2019"}.csv'

# COMMAND ----------

spark_db.write.mode('overwrite').csv(file_path)

# COMMAND ----------

from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

# COMMAND ----------

from pyspark.sql.types import DoubleType, IntegerType, StringType, StructType, StructField, LongType

#define schema
schema = StructType([
  StructField("Fecha", StringType(), True),
  StructField("Hora", LongType(),  True),
  StructField("ZP", StringType(),  True),
  StructField("imecas", DoubleType(),  True),
  StructField("zona", StringType(),  True),
  StructField("contaminante", StringType(),  True),
  StructField("color", StringType(),  True)
])
csv_file_path="dbfs:/FileStore/tables/contaminantes_2019.csv"
pol_data_2019=spark.read.csv(csv_file_path, header=True, schema=schema)

# COMMAND ----------

pol_data_2019.show()

# COMMAND ----------

pol_data_2019.write.mode("overwrite").saveAsTable("raw_poll_table")
