[![CI](https://github.com/dani-jimlar/djl_project_3/actions/workflows/cicd.yml/badge.svg)](https://github.com/dani-jimlar/djl_project_3/actions/workflows/cicd.yml)
# Individual Project 3: Databricks ETL Pipeline 
This project performs ETL on Azure Databrickks for a dataset on pollution emissions in Mexico City during 2019. The dataset is stored in Delta Lake as a Delta Table. 

### ETL
The **Ingest notebook** transforms, using spark, the CSV containing the information into a Delta Table to be stored in DeltaLake. 
The **TL_and_viz notebook** performs ETL operations with SparkSQL on this DeltaTable to translate column names to english and aggragate the data by day and zone. Later, data visualizations are generated to represent the data: 
<img width="922" alt="g_1" src="https://github.com/dani-jimlar/djl_project_3/assets/143829673/1c1179fa-a89c-42e1-a793-710d44cac4f2">
<img width="1005" alt="g_2" src="https://github.com/dani-jimlar/djl_project_3/assets/143829673/8854612d-cd08-4e36-b9bc-6f9c8cf61fa2">

### Pipeline
A workflow was generated to schedule the runs of this pipeline for every Thursday.
<img width="1503" alt="Screenshot 2023-11-16 at 12 12 16 AM" src="https://github.com/dani-jimlar/djl_project_3/assets/143829673/525170ce-fa47-4d1d-a5dc-e38dd508616d">


