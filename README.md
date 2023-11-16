# Individual Project 3: Databricks ETL Pipeline 
This project performs ETL on Azure Databrickks for a dataset on pollution emissions in Mexico City during 2019. The dataset is stored in a CSV that is later stored in Delta Lake as a Delta Table. 

### ETL
The **Ingest notebook** transforms this CSV with spark into a Delta Table to be stored in DeltaLake. 
The **TL_and_viz notebook** performs ETL operations with SparkSQL on this DeltaTable to translate column names to english and aggragate the data by day and zone. Later, data visualizations are generated to represent the data: 
<img width="1015" alt="Screenshot 2023-11-15 at 11 36 46 PM" src="https://github.com/dani-jimlar/djl_project_3/assets/143829673/28bdbd53-e741-4ead-98d1-ba1c85fad823">
<img width="1111" alt="Screenshot 2023-11-15 at 11 37 20 PM" src="https://github.com/dani-jimlar/djl_project_3/assets/143829673/f278200e-0514-4638-9540-62b8e7b76afc">


### Pipeline
A workflow was generated 
An automated trigger to initiate the pipeline.
README.md: m.

