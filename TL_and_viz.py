# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE cleaned_poll_data AS
# MAGIC SELECT
# MAGIC     TO_DATE(Fecha, 'yyyy-MM-dd') AS Date,
# MAGIC     Hora AS Hour,
# MAGIC     ZP,
# MAGIC     imecas AS IMECAS,
# MAGIC     zona AS Zone,
# MAGIC     contaminante AS Polluter,
# MAGIC     color AS Color
# MAGIC FROM raw_poll_table
# MAGIC WHERE Fecha IS NOT NULL; -- Example: Removing rows with NULL dates
# MAGIC
# MAGIC CREATE OR REPLACE TABLE group_poll_data AS
# MAGIC SELECT
# MAGIC     TO_DATE(Fecha, 'yyyy-MM-dd') AS Date,
# MAGIC     Hora AS Hour,
# MAGIC     ZP,
# MAGIC     imecas AS IMECAS,
# MAGIC     zona AS Zone,
# MAGIC     contaminante AS Polluter,
# MAGIC     color AS Color
# MAGIC FROM raw_poll_table
# MAGIC WHERE Fecha IS NOT NULL; 
# MAGIC
# MAGIC SELECT * FROM cleaned_poll_data;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC --average of pollutant by date and zone 
# MAGIC CREATE OR REPLACE TEMPORARY VIEW grouped_poll_data AS
# MAGIC SELECT
# MAGIC     Date,
# MAGIC     Zone,
# MAGIC     Polluter,
# MAGIC     AVG(imecas) AS avg_imecas
# MAGIC FROM cleaned_poll_data 
# MAGIC GROUP BY Date, Zone, Polluter;

# COMMAND ----------

query = "SELECT * FROM grouped_poll_data"
df_s = spark.sql(query)
df_s.show()

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
db_p=df_s.toPandas()
# Bar chart using Matplotlib
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='avg_imecas', hue='Polluter', data=db_p)
plt.title('Average IMECAS values by Date and Polluter')
plt.show()



# COMMAND ----------

# Heatmap using Seaborn
pivot_df = db_p.pivot_table(values='avg_imecas', index='Zone', columns='Date', aggfunc='mean')
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_df, cmap='viridis', annot=True, fmt=".2f", linewidths=.5)
plt.title('Heatmap of Average IMECAS values by Zone and Date')
plt.show()
