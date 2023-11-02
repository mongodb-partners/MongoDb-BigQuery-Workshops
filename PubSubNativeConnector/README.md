## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation : [Create Topic in GCP](https://cloud.google.com/pubsub/docs/create-topic)

  ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/eb232b55-2724-4cd1-993b-cf41d55c588d)

- **Create PUB/SUB Schema**:
  * Create the schema to the topic as per the requirement
  * Create the schema with **"Schema Type : AVRO"**
  * Detailed steps for Schema definition : [Create GCP Schema](https://cloud.google.com/pubsub/docs/create-schemas)
  * Sample schema for the MongoDB sample collection **"sample_analytics.customers"**
``` bash
[
  {
    "name": "_id",
    "type": "STRING"
  },
  {
    "name": "username",
    "type": "STRING"
  },
  {
    "name": "name",
    "type": "STRING"
  },
  {
    "name": "address",
    "type": "STRING"
  },
  {
    "name": "birthdate",
    "type": "TIMESTAMP"
  },
  {
    "name": "email",
    "type": "STRING"
  },
  {
    "name": "accounts",
    "type": "ARRAY<INT64>"
  },
  {
    "name": "tier_and_details",
    "type": "RECORD",
    "fields": [
      {
        "type": "RECORD",
        "fields": [
          {
            "name": "tier",
            "type": "STRING"
          },
          {
            "name": "benefits",
            "type": "ARRAY<STRING>"
          },
          {
            "name": "active",
            "type": "BOOLEAN"
          },
          {
            "name": "id",
            "type": "STRING"
          }
        ]
      },
      {
        "type": "RECORD",
        "fields": [
          {
            "name": "tier",
            "type": "STRING"
          },
          {
            "name": "benefits",
            "type": "ARRAY<STRING>"
          },
          {
            "name": "active",
            "type": "BOOLEAN"
          },
          {
            "name": "id",
            "type": "STRING"
          }
        ]
      }
    ]
  }
]
```
  **Screenshot 1:**
  
  ![Create PUB/SUB Schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/23f4fa99-b64e-450a-9239-3d30c84f76f0)

  **Screenshot 2:**
  
  ![Create PUB/SUB Schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a2a635a9-3a1c-4b3d-b505-4d8accc44a57)

- **Create DataSet**:
  * In the Big Query screen create the Dataset as per the requirement to the Selected Project.
  * Detailed steps for dataset : [Create BQ Dataset](https://cloud.google.com/bigquery/docs/datasets)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cdbb4971-d4ab-4fac-9619-e1623b15e804)

- **Table Creation**:
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation : [Create BQ Table](https://cloud.google.com/bigquery/docs/tables)

    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f025d9fd-52c2-41d4-93b1-b5079de0d3c5)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **delivery Type : "Write to Bigquery"**, as per your requirements. 
  * Detailed steps for Subscription creation : [Create Subscription in GCP](https://cloud.google.com/pubsub/docs/create-subscription)

    ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/1902f905-cc2f-4764-a860-2b5d10224941)

## Exporting to BigQuery:
  * Publish the messages to the Topic created using the change stream as discussed [here](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md)

  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

    ![BigQuery Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/142e4dc9-5ca6-4b52-985b-4173a5fe488b)



