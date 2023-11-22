## Overview
   This pattern demonstrate the dataflow from GCP bigquery table to mongodb collection via **"Dataflow Job"** using template **"PubSub Subscription to BigQuery"**
   
## Pre-requisite
- **Create DataSet**:
  * Create the Dataset in the Bigquery as described [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f179ad2a-09ed-4ea2-b45d-61a6c1e9b812)

- **Table Creation:** 
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    **BigQuery Table**
    ![table schema](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8795774d-2609-4e37-8105-207c06fa963b)

- **Dataflow Job:**
  * Create Dataflow job with the template **"Job Dataflow Template : BigQuery to MongoDb"**
  
  ![dataflow](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/25f44dd2-8b92-444f-903e-9ddbb2a6d554)

## Dataflow Template for BQ to Mongodb Collection:
  * Use the **"Job Dataflow Template : BigQuery to MongoDb"**

     **Job Status :**

       ![Dataflow Job Graph](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0a4a03c9-63d9-4f3d-a667-261515be8a26)
  
     **BigQuery Table :**
    
       ![BigQuery Destination Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d8ef1bdb-d91a-48ee-82af-5635a612c224)

    **Mongodb Collection :**

    ![mongocollection](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1d2f04d2-eb14-4ed2-a879-9fe87f234542)
