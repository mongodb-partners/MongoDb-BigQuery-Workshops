## Overview
   This is to configure the connection between MongoDb collection and the GCP bigquery table using the Kafka from Confluent. Have create the two connectors in the confluent account one is **MongoDb Atlas Source connector** which is connected with the mongodb collection change stream and publish message to the kafka topic and another connector is **Google BigQuery Sink connector** which will read the message published to the kafka topic and write the same to the GCP BigQuery table.
   
## Pre-requisite
- **Confluent Account Creation**
  * Create a user confluent account creation
  * Detailed steps for creating the confluent account can be found [here](https://docs.confluent.io/cloud/current/get-started/index.html)

- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation can be found [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/badbf580-f3d8-45a6-9c3e-c5eebf41235c)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation can be found [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ac0b96df-e37e-4b61-bcb4-86206f294a11)
  
- **Create MongoDb Atlas Source connector:**
  * Click on the Add Connector button select **"MongoDb Atlas Source"**
    - In "Topic selection" e.g : "Customer_kafka_test"
    - In "Kafka credentials" Use the exsisting key or Generate the API keys
    - In "Authentication" Give the Database hastname, Database, Collection Name that message has to be tracked in the topics.(Use the collection **"sample_analytics.Customer"** that we created in the using common readme file.)
    - In "Configuration" 
        * Output Kafka record value format : **"AVRO"**
        * Advanced Configuration
            **"Publish full document only" : True**
    - In "sizing" just click continue 
    - In "Review and launch" Give the connector name **e.g "MongoDbAtlasSourceConnector_Customer_kafka_test"**
  
  * Detailed steps for creating the MongoDb atlas sources can be found [here](https://docs.confluent.io/cloud/current/connectors/cc-mongo-db-source.html#quick-start)
 
   ![MongoDb Atlas Source](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0f6f64ed-8b6c-485b-bb4b-7e6d369d15e2)

- **Create Service Api Key:**
  * Create the Service account in the GCP
  * Detailed steps for creating the service api keys can be found [here](https://developers.google.com/workspace/guides/create-credentials#api-key)

- **Create Google BigQuery Sink connector:**
  * Click on the Add Connector button select **"Google BigQuery Sink"**
    - In "Topic selection" select the topic that we want to sink with **"Customer-kafka-test.sample_analytics.Customer"**
    - In "Kafka credentials" Use the exsisting key or Generate the API keys
    - In "Authentication"
        * Upload the downloaded API key that we downloaded from the GCP profile
    - In "Configuration"
       * Input Kafka record value format : **"AVRO"**
       * Advanced configurations
           - Input Kafka record key format : **"String"**
           - Auto create tables : **True**
    - In "sizing" just click continue 
    - In "Review and launch" Give the connector name **e.g "BigQuerySinkConnector_Customer_kafka_sink"**

  * Detailed steps for creating the Google BigQuery Sink connector can be found [here](https://docs.confluent.io/cloud/current/connectors/cc-gcp-bigquery-sink.html#quick-start)
 
   ![Google BigQuery Sink](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cc2f1e06-cc50-4186-add7-dc9acbbd02fc)
## MongoDB to BigQuery with kafka confluent configuration:
  * Create the Cluster with Two connector in the confluent account
     - Follow the steps to create the **"MongoDb Atlas Source connector"**
     - Once connector is created insert the document to the "collection" that we have configured in the Source connector

     **Screenshot 1:**
       ![Mongo insert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/211f1f77-9e12-4156-8201-423c62fd86a3)

     **Screenshot 2:**
       ![Mongo insert1](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cca69772-832a-4d4c-8cc8-1dd3d9e55843)

     - Follow the steps to create the **"Google BigQuery Sink"**
     - Once Sink connector is created inserted data will get reflected in the Big query table

     **Screenshot 1:**
       ![Sink connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/e31574bc-1e0e-4178-9da5-5274edb92334)

     **Screenshot 2:**
       ![Bq table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8ff33c4b-50da-4f18-9524-2590c59a73fa)
     
