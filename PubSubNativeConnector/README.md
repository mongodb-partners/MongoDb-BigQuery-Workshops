## Overview
   This pattern demonstrate consuming messages with defined schema from GCP PUB/SUB topic to GCP Bigquery table using native connector.
   
## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic by defining the schema (example schema is provided for the reference in the step **Create PUB/SUB Schema**)
  * Detailed steps for topic creation can be found [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/01f6a218-c54c-4eb5-8b81-c103aa35fcb1)

- **Create PUB/SUB Schema**:
  * Create the schema to the topic as per the requirement
  * Create the schema with **"Schema Type : AVRO"**
  * Detailed steps for Schema definition can be found [here](https://cloud.google.com/pubsub/docs/create-schemas#create-schema)
  * Sample schema for the MongoDB sample collection **"sample_analytics.customers"**
``` bash
{
  "type": "record",
  "name": "Avro",
  "fields": [
    {
      "name": "_id",
      "type": "string"
    },
    {
      "name": "username",
      "type": "string"
    },
    {
      "name": "name",
      "type": "string"
    },
    {
      "name": "address",
      "type": "string"
    },
    {
      "name": "email",
      "type": "string"
    }
  ]
}
```
 
  **Screenshot 1:**
  
  ![Create PUB/SUB Schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0113324a-8825-432a-96d7-49b3e1191d1e)

- **Create DataSet**:
  * In the Big Query screen create the Dataset as per the requirement to the Selected Project.
  * Detailed steps for dataset can be found [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/4f4e8bb7-a525-42f5-b0bc-61269f94f2a1)

- **Table Creation**:
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation can be found [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/c83e8728-1462-42f6-bfe2-b915763003ac)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: write to BigQuery**
  * Once created under Message tab give **PULL** to get the messages that are process by the subscription
  * Detailed steps for Subscription creation can be found [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)

    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8c34544a-1da9-4bad-8f18-49322e2ef1c9)

## Exporting to BigQuery:
  * Publish the messages to the Topic created using the change stream as discussed [here](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md)

  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

    **PublishMessage**
    ![PublishMessage](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/53c34fcb-620b-4c34-b326-59872b135f69)

    **BigQuery Table**
    ![BigQuery Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d2e9e61f-ca71-4a94-af5c-23e788587460)



