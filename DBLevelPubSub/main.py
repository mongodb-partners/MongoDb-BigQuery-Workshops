from changestreamtogcptopic  import ChangeStreamToGCPTopic

def main():
    # Method is to demonstrate how the Database level change stream operation data will be published to the GCP pub/sub topics and subscription
    
    # Instance to the class and method is called.
    dbchangestream_to_gcp = ChangeStreamToGCPTopic()
    dbchangestream_to_gcp.to_perform_mongo_changestream_to_gcp_topics()
          
    print("change stream to gcp topics is completed")


#calling the main method
main()