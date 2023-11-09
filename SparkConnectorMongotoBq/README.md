## Overview
  This pattern demostrate the dataflow from MongoDB to the GCP bigquery table using **Spark connector**. 
   
## Pre-requisite
- **Install pyspark :**
  * To use pyspark in the code need to install pyspark with the below command
     ```bash
     pip install pyspark
     ```
- **Table Creation:**
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)
  * Provide **Bigquery Job user** role to the Service account, as mentioned [here](https://cloud.google.com/bigquery/docs/jobs-overview)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/3b692fff-b51a-4b22-906c-a415e383d300)
- **Create GCP Service Account:**
  * Detailed steps for the GCP Service Account Creation can be found [here](https://cloud.google.com/iam/docs/service-accounts-create#creating)

- **Create GCP Bucket:**
  * Create GCP Bucket by enabling it to Multi-region and set public access prevention as described [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/5d75d3b1-b46a-4cdd-a245-32c0d46ba600)

## Spark Connector to sync MongoDB collection to the GCP Bigquery Table:
   * This python application is used to sync the MongoDB Atlas database collections to the GCP Bigquery table in the desire GCP bucket storage.
   * Loads the data from MongoDB collection "sample_analytics.Customer" with spark connector using the python code "mongotobqsync.py"
   * Write the loaded data to the destination GCP BigQuery table that we created.

     **Mongodb collection data**
     ![mongo](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a6b61db4-0481-4d72-817f-bb590ae4e239)

     **BigQuery Table after Syncing the data from Mongodb**
     ![biqTable](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a4b044e6-157b-4c2a-bc67-4a0eecda1246)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".

  


