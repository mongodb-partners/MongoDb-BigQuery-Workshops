## Pre-requisite

### Create a Pub/Sub Topic
- In the Google Cloud Console, navigate to "Pub/Sub" from the left-side menu.
- Click on the "Topics" tab.
- Click the "Create a topic" button.
- Give your topic a name, e.g., "collectionLevelChangestreamTopic," and click "Create."
- If you need to define the message structure, click the "Use a schema" checkbox.

  ![Create a Pub/Sub Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/90228a4e-e735-4b12-a5b7-672c76980c15)

### Create a Pub/Sub Subscription
- From the "Topics" tab, select the topic you just created (e.g., "collectionLevelChangestreamTopic").
- Click the "Create subscription" button.
- Provide a name for your subscription (e.g., "collectionLevelChangestreamTopic-sub").
- Configure other settings, such as acknowledgment mode and delivery type, as per your requirements.
- Click "Create" to create the subscription.

  ![Create a Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/b56a07f0-a7c3-42a4-8899-518992077e86)

  ![Pub/Sub Subscription](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/c79f6e03-a421-45cf-9cff-86111c35327b)

## Listening to collection Level changes
- A collection-level change stream in MongoDB allows you to monitor and capture changes occurring in a specific collection. You can use this feature to track changes to documents within that collection.
- When a change occurs in the monitored collection, the change stream document is sent to the GCP Pub/Sub topic.
- The Pub/Sub topic then sends the change stream document to all subscribed clients in real-time.
- Format the message that has to be published to the PUB/SUB, which we created in the above steps in GCP.

  ![Application Uses Pub/Sub](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/04271301-e466-4061-b114-242e2142249d)

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".
