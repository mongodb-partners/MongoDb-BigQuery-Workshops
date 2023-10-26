## Pre-requisite
- **Pub/Sub Topic creation**:
  * Create the GCP pub/Sub topic
  * If incase to define the message structure, click the "Use a schema" checkbox.
  * Follow the below link to create Topic in GCP
- **Ref Link**:
  * https://cloud.google.com/pubsub/docs/create-topic
  
  ![Create PUB/SUB Topic](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/7e092f7d-178a-4da6-b8ff-39c82d033cc7)

- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
- **Ref Link**:
  * https://cloud.google.com/bigquery/docs/tables
  
  ![Table Creation](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/3abc3b11-f1a6-4fd0-8ebb-9a57c84422eb)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
- **Ref Link**:
  * https://cloud.google.com/storage/docs/creating-buckets
  
  ![Create GCP Bucket](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/51dc1308-918e-4906-9253-ae53f8ff2083)
  
- **Create Dataflow Job Template:**
  * Create the dataflow job template to access big query tabel
  * Check the status once the job is created
  * Follow the below link to create dataflow template
- **Ref Link**:
  * https://cloud.google.com/dataflow/docs/guides/templates/running-templates
  
  ![Create Dataflow Job Template](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/57aa94d1-f40a-40a3-8586-f0df25df965d)

## Dataflow Template for PUB/Sub to BQ
- Publishing the data to the PUB/Sub topic will reflect in the Job graph.
- **Ref Link**:
  * https://cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-to-bigquery
  
  ![Dataflow Template for PUB/Sub to BQ](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/4bcc49a0-525c-4280-b0c7-b4b61066242e)

- Once after publishing, the graph will reflect in the Dataflow job created as below.
  
  ![Dataflow Job Graph](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/96880d32-6f05-408f-b736-8796f8c1dddf)

- Published messages will get reflected in the BigQuery destination table.
  
  ![BigQuery Destination Table](https://github.com/TSowbaranika/BQGCPAtlas/assets/109083730/0365fdc3-3dc1-4830-82e5-9b88d91de613)
