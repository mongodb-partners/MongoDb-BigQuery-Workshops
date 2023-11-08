from mongotobqsync import MongoToBQSync

def main():
    # Method is to demonstrate how the collection level change stream operation data will be published to the GCP pub/sub topics and subscription
    
    # Instance to the class and method is called.
    mongo_to_bq = MongoToBQSync()
    mongo_to_bq.spark_connector_to_sink_mongodb_with_bq()
    
    print("Data is sync is done from mongodb to BQTable")
                
#calling the main method
main()