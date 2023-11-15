## Overview
   This Pattern demostrates how the MongoDb collection level changes has been monitored  and published to GCP PUB/SUB topic using python code.
   
## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic without defining the schema as described [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)
  
    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/80958e4f-e677-4976-a359-cedf101e6109)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: Pull** as described [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)

    **Screenshot 1 :**

    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/c5c1ef20-8718-404c-ac2b-b8beca99e208)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/20f4a3e9-5dd0-4b7d-8cf4-69e207c0dd1f)

## Listening to collection Level changes
- A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.
- When a change occurs in the monitored collection, the change stream document is sent to the GCP Pub/Sub topic.
- The Pub/Sub topic then sends the change stream document to all subscribed clients in real-time.
- Format the message that has to be published to the PUB/SUB, which we created in the above steps in GCP.

  **Mongo Insert Screenshot**
  ![mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d8fd8be4-006a-4fa7-99d5-8352a5998027)

  **PUB/SUB Topic Screenshot**

  - Once message published to the GCP Topic,we can **PULL** message under Message Tab in subscription.
    
  ![Application Uses Pub/Sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8a2ba2e6-e090-494e-892a-8ff1a9ccaac6)

## Steps to Run Application
1. Follow the common readme [file](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/blob/dev_bq-workshop_demo/README.md) to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".
