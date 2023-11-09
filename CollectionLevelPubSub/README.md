## Overview
   This Pattern demostrates how the MongoDb collection level changes has been monitored  and published to GCP PUB/SUB topic using python code.
   
## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic without defining the schema can be found [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)
  
    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/633def66-2df5-42b3-9341-0c791b39ad07)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: Pull**, subscription creation can be found [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)
  * Once created under Message tab give **PULL** to get the messages that are process by the subscription 

    **Screenshot 1 :**

    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ea5e8933-9085-41da-8c8d-37540a4ae5b8)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/855e0a3f-1468-4381-a554-5f139f26e1eb)

## Listening to collection Level changes
- A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.
- When a change occurs in the monitored collection, the change stream document is sent to the GCP Pub/Sub topic.
- The Pub/Sub topic then sends the change stream document to all subscribed clients in real-time.
- Format the message that has to be published to the PUB/SUB, which we created in the above steps in GCP.

  **Mongo Insert Screenshot**
  ![mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/6b485882-f3a5-49e6-8bbf-d6022ba12bf4)

  **PUB/SUB Topic Screenshot**
  ![Application Uses Pub/Sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/cf22d5b7-2e92-4df1-b52a-6c787712be35)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".
