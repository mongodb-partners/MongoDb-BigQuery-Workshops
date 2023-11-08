## Overview
   This application is to demostrate how the MongoDb Database level change stream operations are been handled with GCP PUB/SUB topic and subscription using python code.
   
## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic without defining the schema
  * Detailed steps for topic creation can be found [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/7393d12e-07cc-4edf-91f7-28dbf769ec4f)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: Pull**
  * Once created under Message tab give **PULL** to get the messages that are process by the subscription
  * Detailed steps for Subscription creation can be found [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)

    **Screenshot 1 :**
  
    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/53f2d8c4-d475-45b1-8a2c-348d463df907)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/5165a2ba-306f-46de-994e-5a30fa41860b)

## Listening Database Level Change Stream changes
- A database-level changestream definition allows you to monitor and capture changes occurring at the database level in a MongoDB database. You can use this feature to track changes to documents within any collection in the database.

- Format the message that must be published to the PUB/SUB which we created with the above steps in GCP.

  **Mongoinsert Screenshot**
  ![Mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/7fe0ed6c-5b4e-4189-881a-a5515cfbdb58)

  **PUB/SUB Topic Screenshot**
  ![Pub/Sub Message Format](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/61f89007-420a-422f-abaf-ac6cf5bf1db4)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
