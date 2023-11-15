from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv
from pyspark import SparkConf

# Assuming these are the constant names in your constants file
from constants.constants import (
    MONGODB_CONNECTION_URI_STR,
    MONGODB_DATABASE_NAME,
    MONGODB_COLLECTION_NAME
)

# Load environment variables
load_dotenv()

class MongoToBQSync:
    def __init__(self):
        # Path to your Google Cloud service account key
        self.service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        
        # Spark configuration
        conf = SparkConf()
        conf.set("spark.app.name", "MySparkApp")
        conf.set("spark.master", "local[*]")
        conf.set("spark.cores.max", "4")
        conf.set("spark.executor.memory", "2g")
        conf.set("spark.driver.memory", "2g")
        conf.set("spark.executor.instances", "2")
        conf.set("spark.executor.cores", "2")

        # Create a Spark session with the necessary configurations
        self.spark = SparkSession.builder \
            .config(conf) \
            .config("spark.jars", f"{os.getenv('MONGO_SPARK_CONNECTOR_JAR_PATH')}, {os.getenv('MONGO_JAVA_DRIVER_JAR_PATH')}") \
            .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.34.0") \
            .config("spark.executor.extraJavaOptions", f"-Dcom.google.cloud.auth.service.account.json.keyfile={self.service_account_json}") \
            .config("spark.driver.extraJavaOptions", f"-Dcom.google.cloud.auth.service.account.json.keyfile={self.service_account_json}") \
            .getOrCreate()
        
        # MongoDB configurations
        self.mongoconnstr = os.getenv(MONGODB_CONNECTION_URI_STR)
        self.dbname = os.getenv(MONGODB_DATABASE_NAME)
        self.collname = os.getenv(MONGODB_COLLECTION_NAME)

    def spark_connector_to_sink_mongodb_with_bq(self):
        # Define MongoDB configuration
        mongo_config = {
            "uri": self.mongoconnstr,
            "database": self.dbname,
            "collection": self.collname
        }

        # Read data from MongoDB
        mongo_df = self.spark.read.format("com.mongodb.spark.sql.DefaultSource").options(**mongo_config).load()
        
        # Print the MongoDB schema
        mongo_df.printSchema()
     
        # Assigning the MongoDB schema in JSON format to use in the BigQuery table
        schema_json = mongo_df.schema.json()

        # Hadoop configuration for Google Cloud
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.enable", "true")
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.application.default.credentials", "true")
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", self.service_account_json)

        # BigQuery configuration
        bq_dataset_name = os.getenv('BIGQUERY_DATASET_NAME')
        bq_table_name = os.getenv('BIGQUERY_TABLE_NAME')
        temp_gcs_bucket = os.getenv('TEMPORARY_GCS_BUCKET')

        # Writing data to BigQuery
        mongo_df.write.format("bigquery") \
            .option("table", f"{bq_dataset_name}.{bq_table_name}") \
            .option("temporaryGcsBucket", temp_gcs_bucket) \
            .option("credentialsFile", self.service_account_json) \
            .mode('overwrite') \
            .option("writeMethod", "direct") \
            .option("schema", schema_json) \
            .save()

        # Stop the Spark session
        self.spark.stop()

# Example usage
if __name__ == "__main__":
    sync = MongoToBQSync()
    sync.spark_connector_to_sink_mongodb_with_bq()
