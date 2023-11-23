## Overview
   This pattern demonstrate the dataflow from MongoDB to the GCP bigquery table using the ConfluentKafka connector. We will create **MongoDb Atlas Source connector** and **Google BigQuery Sink connector**.
   
   - **MongoDb Atlas Source connector** will watch the mongodb source collection and publish message to the kafka topic.
   - **Google BigQuery Sink connector** will read the message published to the kafka topic and write the same to the GCP BigQuery table.
   
## Pre-requisite
- **Confluent Account Creation**
  * Create a user confluent account creation as described [here](https://docs.confluent.io/cloud/current/get-started/index.html)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket as described [here](https://cloud.google.com/storage/docs/creating-buckets#create_a_new_bucket)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/32d6d700-e493-4f74-819d-8c9d544ea67f)
  
- **Create MongoDb Atlas Source connector:**
  * Click on the Add Connector button select **"MongoDb Atlas Source"**
    - In "Topic selection" e.g : "user_kafka_test"
    - In "Kafka credentials" Use the exsisting key or Generate the API keys
    - In "Authentication" Give the Database hastname, Database, Collection Name that message has to be tracked in the topics.(Use the collection **"sample_mflix.users"** that we created in the using common readme file.)
    - In "Configuration" 
        * Output Kafka record value format : **"AVRO"**
        * Advanced Configuration
            **"Publish full document only" : True**
    - In "sizing" just click continue 
    - In "Review and launch" Give the connector name **e.g "MongoDbAtlasSourceConnector_user_kafka_connector"**
  
  * Create the MongoDb atlas sources as described [here](https://docs.confluent.io/cloud/current/connectors/cc-mongo-db-source.html#quick-start)
 
   ![MongoDb Atlas Source](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ba76bb74-f2c3-4e4c-9a8a-1d09456c6348)

- **Create Service Api Key:**
  * Create the Service account in the GCP as described [here](https://developers.google.com/workspace/guides/create-credentials#api-key)

- **Create Google BigQuery Sink connector:**
  * Click on the Add Connector button select **"Google BigQuery Sink"**
    - In "Topic selection" select the topic that we want to sink with **"user-kafka-test.sample_mflix.users"**
    - In "Kafka credentials" Use the exsisting key or Generate the API keys
    - In "Authentication"
        * Upload the downloaded API key that we downloaded from the GCP profile
    - In "Configuration"
       * Input Kafka record value format : **"AVRO"**
       * Advanced configurations
           - Input Kafka record key format : **"String"**
           - Auto create tables : **True**
    - In "sizing" just click continue 
    - In "Review and launch" Give the connector name **e.g "BigQuerySinkConnector_user_kafka_sink"**

  * Create the Google BigQuery Sink connector as discribed [here](https://docs.confluent.io/cloud/current/connectors/cc-gcp-bigquery-sink.html#quick-start)
 
   ![Google BigQuery Sink](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/c0088772-3e4a-49e4-879b-45d95e17bbc3)
## MongoDB to BigQuery dataflow with confluent kafka:
  - Once connector is created, insert the document to the "collection" that we have configured in the Source connector

    ![Mongo insert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/9fa3e978-040e-4887-82d7-fb2d8fc06aae)

  - Source connector that takes data from the mongodb source and feeds them into a topic

   ![Mongo insert1](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1ba5007c-0c2d-4754-91b2-03db02dee8d9)

  - Sink connector takes data from Topic and delivers them to Bigquery
     
   ![Sink connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ed98f4c6-d5d7-4c76-b6c2-271111deeefd)

   ![Bq table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/edf44109-f6b2-4f93-9cb7-25f3656698dc)
     
