from pyspark.sql import SparkSession
import os
from dotenv import load_dotenv
from pyspark import SparkConf

from constants.constants import (
    MONGODB_CONNECTION_URI_STR,
    MONGODB_DATABASE_NAME,
    MONGODB_COLLECTION_NAME
)

load_dotenv()
class MongoToBQSync:
    def __init__(self):
         # Path to your service account key
        self.service_account_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        
        conf = SparkConf()
        conf.set("spark.app.name", "MySparkApp")
        conf.set("spark.master", "local[*]")  # Use "local" for local mode or a specific cluster URL
        conf.set("spark.cores.max", "4")  # Maximum number of CPU cores to use
        conf.set("spark.executor.memory", "2g")  # Executor memory per node
        conf.set("spark.driver.memory", "2g")  # Driver memory
        conf.set("spark.executor.instances", "2")  # Number of executor instances
        conf.set("spark.executor.cores", "2")  # Cores per executor

        # Create a Spark session with the necessary configurations
        self.spark = SparkSession.builder \
            .appName("MongoToBigQuerySync") \
            .master("local") \
            .config("spark.jars", "/Users/sowbaranikat/Downloads/mongo-spark-connector_2.12-2.4.0.jar, /Users/sowbaranikat/Downloads/mongo-java-driver-3.12.14.jar") \
            .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.34.0") \
            .config("spark.executor.extraJavaOptions", f"-Dcom.google.cloud.auth.service.account.json.keyfile={self.service_account_json}") \
            .config("spark.driver.extraJavaOptions", f"-Dcom.google.cloud.auth.service.account.json.keyfile={self.service_account_json}") \
            .getOrCreate()
        
        self.mongoconnstr = os.getenv(MONGODB_CONNECTION_URI_STR)
        self.dbname = os.getenv(MONGODB_DATABASE_NAME)
        self.collname = os.getenv(MONGODB_COLLECTION_NAME)

    def spark_connector_to_sink_mongodb_with_bq(self):
        
       # Define MongoDB configuration
        mongo_config = {
            "uri": os.getenv('MONGODB_CONNECTION_URI_STR'),
            "database": os.getenv('MONGODB_DATABASE_NAME'),
            "collection": os.getenv('MONGODB_COLLECTION_NAME')
        }

        # Read data from MongoDB
        mongo_df = self.spark.read.format("com.mongodb.spark.sql.DefaultSource").options(**mongo_config).load()
        
        #To print the mongodb schema
        mongo_df.printSchema()
     
        # Assigning the mongodb schema in json format to use the same in the bigquery table
        schema_json = mongo_df.schema.json()
        

        # Following configuration properties is used to store the data in hadoop of GCP Bucket storage
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.enable", "true")
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.application.default.credentials", "true")
        self.spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile", "/Users/sowbaranikat/Downloads/bq-sln-c8bae67168b4.json") 
        
        # Write data to BigQuery
        bq_config = {
            "table": "bq-sln.Customer.customer",
            "temporaryGcsBucket": "gs://temp_bucket",
            "credentialsFile": self.service_account_json  # Specify the service account JSON key file here
        }
        
        #To write the data into the BigQuery Table in GCP
        mongo_df.write.format("com.google.cloud.spark.bigquery") \
            .option("table", "bq-sln.Customer.customer") \
            .option("temporaryGcsBucket", bq_config["temporaryGcsBucket"]) \
            .option("credentialsFile", bq_config["credentialsFile"]) \
            .mode('overwrite') \
            .option("writeMethod", "direct") \
            .option("schema", schema_json) \
            .save();

        self.spark.stop()
    


