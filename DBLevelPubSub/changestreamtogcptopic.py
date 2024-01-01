import json
import os
import certifi
from pymongo import MongoClient
from google.cloud import pubsub_v1
from dotenv import load_dotenv
from constants.constants import (
    MONGODB_CONNECTION_URI_STR,
    MONGODB_DATABASE_NAME,
    GCP_TOPIC_PATH,
    FULLDOCUMENT_KEY,
    OPERATION_TYPE_KEY
)

load_dotenv()

class ChangeStreamToGCPTopic:
    def __init__(self):
        self.mongoconnstr = os.getenv(MONGODB_CONNECTION_URI_STR)
        self.dbname = os.getenv(MONGODB_DATABASE_NAME)
        self.gcptopicname = os.getenv(GCP_TOPIC_PATH)

   
    def to_perform_mongo_changestream_to_gcp_topics(self):
        mongo_client = MongoClient(self.mongoconnstr ,tlsCAFile=certifi.where())
        db = mongo_client[self.dbname]
        change_stream = db.watch(full_document="updateLookup")

        # Initialize Pub/Sub publisher
        publisher = pubsub_v1.PublisherClient()
        topic_path = self.gcptopicname

        # Listen to MongoDB change stream and publish to Pub/Sub
        for change in change_stream:
            # To skip delete operation to PUB/SUB
            if change[OPERATION_TYPE_KEY].lower() == "delete":
                continue;
            else:
                # Get the change event document as a Pub/Sub message
                fulldocument = change[FULLDOCUMENT_KEY]
                
                # Deleting unique id which is specific to MongoDB
                del fulldocument["_id"]
                
                fulldocument["operation_type"] = change[OPERATION_TYPE_KEY]
                
                # Publish the message to Pub/Sub
                future = publisher.publish(topic_path, json.dumps(fulldocument).encode('utf-8'))
                
                # Optional: Handle errors and retries
                try:
                    future.result()
                except Exception as e:
                    print(f"Error publishing database level changes to Pub/Sub: {e}")
