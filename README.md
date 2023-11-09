# Pre-requisite

## Create MongoDB Cluster with Database and Collections
- **Create an Account**:
  * If you don't already have one, create an account with your MongoDB cloud service provider. For this example, we'll use MongoDB Atlas.
- **Log in**:
  * Log in to the MongoDB Atlas with existing account credentials.
- **Create Cluster**:
  * Create a Cluster and whitelist the required IPs to be accessed.
- **Create Database and Collection**:
  * Create the Database and the Collection in the Cluster.
- Detailed steps for cluster creation can be found [here](https://www.mongodb.com/docs/guides/atlas/cluster/)

  **Note:**
    For the scope of this workshop, Cretae the collection Customer **"sample_analytics.Customer"** with the below document structure
    ```
     {
       "_id": "1",
       "username": "CSCollectionleveltoGCPpubsub",
       "name": "Derek Curtis",
       "address": "565 Hodge Motorway Suite 101 Wendyberg, FL 57099",
       "email": "qgibson@hotmail.com"
     }
    ```

## Create GCP Account
- **Create an Account**:
  * If you don't already have one, create an account with your GCP provider.
- **Log in**:
  * Log in to the account with the credentials.
- **Enable APIs**:
  * Click on the APIs and Service in the left panel, then enable the API's services.
- Detailed steps for creating GCP Account can be found [here](https://www.geeksforgeeks.org/how-to-create-a-free-tier-account-on-gcp/)

## Software to be Installed to Run the Application
Before you start using this application, ensure that you have the necessary software and libraries installed. Follow these steps to set up your development environment:

- **Poetry Setup**:
  ```bash
  poetry init
  poetry install


## 2. Python

Make sure you have Python installed on your system. If not, you can use the following command to install Python 3 using Homebrew (Mac users):

```bash
brew install python3
```

## 3. PyMongo
To work with MongoDB databases, you'll need to install the PyMongo library. Use the following command to install it:

```bash
pip install pymongo
```

## 4. python-dotenv
For managing environment variables and configuration settings in your Python application, you'll need the python-dotenv library. Install it with the following command:

```bash
pip install python-dotenv
```

## 5. Google Cloud Pub/Sub
If your application interacts with Google Cloud Pub/Sub for messaging, install the google-cloud-pubsub library with the following command:

```bash
pip install google-cloud-pubsub
```

## 6. Certifi
To provide a certificate bundle for secure communication over HTTPS and SSL/TLS-encrypted protocols, install the certifi library:

```bash
pip install certifi
```

Ensure that you have Python and pip installed on your system before running these commands. These libraries and tools are essential for the proper functioning of the application.

Now, you're all set to use the application with the required dependencies in place.

## Steps to run each Projects

For Each Project run the main.py in its respective folder.


