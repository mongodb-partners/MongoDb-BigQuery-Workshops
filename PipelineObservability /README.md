## Overview
   Pipeline observability refers to the ability to monitor and understand the health, performance, and behavior of a data pipeline or workflow within a system. In this pattern we will monitor the metrics of PUB/SUB using GCP native monitoring explorer also we will update the metrics in the MongoDB collection.

## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2) with default subscription to the topic.

    ![topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/b0d28333-abc8-445f-ba23-7b39117221d4)

- **Monitoring Collections:**
  * Use the sample mongoDb collection **"sample_mflix.users"**

- **Collection for Metrics:**
  * Create a new Collection in the database **"sample_mflix.metrics"** Always update the count value by incrementing the count value.
  ``` bash
  {
  "_id": {
    "$oid": "6564cfd608e2f8f60850873b"
  },
  "metric_type": "pubsub",
  "metric_name": "publishedcount",
  "count": 0
  }
  ```  

## Monitoring the PUB/SUB Metrics:

  * Setup the Monitoring metrics **"Publish Request"** for PUB/SUB topic is described [here](https://cloud.google.com/pubsub/docs/monitoring).
 
    ![Monitoring](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/15bf461e-7ec7-4e48-a7e1-861191fb9882)

  * Our Python code will publish the message to the created topic and will also insert the updated/inserted documents count to the Metrics collection in the mongoDB by incrementing the count value also updated the last updated time.
 
    **Use mongo shell for Multiple Insert:**
    
    ![Insert Many](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ebe64f1a-586e-408f-9c5c-6c3cadf230a5)

    **Monitoring:**
    
    ![Monitoring](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/15bf461e-7ec7-4e48-a7e1-861191fb9882)

    **Metrics updated in Mongodb collection:**

    ![Metric](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6438e7f4-0d39-47da-8fac-5a34a8d99134)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/PipelineObservability%20/.env) file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
```

    
  
  
    
