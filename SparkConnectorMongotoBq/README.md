## Pre-requisite
- ** To use pyspark in the code need to innstall pyspark 
     ```bash
     pip install pyspark
     ```
- **Table Creation:**
  * Create a table for the schema defined in Bigquery.
  * Detailed steps for GCP table creation can be found [here](https://cloud.google.com/bigquery/docs/tables)
  
    ![Table Creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/24d38411-a9ad-47e6-808c-237645f94fbd)

- **Create GCP Bucket:**
  * Enable it to Multi-region and set public access prevention on the bucket.
  * Detailed steps for GCP Bucket creation can be found [here](https://cloud.google.com/storage/docs/creating-buckets)
  
    ![Create GCP Bucket](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/ac0b96df-e37e-4b61-bcb4-86206f294a11)

## Spark Connector to sync MongoDB collection to the GCP Bigquery Table:
   * This python application is used to sync the MongoDB Atlas database collections to the GCP Bigquery table in the desire GCP buckest storage.
   * Loads the data from MongoDB collection "sample_analytics.Customer" with spark connector 
   * Write the loaded data to the destination GCP BigQuery table that we created.

## Steps to Run Application
1. Follow the common readme file to install all the required software.
2. Update the required configuration details in the .env file.
3. Open the terminal in the respective project folder and run the command "python main.py".

  


