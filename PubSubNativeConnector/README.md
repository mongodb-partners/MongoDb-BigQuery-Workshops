## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation : [Create Topic in GCP](https://cloud.google.com/pubsub/docs/create-topic)

  ![Create a Pub/Sub Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7)

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
  ![Create PUB/SUB Schema](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/edde0645-f4c0-43a2-a57c-8b22041f3b3a)

- **Create DataSet**:
  * In the Big Query screen create the Dataset as per the requirement to the Selected Project.
  * Detailed steps for dataset : [Create BQ Dataset](https://cloud.google.com/bigquery/docs/datasets)

  ![Create DataSet](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/686850e2-ba3c-4ea3-aca8-8f7a1a83c459)

- **Table Creation**:
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation : [Create BQ Table](https://cloud.google.com/bigquery/docs/tables)

  ![Table Creation](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **delivery Type : "Write to Bigquery"**, as per your requirements. 
  * Detailed steps for Subscription creation : [Create Subscription in GCP](https://cloud.google.com/pubsub/docs/create-subscription)

  ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/1902f905-cc2f-4764-a860-2b5d10224941)

## Exporting to BigQuery:
  * Publish the messages to the Topic created using the change stream as discussed [here](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md)

  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

  ![BigQuery Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/142e4dc9-5ca6-4b52-985b-4173a5fe488b)



