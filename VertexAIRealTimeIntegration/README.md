## Overview
   This pattern demonstrate creation and deployment of Model on vertexAI and its real time integration with mongodb changestream. For the scope of this workshop we use **"K-means"** clustering for data segmentation.This model identifies users segments.
   
   **User Clustering**
     
   - Loyalty programs often categorize users into discrete segments based on the user’s purchase behavior and site engagement, such as Platinum / Gold / Silver / Bronze tiers.
      
   - In this example, we showcase how a ML driven clustering model can be applied to achieve user clustering using **Big query SQL workspace**.
   
   **K-means clustering**
      
   - K-means is an unsupervised learning technique identifying customer segments, so model training does not require labels nor split data for training or evaluation.
      
   **Cluster Users based on following attributes**
   
   - Session count
   - Total time spent
   - Average order value
   - No of orders

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
- **Bigquery Data sink**
  * Follow the [pattern](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/DataflowBq/README.md) to sink the data from mongodb to bigquery.

   ![bigquery table](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0a888e1d-f164-4c46-8dee-4367abe29a41)
    
- **API Bearer token creation for the endpoint:**
  * Create the bearer token as  described [here](https://developers.google.com/spectrum-access-system/guides/authorization-and-authentication) for accessing the endpoint and copy the token to the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/VertexAIRealTimeIntegration/.env) file
  
- **Datamodel creation**
  * Follow the [link](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#3) to create the K-means model.
  * sample query to create a model
  ``` bash
  CREATE OR REPLACE MODEL
  {dataset.user_cluster} OPTIONS(model_type='kmeans',kmeans_init_method = 'KMEANS++') AS (select * EXCEPT(CENTROID_ID) from dataset.users as u)
  ```
    ![Modelcreation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0ac3063d-0d0d-4162-87ce-9289415c32bd)
  
- **Deploy model to endpoint**
  * Follow the steps described [here](https://codelabs.developers.google.com/codelabs/bqml-vertex-prediction#0) to deploy model to an endpoint.
    
    ![deploy](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/dc8408d8-d70b-4a57-bb12-0665cabca97e)


## Real time integration of Mongodb with vertex AI
   Whenever the real time changes made to the MongoDB collection changestream will be trigger the endpoint and get the online prediction and update the nearest centroid id to the MongoDb collection.
  
   **Insert/Update to MongoDb:**
   
   Python program watch the collection for changes, whenever changes detected, it will trigger the vertex AI endpoint to get online prediction.
   
   ![mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/03d71e6a-63a4-498f-b719-5b7a638950c9)

   **Updated Document with Vertex AI endpoint response:**

   Once we get prediction response, python program will update the same to the MongoDB collection.
   
   ![updatemongo](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8c26db96-6e36-428b-840e-d0d4cb157270)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/VertexAIRealTimeIntegration/.env) file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
```
