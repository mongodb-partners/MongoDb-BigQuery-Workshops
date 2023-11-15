## Overview
   This pattern demonstrate the dataflow from MongoDB to the GCP bigquery table using the ConfluentKafka connector. We will create **MongoDb Atlas Source connector** and **Google BigQuery Sink connector**.
   
   - **MongoDb Atlas Source connector** will watch the mongodb source collection and publish message to the kafka topic.
   - **Google BigQuery Sink connector** will read the message published to the kafka topic and write the same to the GCP BigQuery table.
   
## Pre-requisite
- **Confluent Account Creation**
  * Create a user confluent account creation as described [here](https://docs.confluent.io/cloud/current/get-started/index.html)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket as described [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1b0779cf-f321-47ef-9a60-b56a426771b1)
  
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
  
  * Create the MongoDb atlas sources as described [here](https://docs.confluent.io/cloud/current/connectors/cc-mongo-db-source.html#quick-start)
 
   ![MongoDb Atlas Source](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/fea7d885-049f-486e-92a9-ba5a055bc153)

- **Create Service Api Key:**
  * Create the Service account in the GCP as described [here](https://developers.google.com/workspace/guides/create-credentials#api-key)

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

  * Create the Google BigQuery Sink connector as discribed [here](https://docs.confluent.io/cloud/current/connectors/cc-gcp-bigquery-sink.html#quick-start)
 
   ![Google BigQuery Sink](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d754b2f7-c230-4379-aabd-07df54314478)
## MongoDB to BigQuery with kafka confluent configuration:
  * Create the Cluster with Two connector in the confluent account
     - Follow the steps to create the **"MongoDb Atlas Source connector"**
     - Once connector is created insert the document to the "collection" that we have configured in the Source connector

     **Screenshot 1:**
       ![Mongo insert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/9fa3e978-040e-4887-82d7-fb2d8fc06aae)

     **Screenshot 2:**
       ![Mongo insert1](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/57156d3f-29e8-4c47-b207-ecf696bf6cf4)

     - Follow the steps to create the **"Google BigQuery Sink"**
     - Once Sink connector is created inserted data will get reflected in the Big query table

     **Screenshot 1:**
       ![Sink connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/82ee9543-83b8-4425-9f9a-e686de716bc5)

     **Screenshot 2:**
       ![Bq table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8f91e33a-2f4e-478e-a2e5-c9480e900534)
     
