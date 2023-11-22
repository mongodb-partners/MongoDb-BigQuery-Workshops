from pymongo import MongoClient
from bson import json_util
import requests
import json
import certifi
import os
from dotenv import load_dotenv


from constants.constants import (
    MONGODB_CONNECTION_URI_STR,
    MONGODB_DATABASE_NAME,
    MONGODB_COLLECTION_NAME
)

load_dotenv()
class VertexRealTimeIntegration:
    def __init__(self):
        self.mongoconnstr = os.getenv(MONGODB_CONNECTION_URI_STR)
        self.dbname = os.getenv(MONGODB_DATABASE_NAME)
        self.collectionname = os.getenv(MONGODB_COLLECTION_NAME)
        self.endpoint_id = os.getenv('ENDPOINT_ID')
        self.project_id = os.getenv('PROJECT_ID')
        self.access_token = os.getenv('ACCESS_TOKEN')

    def process_user_trans(self):
        pipeline = [
            {"$match": {"$or": [
                {"operationType": "insert"},
                {"operationType": "update", "updateDescription.updatedFields.amouunt": {"$exists": True}}
            ]}}
        ]
        
        mongo_client = MongoClient(self.mongoconnstr ,tlsCAFile=certifi.where())
        db = mongo_client[self.dbname]
        collection = db[self.collectionname]

        change_stream = collection.watch(pipeline, full_document='updateLookup')
        
        
        print("==> Going through the stream a first time & record a resumeToken")
        index_of_operation_to_restart_from = 5
        index_of_incident = 8
        counter = 0
        resume_token = None

        for event in change_stream:
            updated_transaction = event['fullDocument']
            updated_transaction["userId"] = updated_transaction["_id"]
            
            del updated_transaction["_id"]
            del updated_transaction["email"]
            req_body = {}
            json_array= []
            json_array.append(updated_transaction)
            req_body["instances"] = json_array

            # Method to call Deployed API in the vertexAI
            centroid_id = self.get_prediction_from_bq_model_user_transaction(req_body)

            # Update MongoDB
            collection.update_one({"_id": updated_transaction["userId"]}, {"$set": {"centroid_id": centroid_id}})
            
            if index_of_operation_to_restart_from == counter:
                resume_token = event["resumeToken"]
            
            #print(event)
            counter += 1
            if counter == index_of_incident:
                break

        print("==> Let's imagine something wrong happened and I need to restart my Change Stream.")
        print("==> Starting from resumeToken=" + str(resume_token))
        
        # Assuming 'get_resume_after' returns the resume token for the Python MongoDB driver
        resume_token = collection.watch(pipeline).resume_after(resume_token).next().get_resume_after()
        
        # Assuming 'print_events_for_user_transaction' is a placeholder function; you may need to implement its logic
        collection.watch(pipeline).resume_after(resume_token).foreach(self.print_events_for_user_transaction())

    # Assuming the following function is implemented elsewhere in your code
    def get_prediction_from_bq_model_user_transaction(self,json_input_string):
        post_url_user_trans = "https://us-central1-aiplatform.googleapis.com/v1/projects/"+self.project_id+"/locations/us-central1/endpoints/"+self.endpoint_id+":predict";
        # Replace "YOUR_POST_URL_USER_TRANS" with your actual endpoint URL
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer "+ self.access_token
            # Replace "YOUR_ACCESS_TOKEN" with your actual access token
        }
        centroid_id = ""
        try:
            response = requests.post(post_url_user_trans, headers=headers, data=str(json_input_string).encode('utf-8'))
            response.raise_for_status()

            print(f"POST Response Code :: {response.status_code}")

            if response.status_code == requests.codes.ok:  # success
                result_json = response.json()

                print(result_json)
                predictions_json = result_json.get("predictions", [])
                if predictions_json:
                    prediction_object = predictions_json[0]
                    nearest_centroid_array = prediction_object.get("nearest_centroid_id", [])
                    try:
                        centroid_id = str(nearest_centroid_array[0]).lower()
                    except Exception as e:
                        print(f"Exception: {str(e)}")

                print(f"centroid_id: {centroid_id}")

            else:
                print("POST request did not work.")

        except requests.exceptions.RequestException as e:
            print(f"Exception: {str(e)}")

        return centroid_id
    
    def print_events_for_user_transaction(self):
        return lambda event: print(event)


