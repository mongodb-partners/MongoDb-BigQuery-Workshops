
## Overview
   This pattern demonstrate how we can use looker as a product to explore, share, and visualize our data in MongoDB, So that we can make better business decisions.
   
## Pre-requisite

   - **Connections to DB:**
     * Creating the Connections to the DB in the looker is described [here](https://cloud.google.com/looker/docs/connecting-to-your-db)

   - **Project Creation:**
     * Creating the Project in the Looker is described [here](https://cloud.google.com/looker/docs/create-projects#creating_a_project)

   - **MongoDb Collection:**
     * Mongodb collection **"sample_supplies.sales"** is used for the looker integration

   - **Looker Dashboard creation:**
     * Creating a dashboard from a Look or an Explore is described [here](https://cloud.google.com/looker/docs/creating-user-defined-dashboards#creating_a_dashboard_from_a_look_or_an_explore)

## Looker Integration with MongoDB:

   - **Set Up Looker and Database Connection**

        - **Access to Looker:**
           Ensure you have access to a Looker instance. Your organization might have its own Looker environment.
   
        - **Connect to Database:**
           In Looker, you need to connect to your database. This is typically done through the Admin section where you can add a new database connection by specifying the type of database (e.g., MongoBI.), and providing connection details like host, port, username, and password.

          ![connection creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/0868c8e9-7b9a-4336-a8fd-b4ec63cb549b)

          ![test connection](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/434769fa-c07f-4c35-9084-64b765d1be99)
   - **Create a Looker Project**

      - **Start a New Project:**
        In Looker, a project is a collection of files that define your data models. You can create a new project in the Develop menu. Looker will guide you through initializing a new project.

        ![Project](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/b733a56e-a6a9-47db-b648-ce5c2e985857)
      
      - **Create Model and View Files:**
        In your project, you will create LookML files (Looker’s modeling language). A basic project includes model files (defining the connection to your database and including view files) and view files (defining the dimensions and measures - essentially, what you can query).

   - **Define Models and Explore**
     
      - **Define Dimensions and Measures:**
        In view files, define dimensions (fields you can group by) and measures (aggregations like counts, sums, averages).

      - **Create Explores:**
       In model files, create explores which are essentially the starting points for queries. They determine which fields are available for querying in the Looker UI.

      ![Explore model](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/186ffb4c-48e1-4921-bb3d-87e76b13fbe3)

   - **Query Data**
     
       - **Explore Data:**
         Once your model is set up, you can start exploring. Go to the Explore section, select the explore you created, and start querying. You can select dimensions and measures, apply filters, and perform various types of data analysis.

         ![Explore query](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1e57143e-3369-4e8a-becd-a046c8886c0e)

   - **Create Visualizations and Dashboards**
       
       - **Visualize Data:**
         After running queries, you can visualize your results in Looker. Looker offers various types of visualizations like charts, graphs, and tables.

         ![visualize data](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/62951b7e-69f3-4531-b621-3274971f9c68)
         
       - **Create Dashboards:**
         Combine different visualizations into a dashboard for a comprehensive view. In the Looker UI, you can create a new dashboard, add your visualizations, arrange them, and configure filters.

         ![dashboard creation](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/1881a43b-0721-4f5d-b0c4-6f6bd208e658)
      
       - **Save and Share Dashboards:**
         Once your dashboard is ready, save it and share it with your team or other stakeholders. You can set permissions to control who can see and edit your dashboard.

         ![Dashboard](https://github.com/mongodb-partners/MongoDb-BigQuery-Workshops/assets/109083730/7c389095-608f-478b-b47f-0611555a94ce)
      
 

   
