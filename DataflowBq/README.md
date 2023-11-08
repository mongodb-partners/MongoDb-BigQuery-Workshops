## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation can be found [here](https://cloud.google.com/pubsub/docs/create-topic)
  
    ![Create PUB/SUB Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/01ece0c5-62e7-4e7b-b927-b5db853f7f82)

- **Table Creation:** 
  * Create a table for the schema defined in Bigquery.

    **BigQuery Table schema update**
    ![table schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0999a4a8-9968-4293-8be5-4a4ad029f625)
    
  * Detailed steps for GCP table creation can be found [here](https://cloud.google.com/bigquery/docs/tables)

    **Dataset Creation**
    ![DataSetcreation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/42ed0a45-4021-4f9a-804c-ef1ed48357b6)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation can be found [here](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ac0b96df-e37e-4b61-bcb4-86206f294a11)
  
- **Create Dataflow Job Template:**
  * Create the dataflow job template to access big query tabel by selecting **"Dataflow Template : PubSub Subscription to BigQuery"**
  * Check the status once the job is created
  * Detailed steps to create Dataflow Job template can be found [here](https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery)
  
    ![Create Dataflow Job Template](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dc4e6083-3970-47c0-9dc1-6648e0fef043)

## Dataflow Template for Pub/Sub to BQ:
  * Use the Pub/Sub topic which we created with the **"Use a schema"**
  * Publish the message with the defined schema to the topic.
  * Use the **"Job Dataflow Template : PubSub Subscription to BigQuery"** 
  * This message will get reflected in the big query destination table with the defined schema.
  * Refer the screenshots for configuration process.
  
     **Publish message :** 
      
       ![Dataflow Template for PUB/Sub to BQ](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6a4287c8-dabf-41e7-bbc0-8620b16204fd)

     **Job Status :**

       ![Dataflow Job Graph](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/34870f31-aa80-4fab-ac2a-e2d22dd20fc2)
  
     **BigQuery Table :**
    
       ![BigQuery Destination Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d531d743-6681-4b86-a355-1129f0d546ed)
