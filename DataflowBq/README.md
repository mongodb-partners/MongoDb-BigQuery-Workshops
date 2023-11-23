## Overview
   This pattern demonstrate the data streams from GCP Pub/Sub to the GCP bigquery table by Dataflow Job using template **"PubSub Subscription to BigQuery"**
   
## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic by defining the schema as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)

    ![topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/13ad7e14-e965-4351-b077-e3fd75117939)


- **BigQuery Schema**
  
    ![schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/17bcc428-09b6-43fb-8573-ba4aecc358b1)


- **Create DataSet**:
  * Create the Dataset in the Bigquery as described [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f179ad2a-09ed-4ea2-b45d-61a6c1e9b812)

- **Table Creation:** 
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    **BigQuery Table**
    ![table schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6d3c3428-22c0-41c7-823f-e251f55482a5)

  
    
- **Create GCP Bucket:**
  * Create bucket by enabling it to Multi-region and set public access prevention on the bucket as described [here](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/19b5b538-8cb2-49b8-86ec-e86b390d0e80)
  
- **Create Dataflow Job Template:**
  * Create the dataflow streaming job using the template **"PubSub Subscription to BigQuery"** as described [here](https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery)
  * Check the status once the job is created
  
    ![Create Dataflow Job Template](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d2dc6f9c-08df-4127-866b-56983d552a08)

## Dataflow Template for Pub/Sub to BQ:
  * Use the Pub/Sub topic which we created to publish the message
  * This message will get reflected in the big query destination table with the defined schema.
  
     **Publish message :** 
      
       ![Dataflow Template for PUB/Sub to BQ](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/b1b7e294-1f32-4902-aa89-823ff94a0b0f)

     **Job Status :**

       ![Dataflow Job Graph](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/13063088-f8f5-41cf-b7ba-6a679c9de71f)
  
     **BigQuery Table :**
    
       ![BigQuery Destination Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dea69155-2ac6-4e45-9aa4-6fe77104edc5)
