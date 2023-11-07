## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation can be found [here](https://cloud.google.com/pubsub/docs/create-topic)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/33313e48-f2b5-4972-abb1-88a9624919a4)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **Delivery type: Pull**, as per your requirements.
  * Detailed steps for Subscription creation can be found [here](https://cloud.google.com/pubsub/docs/create-subscription)

    **Screenshot 1 :**

    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/59824c75-3727-46b8-9b73-aa77b9607f66)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/855e0a3f-1468-4381-a554-5f139f26e1eb)

## Listening to collection Level changes
- A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.
- When a change occurs in the monitored collection, the change stream document is sent to the GCP Pub/Sub topic.
- The Pub/Sub topic then sends the change stream document to all subscribed clients in real-time.
- Format the message that has to be published to the PUB/SUB, which we created in the above steps in GCP.

  ![Application Uses Pub/Sub](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/54aa7265-5ed2-4bd3-b8d9-c41511a76a10)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".
