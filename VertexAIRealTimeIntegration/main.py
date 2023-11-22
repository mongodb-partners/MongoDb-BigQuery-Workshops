from vertexrealtimeintegration import VertexRealTimeIntegration

def main():
    # Method is to demonstrate how the collection level change stream operation data will be published to the GCP pub/sub topics and subscription
    
    # Instance to the class and method is called.
    vertex_realtime = VertexRealTimeIntegration()
    vertex_realtime.process_user_trans()
                
    print("change stream to gcp topics is completed")


#calling the main method
main()


