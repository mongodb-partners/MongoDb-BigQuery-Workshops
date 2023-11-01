## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Follow the below link to create Topic in GCP
  * **Ref Link**:
    * https://cloud.google.com/pubsub/docs/create-topic

  ![Create a Pub/Sub Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7)

- **Create PUB/SUB Schema**:
  * Create the schema to the topic as per the requirement
  * Follow the link to create the schema with **"Schema Type : AVRO"**
  * **Ref Link**:
    * https://cloud.google.com/pubsub/docs/create-schemas

``` bash
        {
         "type" : "record",
         "name" : "Avro",
         "fields" : [
           {
             "name" : "StringField",
             "type" : "string"
           },
           {
             "name" : "FloatField",
             "type" : "float"
           },
           {
             "name" : "BooleanField",
             "type" : "boolean"
           }
         ]
        }
```

  ![Create PUB/SUB Schema](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/edde0645-f4c0-43a2-a57c-8b22041f3b3a)

- **Create DataSet**:
  * In the Big Query screen create the Dataset as per the requirement to the Selected Project.
  * Follow the steps to create dataset

  * **Ref Link**:
    * https://cloud.google.com/bigquery/docs/datasets

  ![Create DataSet](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/686850e2-ba3c-4ea3-aca8-8f7a1a83c459)

- **Table Creation**:
  * Create a table for the schema defined in Bigquery.
  * **Ref Link**:
    * https://cloud.google.com/bigquery/docs/tables

  ![Table Creation](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **delivery Type : "Write to Bigquery"**, as per your requirements. 
  * For more details follow the below link to create Subscription in GCP
  * **Ref Link**:
    * https://cloud.google.com/pubsub/docs/create-subscription

  ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/1902f905-cc2f-4764-a860-2b5d10224941)

## BigQuery Table:
  * In the Bigquery Tab you could see the reflection of the data that we published to the topic we created.

  ![BigQuery Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/142e4dc9-5ca6-4b52-985b-4173a5fe488b)



