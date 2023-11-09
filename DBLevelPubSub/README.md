## Overview
   This Pattern demostrates how the MongoDb database level changes has been monitored and published to GCP PUB/SUB topic using python code.
   
## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic without defining the schema as discribed [here](https://cloud.google.com/pubsub/docs/create-topic#create_a_topic_2)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/a90489e7-5713-4627-ae75-5b8226707aa7)
    
- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription with acknowledgment mode and **Delivery type: Pull** as described [here](https://cloud.google.com/pubsub/docs/create-subscription#create_a_pull_subscription)

    **Screenshot 1 :**
  
    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/8695e215-6a82-49d0-ae50-85819ba27762)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/9d9c44a9-f4bd-4c89-b655-7902802fbf3d)

## Listening Database Level Change Stream changes
- A database-level changestream definition allows you to monitor and capture changes occurring at the database level in a MongoDB database. You can use this feature to track changes to documents within any collection in the database.

- Format the message that must be published to the PUB/SUB which we created with the above steps in GCP.

  **Mongoinsert Screenshot**
  ![Mongoinsert](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/5ee2826e-f8a9-4eeb-b3f3-bb1dbcd3fa85)

  **PUB/SUB Topic Screenshot**
  ![Pub/Sub Message Format](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/9d7b55f5-f143-4e10-8ac1-6609809bf6d9)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
