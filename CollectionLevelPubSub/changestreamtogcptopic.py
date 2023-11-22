import json
import os
import certifi
from pymongo import MongoClient
from google.cloud import pubsub_v1
from dotenv import load_dotenv

from constants.constants import (
    MONGODB_CONNECTION_URI_STR,
    MONGODB_DATABASE_NAME,
    MONGODB_COLLECTION_NAME,
    GCP_TOPIC_PATH,
    FULLDOCUMENT_KEY,
    OPERATION_TYPE_KEY
)

load_dotenv()
class CollectionChangeStreamToGCPTopic:
    def __init__(self):
        self.mongoconnstr = os.getenv(MONGODB_CONNECTION_URI_STR)
        self.dbname = os.getenv(MONGODB_DATABASE_NAME)
        self.collectionname = os.getenv(MONGODB_COLLECTION_NAME)
        self.gcptopicname = os.getenv(GCP_TOPIC_PATH)
        self.service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

   
    def to_perform_mongo_changestream_to_gcp_topics(self):
        mongo_client = MongoClient(self.mongoconnstr ,tlsCAFile=certifi.where())
        db = mongo_client[self.dbname]
        collection = db[self.collectionname]
        change_stream = collection.watch(full_document="updateLookup")

        # Initialize Pub/Sub publisher
        publisher = pubsub_v1.PublisherClient()
        topic_path = self.gcptopicname

        # Listen to MongoDB change stream and publish to Pub/Sub
        for change in change_stream:
             # Get the change event document as a Pub/Sub message
            if change[OPERATION_TYPE_KEY].lower() == "delete":
                continue;
            else:
                
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
                    print(f"Error publishing collection level changes to Pub/Sub: {e}")
