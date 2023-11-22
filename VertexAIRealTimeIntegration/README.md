## Overview
   This pattern demonstrate creation and deployment of Model on vertexAI and its real time integration with mongodb changestream.

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
- **API Bearer token creation for he endpoint:**
  * Run following commands to get the Token, copy the token to the .env file
  ```bash
  gcloud auth application-default login
  gcloud auth login
  gcloud config set project PROJECT_ID
  gcloud auth application-default set-quota-project PROJECT_ID
  gcloud auth print-access-token
  ```
  
- **DataModel Creation**
  * Follow the [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#3) in creating the data model.
  * Query we used to create the data model
  ``` bash
  CREATE OR REPLACE MODEL
  {dataset.modelname} OPTIONS(model_type='kmeans',kmeans_init_method = 'KMEANS++') AS (select * EXCEPT(CENTROID_ID) from dataset.tablename as u)
  ```
    ![Modelcreation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0ac3063d-0d0d-4162-87ce-9289415c32bd)
  
- **Export DataModel**
  * Refer [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#4) to export the bigquery data model 

    ![ExportImage](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1ae05be2-8308-4d51-bb3c-a2bcc7547d80)

- **Import the model to Vertex AI**
  * Refer [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#5) to import the model registry.

    ![import](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ec86ace4-2379-4461-83f5-7cf4505e6f18)
 
- **Deploy and test DataModel**
  * Refer [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#6) to create the endpoint.
    
    ![deploy](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dc8408d8-d70b-4a57-bb12-0665cabca97e)


## Real time integration of Mongodb with vertex AI
   Created the Model using "KMean" for details click [here](https://cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-kmeans) 

   Handled the mongodb chnagestream will trigger the endpoint that we created and deployed in vertexAI and it will update the prediction to the mongodb document.

   **Deploy and test predicates:**

   ![testpredicates](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/b8e3593e-64d3-45fe-a7c9-c7b9d05d5a93)

   **Insert to MongoDb:**

   ![mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/f00e91a7-c121-4249-80d2-66b97afba3b4)

   **Updated Document with Vertex AI endpoint response:**

   ![updatemongo](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/bad8432a-3646-4082-83fa-3bc1817f5083)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/VertexAIRealTimeIntegration/.env) file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
```