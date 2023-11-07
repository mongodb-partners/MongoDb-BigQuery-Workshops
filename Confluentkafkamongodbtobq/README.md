## Pre-requisite
- **Confluent Account Creation**
  * Create a user confluent account creation
  * Detailed steps for creating the confluent account can be found [here](https://docs.confluent.io/cloud/current/get-started/index.html)

- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation can be found [here](https://cloud.google.com/bigquery/docs/tables)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/24d38411-a9ad-47e6-808c-237645f94fbd)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation can be found [here](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ac0b96df-e37e-4b61-bcb4-86206f294a11)
  
- **Create MongoDb Atlas Source connector:**
  * Click on the Add Connector button select **"MongoDb Atlas Source"**
    - In "Topic selection" e.g : "Customer_kafka_test"
    - In "Kafka credentials" Use the exsisting key or Generate the API keys
    - In "Authentication" Give the Database hastname, Database, Collection Name that message has to be tracked in the topics.
    - In "Configuration" 
        * Output Kafka record value format : **"AVRO"**
        * Advanced Configuration
            **"Publish full document only" : True**
    - In "sizing" just click continue 
    - In "Review and launch" Give the connector name **e.g "MongoDbAtlasSourceConnector_Customer_kafka_test"**
  
  * Detailed steps for creating the MongoDb atlas sources can be found [here](https://docs.confluent.io/cloud/current/connectors/cc-mongo-db-source.hl#)
 
   ![MongoDb Atlas Source](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0f6f64ed-8b6c-485b-bb4b-7e6d369d15e2)

- **Create Service Api Key:**
  * Create the Service account in the GCP
  * Detailed steps for creating the service api keys can be found [here](https://developers.google.com/workspace/guides/create-credentials)

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

  * Detailed steps for creating the Google BigQuery Sink connector can be found [here](https://docs.confluent.io/cloud/current/connectors/cc-gcp-bigquery-sink.html)
 
   ![Google BigQuery Sink](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cc2f1e06-cc50-4186-add7-dc9acbbd02fc)
## MongoDB to BigQuery with kafka confluent configuration**:
  * Create the Cluster with Two connector in the confluent account
     - Follow the steps to create the **"MongoDb Atlas Source connector"**
     - Once connector is created insert the document to the "collection" that we have configured in the Source connector

     **Screenshot 1:**
       ![Mongo insert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cc9708b1-b5e9-4ce6-b036-f0fd0c147f93)

     **Screenshot 2:**
       ![Mongo insert1](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/2f1d4174-a386-488c-939c-761f63ee6755)

     - Follow the steps to create the **"Google BigQuery Sink"**
     - Once Sink connector is created inserted data will get reflected in the Big query table

     **Screenshot 1:**
       ![Sink connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ab96dc11-78e3-4942-a1ce-96e2fdd7ed58)

     **Screenshot 2:**
       ![Bq table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/58682ba4-9364-470a-96ca-5e0e1278ce97)
     
