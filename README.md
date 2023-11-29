## Overview
   As part of the Atlas GCP BigQuery workshop initiative, we have explored and demonstrated a number of integration patterns between Atlas and GCP data products. Specifically Atlas integration with BigQuery, VertexAI, Looker. This repo holds the code samples for the integration patterns.This would enable the customers to try it out themselves. 

 | Patterns | Description |
|----------|-------------|
| [MongoDB Collection level change stream to Pub Sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/CollectionLevelPubSub/README.md) | This pattern demonstrates how the MongoDB collection level changes have been monitored and published to GCP PUB/SUB topic using python code. |
| [MongoDB Database level change stream to Pub Sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/DBLevelPubSub/README.md) | This pattern demonstrates how the MongoDB database level changes have been monitored and published to GCP PUB/SUB topic using python code. |
| [Configuring BigQuery PubSub native connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/PubSubNativeConnector/README.md) | This pattern demonstrates consuming messages with defined schema from GCP PUB/SUB topic to GCP Bigquery table using native connector. |
| [Configuring Dataflow template for PubSub to BQ](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/DataflowBq/README.md) | This pattern demonstrates the data streams from GCP Pub/Sub to the GCP bigquery table by Dataflow Job using template "PubSub Subscription to BigQuery". |
| [Configuring BigQuery Kafka connector for MongoDB (either Confluent or Apache Kafka)](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/Confluentkafkamongodbtobq/README.md) | This pattern demonstrates the dataflow from MongoDB to the GCP bigquery table using the ConfluentKafka connector. |
| [MongoDB to BigQuery sync using the Spark connector](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/SparkConnectorMongotoBq/README.md) | This pattern demonstrates the dataflow from MongoDB to the GCP bigquery table using Spark connector. |
| [Real time integration of Vertex AI endpoint with change stream](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/VertexAIRealTimeIntegration/README.md) | This pattern demonstrates creation and deployment of Model on vertexAI and its real-time integration with MongoDB changestream. |
| [Reverse batch sync from BigQuery to MongoDB](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/BQtoMongodb/README.md) | This pattern demonstrates the dataflow from GCP bigquery table to MongoDB collection by dataflow job using "BigQuery to MongoDB" template. |



# Pre-requisite

## Create MongoDB Cluster with Database and Collections
- **Create an Account**:
  * If you don't already have one, create an account with your MongoDB cloud service provider. For this example, we'll use MongoDB Atlas.
- **Log in**:
  * Log in to the MongoDB Atlas with existing account credentials.
- **Create Cluster**:
  * Create a cluster as described [here](https://www.mongodb.com/docs/guides/atlas/cluster/) 
  * whitelist the required IPs to be accessed as described [here](https://www.mongodb.com/docs/atlas/security/ip-access-list/).
- **Create Database and Collection**:
  * Create the Database and the Collection in the Cluster.
    
  **Note:**
    For the scope of this workshop, create the collection Customer **"sample_analytics.Customer"** with the below document structure
    ```
     {
       "_id": "1",
       "username": "CSCollectionleveltoGCPpubsub",
       "name": "Derek Curtis",
       "address": "565 Hodge Motorway Suite 101 Wendyberg, FL 57099",
       "email": "qgibson@hotmail.com"
     }
    ```

## Create GCP Account
- **Create an Account**:
  * If you don't already have one, create an account with your GCP provider.
- **Log in**:
  * Log in to the account with the credentials.
- **Enable APIs**:
  * Click on the APIs and Service in the left panel, then enable the API's services.
- Detailed steps for creating GCP Account can be found [here](https://www.geeksforgeeks.org/how-to-create-a-free-tier-account-on-gcp/)

## Software to be Installed to Run the Application
Before you start using this application, ensure that you have the necessary software and libraries installed. Follow these steps to set up your development environment:
## 1. Python

Make sure you have Python installed on your system. Follow steps described [here](https://www.tutorialsteacher.com/python/install-python)
pip installation steps is described [here](https://www.geeksforgeeks.org/how-to-install-pip-on-windows/)

 **Poetry Setup**:
  ```bash
  pip3 install poetry
  poetry init
  brew install pyenv
  poetry env use <replace with your python version>
  poetry shell
  poetry install
  ```

## 2. PyMongo
To work with MongoDB databases, you'll need to install the PyMongo library. Use the following command to install it:

```bash
pip3 install pymongo
```

## 3. python-dotenv
For managing environment variables and configuration settings in your Python application, you'll need the python-dotenv library. Install it with the following command:

```bash
pip3 install python-dotenv
```

## 4. Google Cloud Pub/Sub
If your application interacts with Google Cloud Pub/Sub for messaging, install the google-cloud-pubsub library with the following command:

```bash
pip3 install google-cloud-pubsub
```

## 5. Certifi
To provide a certificate bundle for secure communication over HTTPS and SSL/TLS-encrypted protocols, install the certifi library:

```bash
pip3 install certifi
```

Ensure that you have Python and pip installed on your system before running these commands. These libraries and tools are essential for the proper functioning of the application.

Now, you're all set to use the application with the required dependencies in place.

## Steps to run each Projects

For Each Project run the main.py in its respective folder.


