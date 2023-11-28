from pipelineobservability import PipelineObservability

def main():
    # Method is to demonstrate how the collection level change stream operation data will be published to the GCP pub/sub topics and subscription
    
    # Instance to the class and method is called.
    pipeline_observability = PipelineObservability()
    pipeline_observability.to_perform_pipeline_observability()
                
    print("Pipeline Observability is completed")


#calling the main method
main()