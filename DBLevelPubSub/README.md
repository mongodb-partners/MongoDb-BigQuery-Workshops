## Pre-requisite
- **Create a Pub/Sub Topic:**
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the **"Use a schema"** checkbox.
  * For more details follow the below link to create Topic in GCP
  * **Ref Link**:
    * https://cloud.google.com/pubsub/docs/create-topic

  ![Create a Pub/Sub Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/48faec53-39c2-4411-a0c9-9b0ff6d93f24)

- **Create a Pub/Sub Subscription:**
  * Create the GCP pub/Sub Subscription
  * Configure other settings, such as acknowledgment mode and **Delivery type: PULL**, as per your requirements.
  * For more details follow the below link to create Subscription in GCP
  * **Ref Link**:
    * https://cloud.google.com/pubsub/docs/create-subscription
  
  ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/c997b4a0-c836-47f9-8b16-1a625acf8fdd)
  
  ![Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/cb0a6cdf-1a8f-4e33-8784-fec8dfbda77e)

## Listening Database Level Change Stream changes
- A database-level changestream definition allows you to monitor and capture changes occurring at the database level in a MongoDB database. You can use this feature to track changes to documents within any collection in the database.

- Format the message that must be published to the PUB/SUB which we created with the above steps in GCP.
  
  ![Pub/Sub Message Format](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/820a03fd-0669-4e7d-beb0-3e92e12460f1)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command:
```bash
python main.py
