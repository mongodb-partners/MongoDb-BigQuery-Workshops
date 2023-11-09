## Overview
   This pattern demonstrate consuming messages with defined schema from GCP PUB/SUB topic to GCP Bigquery table using native connector.
   
## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic by defining the schema (example schema is provided for the reference in the step **Create PUB/SUB Schema**) as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/01f6a218-c54c-4eb5-8b81-c103aa35fcb1)

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

    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8c34544a-1da9-4bad-8f18-49322e2ef1c9)

## Exporting to BigQuery:
  * Publish the messages to the Topic created using the change stream as described [here](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md)

  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

    **PublishMessage**
    ![PublishMessage](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/4a4b1195-586a-4344-961b-c635af1ea3bd)

    **BigQuery Table**
    ![BigQuery Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/48adfb10-81ac-44cc-9268-53befb998773)



