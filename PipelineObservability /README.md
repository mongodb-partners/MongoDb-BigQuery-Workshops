## Overview
   This pattern demostrates how the MongoDB Status collection and Pub Sub Metrics by creating the GCP PUB/SUB topics by populating the data to the topics using python code.

## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2) with default subscription to the topic without defining schema.

    ![topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/b0d28333-abc8-445f-ba23-7b39117221d4)

## Monitoring the PUB/SUB Metrics:

  * Click [here](https://cloud.google.com/pubsub/docs/monitoring) to monitor your Pub/Sub usage in the Google Cloud console using Monitoring.
 
    ![Monitoring](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/15bf461e-7ec7-4e48-a7e1-861191fb9882)

  * Our Python code will publish the message to the created topic and will also insert the updated/inserted documents count to the Metrics collection in the mongoDB by incrementing the count value also updated the last updated time.
 
    Multiple Insert:
    
    ![Insert Many](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ebe64f1a-586e-408f-9c5c-6c3cadf230a5)

    Monitoring:
    
    ![Monitoring](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/15bf461e-7ec7-4e48-a7e1-861191fb9882)

    Metrics updated in Mongodb collection:

    ![Metric](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6438e7f4-0d39-47da-8fac-5a34a8d99134)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the [.env](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/PipelineObservability%20/.env) file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py

    
  
  
    
