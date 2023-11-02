## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation : [Create Topic in GCP](https://cloud.google.com/pubsub/docs/create-topic)
  
    ![Create PUB/SUB Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f86a5edc-336a-40e0-a9cd-1d57ea9c2c60)

- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation : [Create GCP Table](https://cloud.google.com/bigquery/docs/tables)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/24d38411-a9ad-47e6-808c-237645f94fbd)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation : [Create GCP Bucket](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ac0b96df-e37e-4b61-bcb4-86206f294a11)
  
- **Create Dataflow Job Template:**
  * Create the dataflow job template to access big query tabel by selecting **"Dataflow Template : PubSub Subscription to BigQuery"**
  * Check the status once the job is created
  * Detailed steps to create Dataflow Job template: [Create Job template](https://cloud.google.com/dataflow/docs/guides/templates/running-templates)
  
    ![Create Dataflow Job Template](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/57aa94d1-f40a-40a3-8586-f0df25df965d)

  * Detailed steps to create the job template for pubsub to BQ : [PubSub-To-bq](https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery)

## Dataflow Template for Pub/Sub to BQ:
  * Use the Pub/Sub topic which we created with the **"Use a schema"**
  * Publish the message with the defined schema to the topic.
  * Use the **"Job Dataflow Template : PubSub Subscription to BigQuery"** 
  * This message will get reflected in the big query destination table with the defined schema.
  * Refer the screenshots for configuration process.
  
     **Publish message :** 
      
       ![Dataflow Template for PUB/Sub to BQ](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/4bcc49a0-525c-4280-b0c7-b4b61066242e)

     **Job Status :**

       ![Dataflow Job Graph](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/96880d32-6f05-408f-b736-8796f8c1dddf)
  
     **BigQuery Table :**
    
       ![BigQuery Destination Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/0365fdc3-3dc1-4830-82e5-9b88d91de613)
