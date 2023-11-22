## Overview
   This pattern demonstrate consuming messages with defined schema from GCP PUB/SUB topic to GCP Bigquery table using native connector.
   
## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic by defining the schema (example schema is provided for the reference in the step **Create PUB/SUB Schema**) as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)
    
     ![topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/13ad7e14-e965-4351-b077-e3fd75117939)
  
- **Create PUB/SUB Schema**:
  * Create the schema to the topic as described [here](https://cloud.google.com/pubsub/docs/create-schemas#create-schema)
  * Create the schema with **"Schema Type : AVRO"**
  * Sample schema for the MongoDB sample collection **"sample_mflix.users"**
``` bash
      {
        "type": "record",
        "name": "Avro",
        "fields": [
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "email",
            "type": "string"
          },
          {
            "name": "password",
            "type": "string"
          }
        ]
      }
```
 
  **Screenshot 1:**
  
  ![Create PUB/SUB Schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1ea4b3bb-2574-4278-b582-aef329b60578)

- **Create DataSet**:
  * Create the Dataset in Bigquery as described [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6e45e4f8-925e-4799-9037-27e9dd405429)

- **Table Creation**:
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6086541c-ac07-401c-84a2-9e9d4e508914)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: write to BigQuery** as described [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)
 
    <img width="1239" alt="image" src="https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/3755c4cc-41b0-4192-8d40-f44c46cab441">

## Exporting to BigQuery:
  * Publish the messages to the Topic created using the change stream as described [here](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md)

  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

    **PublishMessage**
    <img width="1726" alt="image" src="https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dedcded3-bef1-4435-9f91-5fe03f54716a">

    **BigQuery Table**
    <img width="1726" alt="image" src="https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/873fff48-5b58-4cb6-b44b-9cc7f7a83eb4">



