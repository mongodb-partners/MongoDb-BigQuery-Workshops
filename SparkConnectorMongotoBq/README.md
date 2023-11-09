## Overview
  This pattern demostrate the dataflow from MongoDB to the GCP bigquery table using **Spark connector**. 
   
## Pre-requisite
- **Install pyspark :**
  * To use pyspark in the code need to install pyspark with the below command
     ```bash
     pip install pyspark
     ```
- **Table Creation:**
  * Create the GCP pub/Sub topic without defining the schema
  * Detailed steps for topic creation can be found [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)
  * Provide **Bigquery Job user** role to the Service account, as mentioned [here](https://cloud.google.com/bigquery/docs/jobs-overview)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/4c24ebec-bd06-4d3b-908f-fcd40069840b)
- **Create GCP Service Account:**
  * Detailed steps for the GCP Service Account Creation can be found [here](https://cloud.google.com/iam/docs/service-accounts-create#creating)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation can be found [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/4078cd12-3f48-4308-b507-dff2cabcfea1)

## Spark Connector to sync MongoDB collection to the GCP Bigquery Table:
   * This python application is used to sync the MongoDB Atlas database collections to the GCP Bigquery table in the desire GCP bucket storage.
   * Loads the data from MongoDB collection "sample_analytics.Customer" with spark connector using the python code "mongotobqsync.py"
   * Write the loaded data to the destination GCP BigQuery table that we created.

     **Insert the document to mongodb collection**
     ![mongo_insert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/e38df119-5c0c-4824-8fea-96ec03aa0771)

     **BigQuery Table after Syncing the data from Mongodb**
     ![biqTable](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0cc0ca36-9f84-4c20-a4ea-09c30e891a42)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".

  


