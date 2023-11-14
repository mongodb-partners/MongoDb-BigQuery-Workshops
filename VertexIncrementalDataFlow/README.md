## Overview
   This pattern demonstrate integration of mongodb change stream with real time vertex model traning and deployment.

## Pre-requisite
- **Mongodb collection creation**:
  * Create sample collection **"Users"** in the already exsisting database referred in the common readme file. Follow the below JSON format to create mongodb documents.
  ```bash
  {
  "_id": 15,
  "average_order_value": 21,
  "no_of_orders": 10,
  "session_count": 13,
  "total_time_spend_by_user_in_msec": 2224700,
  "email": "test_1@gmail.com"
  }
  ```
- **Native Pub/Sub connector creation**
  * Refer the [document](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/PubSubNativeConnector/README.md) to create native Pub/Sub topic and subscription.
  * Create the schema to the Users collection that we created in mongodb with schema, Create the Pub/Sub topic with the created schema
  ```bash
  {
    "type": "record",
    "name": "Avro",
    "fields": [
      {
        "name": "userId",
        "type": "float"
      },
      {
        "name": "average_order_value",
        "type": "int"
      },
      {
        "name": "no_of_orders",
        "type": "int"
      },
      {
        "name": "session_count",
        "type": "int"
      },
      {
        "name": "total_time_spend_by_user_in_msec",
        "type": "int"
      }
    ]
  }
  ```
  * Create the Pub/Sub Subscription with the Delivery type as **"Write to BigQuery"**

    **Topic**

      ![Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8aac15ca-fd7c-432f-864f-cc6920184092)
      
    **Subscription**

      ![sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ebbe7c81-1cf0-4184-ae59-5102a37bc45b)


- **Create DataSet**:
  * Create the Dataset in Bigquery as described [here](https://cloud.google.com/bigquery/docs/datasets#create-dataset)

    ![Create DataSet](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6e45e4f8-925e-4799-9037-27e9dd405429)


- **Table Creation**:
  * Create a table for the schema defined in Bigquery as described [here](https://cloud.google.com/bigquery/docs/tables#create_an_empty_table_with_a_schema_definition)

    ![create Table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/da04bca0-2f06-4871-b2ed-d5e51cdd6123)

- **DataModel Creation**
  * Follow the [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#3) in creating the data model. Sample Query that we used to create the data model
  * Replace the Bigquery dataset name and the tablename in the below query.
  ``` bash
  CREATE OR REPLACE MODEL
  {dataset.modelname} OPTIONS(model_type='kmeans',kmeans_init_method = 'KMEANS++') AS (select * EXCEPT(CENTROID_ID) from dataset.tablename as u)
  ```
    ![Modelcreation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0ac3063d-0d0d-4162-87ce-9289415c32bd)

    ![Evaluation]()
  
- **Export DataModel**
  * Refer [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#4) to export the bigquery data model we created before.
    Once export is done we can see the exported data in the dowloaded folder as below.

    ![ExportImage](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1ae05be2-8308-4d51-bb3c-a2bcc7547d80)

- **Import the model to Vertex AI**
  * Refer [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#5) to import the model registry exported above.

    ![import](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ec86ace4-2379-4461-83f5-7cf4505e6f18)
 
- **Deploy and test DataModel**
  * Refer [link] (https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#6). Create the Endpoint to the deployed model.
    
    ![deploy](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/de2a9183-db08-455e-a9c2-8db0f955f11c)


## Real time integration of Mongodb with vertex AI
   Real time incremental changes to Bigquery table data, our model also has to be retrained on an increamental basis. BigML model provides an option 'warm_start' from which we can train our existing model with new data that are update from the MongoDb change stream.
   
   Have used "KMean" Model to train the data, for details click [here](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-kmeans) 

   Handle all the MongoDb change straem operations using Native PUB/SUB connectors with Subscription delivery type as "Write to BigQuery"

   Create the Scheduled Query in the Bigquery table, this will train and retain the real time data sync with MongoDb

   ![scheduleQuery](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f69ba58d-4359-43f5-afb6-94c59679f06c)

   ![runhistory](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f080aaa1-b095-4df2-9ecd-e8d5ad35fdf3)


   Deploy and test predicates

   ![testpredicates](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/025c0b85-8d6b-4c74-ba57-01f5886adfcb)



   

   

   

    
    


