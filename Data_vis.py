# Databricks notebook source


# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(data)

# Bar chart using Matplotlib
plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y='avg_imecas', hue='Polluter', data=df)
plt.title('Average IMECAS values by Date and Polluter')
plt.show()

# Heatmap using Seaborn
pivot_df = df.pivot_table(values='avg_imecas', index='Zone', columns='Date', aggfunc='mean')
plt.figure(figsize=(12, 6))
sns.heatmap(pivot_df, cmap='viridis', annot=True, fmt=".2f", linewidths=.5)
plt.title('Heatmap of Average IMECAS values by Zone and Date')
plt.show()
