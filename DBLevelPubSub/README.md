## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * Detailed steps for topic creation : [Create Topic in GCP](https://cloud.google.com/pubsub/docs/create-topic)

    ![Create a Pub/Sub Topic](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/506f1cb3-835f-4023-b258-2670b91ff409)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **Delivery type: PULL**, as per your requirements.
  * Detailed steps for Subscription creation : [Create Subscription in GCP](https://cloud.google.com/pubsub/docs/create-subscription)

    **Screenshot 1 :**
  
    ![Create a Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/d45a5719-58af-4a29-ad71-14bc1d4aa9fa)

    **Screenshot 2 :**
  
    ![Pub/Sub Subscription](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/5165a2ba-306f-46de-994e-5a30fa41860b)

## Listening Database Level Change Stream changes
- A database-level changestream definition allows you to monitor and capture changes occurring at the database level in a MongoDB database. You can use this feature to track changes to documents within any collection in the database.

- Format the message that must be published to the PUB/SUB which we created with the above steps in GCP.
  
  ![Pub/Sub Message Format](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/7304e18c-661a-414f-90b8-3d793b1855b0)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
