## Overview
   This Pattern demonstrate the dataflow from GCP Pub/Sub to the GCP bigquery table via **"Dataflow Job"** using template **"PubSub Subscription to BigQuery"**
   
## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic can be created either by defining the schema as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)
  
    ![Create PUB/SUB Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/01ece0c5-62e7-4e7b-b927-b5db853f7f82)

- **Create DataSet**:
  * Create the Dataset in the Bigquery as described [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f179ad2a-09ed-4ea2-b45d-61a6c1e9b812)

- **Table Creation:** 
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    **BigQuery Table**
    ![table schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6d3c3428-22c0-41c7-823f-e251f55482a5)

    **BigQuery Schema**
    ![schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/17bcc428-09b6-43fb-8573-ba4aecc358b1)

    
- **Create GCP Bucket:**
  * Create bucket by enabling it to Multi-region and set public access prevention on the bucket as described [here](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/43cc1104-a868-4237-8c29-ed72e4201768)
  
- **Create Dataflow Job Template:**
  * Create the dataflow job template to access big query tabel by selecting **"Dataflow Template : PubSub Subscription to BigQuery"** as described [here](https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery)
  * Check the status once the job is created
  
    ![Create Dataflow Job Template](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/e28050ed-8126-4ab6-bbeb-b9ce36f1fcb5)

## Dataflow Template for Pub/Sub to BQ:
  * Use the Pub/Sub topic which we created with the **"Use a schema"**
  * Publish the message with the defined schema to the topic.
  * Use the **"Job Dataflow Template : PubSub Subscription to BigQuery"** 
  * This message will get reflected in the big query destination table with the defined schema.
  * Refer the screenshots for configuration process.
  
     **Publish message :** 
      
       ![Dataflow Template for PUB/Sub to BQ](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/879ca729-4133-414a-a671-1dec637d7472)

     **Job Status :**

       ![Dataflow Job Graph](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/34870f31-aa80-4fab-ac2a-e2d22dd20fc2)
  
     **BigQuery Table :**
    
       ![BigQuery Destination Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dea69155-2ac6-4e45-9aa4-6fe77104edc5)
