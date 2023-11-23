## Overview
  This pattern demostrate the dataflow from MongoDB to the GCP bigquery table using **Spark connector**. 
   
## Pre-requisite
- **Install pyspark :**
  * To use pyspark in the code need to install pyspark with the below command
     ```bash
     pip install pyspark
     ```
- **Create GCP Service Account:**
  * Detailed steps for the GCP Service Account Creation can be found [here](https://cloud.google.com/iam/docs/service-accounts-create#creating)
     
- **Table Creation:**
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)
  * Provide **Bigquery Job user** role to the Service account, as mentioned [here](https://cloud.google.com/bigquery/docs/jobs-overview)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/3b692fff-b51a-4b22-906c-a415e383d300)

- **Create GCP Bucket:**
  * Create GCP Bucket by enabling it to Multi-region and set public access prevention as described [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
## Spark Connector to sync data to GCP Bigquery Table from MongoDB collection :
   * This python application reads the data from MongoDB collection "sample_analytics.Customer" using spark connector
   * Write the loaded data to the destination GCP BigQuery table that we created.

     **Mongodb collection data**
     ![mongo](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a6b61db4-0481-4d72-817f-bb590ae4e239)

     **BigQuery Table after Syncing the data from Mongodb**
     ![biqTable](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a4b044e6-157b-4c2a-bc67-4a0eecda1246)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/SparkConnectorMongotoBq/.env) file.
3. Open the terminal in the respective project folder and run the command "python main.py".

  


