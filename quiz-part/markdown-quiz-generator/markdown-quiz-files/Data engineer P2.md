# GCP Data engineer test part2

---

1. You have a data pipeline with a Dataflow job that aggregates and writes time series metrics to Bigtable. You notice that data is slow to update in Bigtable. This data feeds a dashboard used by thousands of users across the organization. You need to support additional concurrent users and reduce the amount of time required to write the data. Which two actions should you take? (Choose two.)
 

    - [ ] A. Configure your Dataflow pipeline to use local execution
    - [x] B. Increase the maximum number of Dataflow workers by setting maxNumWorkers in PipelineOptions
    - [x] C. Increase the number of nodes in the Bigtable cluster
    - [ ] D. Modify your Dataflow pipeline to use the Flatten transform before writing to Bigtable
    - [ ] E. Modify your Dataflow pipeline to use the CoGroupByKey transform before writing to Bigtable

2. As your organization expands its usage of GCP, many teams have started to create their own projects. Projects are further multiplied to accommodate different stages of deployments and target audiences. Each project requires unique access control configurations. The central IT team needs to have access to all projects. Furthermore, data from Cloud Storage buckets and BigQuery datasets must be shared for use in other projects in an ad hoc way. You want to simplify access control management by minimizing the number of policies. Which two steps should you take? (Choose two.)
    - [ ] A. Use Cloud Deployment Manager to automate access provision.
    - [x] B. Introduce resource hierarchy to leverage access control policy inheritance.
    - [x] C. Create distinct groups for various teams, and specify groups in Cloud IAM policies.
    - [ ] D. Only use service accounts when sharing data for Cloud Storage buckets and BigQuery datasets.
    - [ ] E. For each Cloud Storage bucket or BigQuery dataset, decide which projects need access. Find all the active members who have access to these projects, and create
a Cloud IAM policy to grant access to all these users.

3. Your company has a hybrid cloud initiative. You have a complex data pipeline that moves data between cloud provider services and leverages services from each of the cloud providers. Which cloud-native service should you use to orchestrate the entire pipeline?
   
    - ( ) A. Cloud Dataflow
    - (x) B. Cloud Composer
    - ( ) C. Cloud Dataprep
    - ( ) D. Cloud Dataproc

4. You work for a shipping company that uses handheld scanners to read shipping labels. Your company has strict data privacy standards that require scanners to only transmit tracking numbers when events are sent to Kafka topics. A recent software update caused the scanners to accidentally transmit recipients’ personally identifiable information (PII) to analytics systems, which violates user privacy rules. You want to quickly build a scalable solution using cloud-native managed services to prevent exposure of Pll to the analytics systems. What should you do?

    - ( ) A. Create an authorized view in BigQuery to restrict access to tables with sensitive data.
    - ( ) B. Install a third-party data validation tool on Compute Engine virtual machines to check the incoming data for sensitive information.
    - ( ) C. Use Cloud Logging to analyze the data passed through the total pipeline to identify transactions that may contain sensitive information.
    - (x) D. Build a Cloud Function that reads the topics and makes a call to the Cloud Data Loss Prevention (Cloud DLP) API. Use the tagging and confidence levels to either pass or quarantine the data in a bucket for review.

5. You need to set access to BigQuery for different departments within your company. Your solution should comply with the following requirements:
    * Each department should have access only to their data.
    * Each department will have one or more leads who need to be able to create and update tables and provide them to their team.
    * Each department has data analysts who need to be able to query but not modify data.
    * How should you set access to the data in BigQuery?

    - ( ) A. Create a dataset for each department. Assign the department leads the role of OWNER, and assign the data analysts the role of WRITER on their dataset.
    - (x) B. Create a dataset for each department. Assign the department leads the role of WRITER, and assign the data analysts the role of READER on their dataset.
    - ( ) C. Create a table for each department. Assign the department leads the role of Owner, and assign the data analysts the role of Editor on the project the table is in.
    - ( ) D. Create a table for each department. Assign the department leads the role of Editor, and assign the data analysts the role of Viewer on the project the table is in.
    
6. You have a data stored in BigQuery. The data in the BigQuery dataset must be highly available. You need to define a storage, backup, and recovery strategy of this data that minimizes cost. How should you configure the BigQuery table that have a recovery point objective (RPO) of 30 days?

    - ( ) A. Set the BigQuery dataset to be regional. In the event of an emergency, use a point-in-time snapshot to recover the data.
    - ( ) B. Set the BigQuery dataset to be regional. Create a scheduled query to make copies of the data to tables suffixed with the time of the backup. In the event of an emergency, use the backup copy of the table.
    - (x) C. Set the BigQuery dataset to be multi-regional. In the event of an emergency, use a point-in-time snapshot to recover the data.
    - ( ) D. Set the BigQuery dataset to be multi-regional. Create a scheduled query to make copies of the data to tables suffixed with the time of the backup. In the event of an emergency, use the backup copy of the table.
    
7. You operate a logistics company, and you want to improve event delivery reliability for vehicle-based sensors. You operate small data centers around the world to capture these events, but leased lines that provide connectivity from your event collection infrastructure to your event processing infrastructure are unreliable, with unpredictable latency. You want to address this issue in the most cost-effective way. What should you do?

    - ( ) A. Deploy small Kafka clusters in your data centers to buffer events.
    - (x) B. Have the data acquisition devices publish data to Cloud Pub/Sub.
    - ( ) C. Establish a Cloud Interconnect between all remote data centers and Google.
    - ( ) D. Write a Cloud Dataflow pipeline that aggregates all data in session windows.
    
8. You are deploying MariaDB SQL databases on GCE VM Instances and need to configure monitoring and alerting. You want to collect metrics including network connections, disk 10 and replication status from MariaDB with minimal development effort and use StackDriver for dashboards and alerts. What should you do?


    - ( ) A. Install the OpenCensus Agent and create a custom metric collection application with a StackDriver exporter.
    - ( ) B. Place the MariaDB instances in an Instance Group with a Health Check.
    - ( ) C. Install the StackDriver Logging Agent and configure fluentd in_tail plugin to read MariaDB logs.
    - (x) D. Install the StackDriver Agent and configure the MySQL plugin.
    
9. You have Cloud Functions written in Node.js that pull messages from Cloud Pub/Sub and send the data to BigQuery. You observe that the message processing rate on the Pub/Sub topic is orders of magnitude higher than anticipated, but there is no error logged in Cloud Logging. What are the two most likely causes of this problem?

    - [ ] A. Publisher throughput quota is too small.
    - [ ] B. Total outstanding messages exceed the 10-MB maximum.
    - [x] C. Error handling in the subscriber code is not handling run-time errors properly.
    - [ ] D. The subscriber code cannot keep up with the messages.
    - [x] E. The subscriber code does not acknowledge the messages that it pulls.
    
10. You have a data pipeline that writes data to Cloud Bigtable using well-designed row keys. You want to monitor your pipeline to determine when to increase the size of your Cloud Bigtable cluster. Which two actions can you take to accomplish this? (Choose two.)

    - [ ] A. Review Key Visualizer metrics. Increase the size of the Cloud Bigtable cluster when the Read pressure index is above 100.
    - [ ] B. Review Key Visualizer metrics. Increase the size of the Cloud Bigtable cluster when the Write pressure index is above 100.
    - [x] C. Monitor the latency of write operations. Increase the size of the Cloud Bigtable cluster when there is a sustained increase in write latency..
    - [x] D. Monitor storage utilization. Increase the size of the Cloud Bigtable cluster when utilization increases above 70% of max capacity.
    - [ ] E. Monitor latency of read operations. Increase the size of the Cloud Bigtable cluster of read operations take longer than 100 ms.
    
11. You work for a manufacturing company that sources up to 750 different components, each from a different supplier. You've collected a labeled dataset that has on average 1000 examples for each unique component. Your team wants to implement an app to help warehouse workers recognize incoming components based on a photo of the component. You want to implement the first working version of this app (as Proof-Of-Concept) within a few working days. What should you do?

    - (x) A. Use Cloud Vision AUtoML with the existing dataset.
    - ( ) B. Use Cloud Vision AutoML, but reduce your dataset twice.
    - ( ) C. Use Cloud Vision API by providing custom labels as recognition hints.
    - ( ) D. Train your own image recognition model leveraging transfer learning techniques.
    
12. You are operating a Cloud Dataflow streaming pipeline. The pipeline aggregates events from a Cloud Pub/Sub subscription source, within a window, and sinks the resulting aggregation to a Cloud Storage bucket. The source has consistent throughput. You want to monitor an alert on behavior of the pipeline with Cloud Stackdriver to ensure that it is processing data. Which Stackdriver alerts should you create?

    - ( ) A. An alert based on a decrease of subscription/num_undelivered_messages for the source and a rate of change increase of instance/storage/ used_bytes for the destination
    - (x) B. An alert based on an increase of subscription/num_undelivered_messages for the source and a rate of change decrease of instance/storage/ used_bytes for the destination
    - ( ) C. An alert based on a decrease of instance/storage/used_bytes for the source and a rate of change increase of subscription/ num_undelivered_messages for the destination
    - ( ) D. An alert based on an increase of instance/storage/used_bytes for the source and a rate of change decrease of subscription/ num_undelivered_messages for the destination
    
13. You are a retailer that wants to integrate your online sales capabilities with different in-home assistants, such as Google Home. You need to interpret customer voice commands and issue an order to the backend systems. Which solutions should you choose?

    - ( ) A. Speech-to-Text API
    - ( ) B. Cloud Natural Language API
    - (x) C. Dialogflow Enterprise Edition
    - ( ) D. AutoML Natural Language
    
14. You work for a bank. You have a labelled dataset that contains information on already granted loan application and whether these applications have been defaulted. You have been asked to train a model to predict default rates for credit applicants. What should you do?

    - ( ) A. Increase the size of the dataset by collecting additional data.
    - (x) B. Train a linear regression to predict a credit default risk score.
    - ( ) C. Remove the bias from the data and collect applications that have been declined loans.
    - ( ) D. Match loan applicants with their social profiles to enable feature engineering.
    
15. You operate a database that stores stock trades and an application that retrieves average stock price for a given company over an adjustable window of time. The data is stored in Cloud Bigtable where the datetime of the stock trade is the beginning of the row key. Your application has thousands of concurrent users, and you notice that performance is starting to degrade as more stocks are added. What should you do to improve the performance of your application?

    - (x) A. Change the row key syntax in your Cloud Bigtable table to begin with the stock symbol.
    - ( ) B. Change the row key syntax in your Cloud Bigtable table to begin with a random number per second.
    - ( ) C. Change the data pipeline to use BigQuery for storing stock trades, and update your application.
    - ( ) D. Use Cloud Dataflow to write a summary of each day's stock trades to an Avro file on Cloud Storage. Update your application to read from Cloud Storage and Cloud
Bigtable to compute the responses.
    
16. You need to create a near real-time inventory dashboard that reads the main inventory tables in your BigQuery data warehouse. Historical inventory data is stored as inventory balances by item and location. You have several thousand updates to inventory every hour. You want to maximize performance of the dashboard and ensure that the data is accurate. What should you do?

    - ( ) A. Leverage BigQuery UPDATE statements to update the inventory balances as they are changing.
    - ( ) B. Partition the inventory balance table by item to reduce the amount of data scanned with each inventory update.
    - (x) C. Use the BigQuery streaming the stream changes into a daily inventory movement table. Calculate balances in a view that joins it to the historical inventory balance table. Update the inventory balance table nightly.
    - ( ) D. Use the BigQuery bulk loader to batch load inventory changes into a daily inventory movement table. Calculate balances in a view that joins it to the historical
inventory balance table. Update the inventory balance table nightly.
    
17. You are designing a data processing pipeline. The pipeline must be able to scale automatically as load increases. Messages must be processed at least once and must be ordered within windows of 1 hour. How should you design the solution?
   
    - ( ) A. Use Apache Kafka for message ingestion and use Cloud Dataproc for streaming analysis.
    - ( ) B. Use Apache Kafka for message ingestion and use Cloud Dataflow for streaming analysis.
    - ( ) C. Use Cloud Pub/Sub for message ingestion and Cloud Dataproc for streaming analysis.
    - (x) D. Use Cloud Pub/Sub for message ingestion and Cloud Dataflow for streaming analysis.
    
18. You used Dataprep to create a recipe on a sample of data in a BigQuery table. You want to reuse this recipe on a daily upload of data with the same schema, after the load job with variable execution time completes. What should you do?

    - ( ) A. Create a cron schedule in Dataprep.
    - ( ) B. Create an App Engine cron job to schedule the execution of the Dataprep job.
    - ( ) C. Export the recipe as a Dataprep template, and create a job in Cloud Scheduler.
    - (x) D. Export the Dataprep job as a Dataflow template, and incorporate it into a Composer job.
    
19. You have developed three data processing jobs. One executes a Cloud Dataflow pipeline that transforms data uploaded to Cloud Storage and writes results to BigQuery. The second ingests data from on-premises servers and uploads it to Cloud Storage. The third is a Cloud Dataflow pipeline that gets information from third-party data providers and uploads the information to Cloud Storage. You need to be able to schedule and monitor the execution of these three workflows and manually execute them when needed. What should you do?

    - (x) A. Create a Direct Acyclic Graph in Cloud Composer to schedule and monitor the jobs.
    - ( ) B. Use Stackdriver Monitoring and set up an alert with a Webhook notification to trigger the jobs.
    - ( ) C. Develop an App Engine application to schedule and request the status of the jobs using GCP API calls.
    - ( ) D. Set up cron jobs in a Compute Engine instance to schedule and monitor the pipelines using GCP API calls.
    
20. You currently have a single on-premises Kafka cluster in a data center in the us-east region that is responsible for ingesting messages from loT devices globally. Because large parts of globe have poor internet connectivity, messages sometimes batch at the edge, come in all at once, and cause a spike in load on your Kafka cluster. This is becoming difficult to manage and prohibitively expensive. What is the Google-recommended cloud native architecture for this scenario?

    - ( ) A. Edge TPUs as sensor devices for storing and transmitting the messages.
    - ( ) B. Cloud Dataflow connected to the Kafka cluster to scale the processing of incoming messages.
    - (x) C. An loT gateway connected to Cloud Pub/Sub, with Cloud Dataflow to read and process the messages from Cloud Pub/Sub.
    - ( ) D. A Kafka cluster virtualized on Compute Engine in us-east with Cloud Load Balancing to connect to the devices around the world.

21. You have a petabyte of analytics data and need to design a storage and processing platform for it. You must be able to perform data warehouse-style analytics on the data in Google Cloud and expose the dataset as files for batch analysis tools in other cloud providers. What should you do?

    - ( ) A. Store and process the entire dataset in BigQuery.
    - ( ) B. Store and process the entire dataset in Bigtable.
    - (x) C. Store the full dataset in BigQuery, and store a compressed copy of the data in a Cloud Storage bucket.
    - ( ) D. Store the warm data as files in Cloud Storage, and store the active data in BigQuery. Keep this ratio as 80% warm and 20% active.

22. You want to analyze hundreds of thousands of social media posts daily at the lowest cost and with the fewest steps.
        * You have the following requirements:
        * You will batch-load the posts once per day and run them through the Cloud Natural Language API.
        * You will extract topics and sentiment from the posts.
        * You must store the raw posts for archiving and reprocessing.
        * You will create dashboards to be shared with people both inside and outside your organization.
        * You need to store both the data extracted from the API to perform analysis as well as the raw social media posts for historical archiving. What should you do?

    - ( ) A. Store the social media posts and the data extracted from the API in BigQuery.
    - ( ) B. Store the social media posts and the data extracted from the API in Cloud SQL.
    - (x) C. Store the raw social media posts in Cloud Storage, and write the data extracted from the API into BigQuery.
    - ( ) D. Feed to social media posts into the API directly from the source, and write the extracted data from the API into BigQuery.

23. Your United States-based company has created an application for assessing and responding to user actions. The primary table's data volume grows by 250,000 records
per second. Many third parties use your application's APIs to build the functionality into their own frontend applications. Your application's APIs should comply with the
following requirements:

* Single global endpoint

* ANSI SQL support

* Consistent access to the most up-to-date data What should you do?

    - ( ) A. Implement BigQuery with no region selected for storage or processing.
    - (x) B. Implement Cloud Spanner with the leader in North America and read-only replicas in Asia and Europe.
    - ( ) C. Implement Cloud SQL for PostgreSQL with the master in North America and read replicas in Asia and Europe.
    - ( ) D. Implement Bigtable with the primary cluster in North America and secondary clusters in Asia and Europe.

24. You are running a pipeline in Dataflow that receives messages from a Pub/Sub topic and writes the results to a BigQuery dataset in the EU. Currently, your pipeline is located in europe-west4 and has a maximum of 3 workers, instance type n1-standard-1. You notice that during peak periods, your pipeline is struggling to process records in a timely fashion, when all 3 workers are at maximum CPU utilization. Which two actions can you take to increase performance of your pipeline? (Choose two.)

    - [x] A. Increase the number of max workers
    - [x] B. Use a larger instance type for your Dataflow workers
    - [ ] C. Change the zone of your Dataflow pipeline to run in us-central1
    - [ ] D. Create a temporary table in Bigtable that will act as a buffer for new data. Create a new step in your pipeline to write to this table first, and then create a new pipeline to write from Bigtable to BigQuery
    - [ ] E. Create a temporary table in Cloud Spanner that will act as a buffer for new data. Create a new step in your pipeline to write to this table first, and then create a new pipeline to write from Cloud Spanner to BigQuery

25. You are working on a niche product in the image recognition domain. Your team has developed a model that is dominated by custom C++ TensorFlow ops your team has implemented. These ops are used inside your main training loop and are performing bulky matrix multiplications. It currently takes up to several days to train a model. You want to decrease this time significantly and keep the cost low by using an accelerator on Google Cloud. What should you do?

    - ( ) A. Use Cloud TPUs without any additional adjustment to your code.
    - ( ) B. Use Cloud TPUs after implementing GPU kernel support for your customs ops.
    - ( ) C. Use Cloud GPUs after implementing GPU kernel support for your customs ops.
    - ( ) D. Stay on CPUs, and increase the size of the cluster you're training your model on.

26. Your company needs to upload their historic data to Cloud Storage. The security rules don't allow access from external IPs to their on-premises resources. After an initial upload, they will add new data from existing on-premises applications every day. What should they do?

    - (x) A. Execute gsutil rsync from the on-premises servers.
    - ( ) B. Use Dataflow and write the data to Cloud Storage.
    - ( ) C. Write a job template in Dataproc to perform the data transfer.
    - ( ) D. Install an FTP server on a Compute Engine VM to receive the files and move them to Cloud Storage.

27. You need to create a data pipeline that copies time-series transaction data so that it can be queried from within BigQuery by your data science team for analysis. Every hour, thousands of transactions are updated with a new status. The size of the initial dataset is 1.5 PB, and it will grow by 3 TB per day. The data is heavily structured, and your data science team will build machine learning models based on this data. You want to maximize performance and usability for your data science team. Which two strategies should you adopt? (Choose two.)

    - [x] A. Denormalize the data as must as possible.
    - [ ] B. Preserve the structure of the data as much as possible.
    - [ ] C. Use BigQuery UPDATE to further reduce the size of the dataset.
    - [x] D. Develop a data pipeline where status updates are appended to BigQuery instead of updated.
    - [ ] E. Copy a daily snapshot of transaction data to Cloud Storage and store it as an Avro file. Use BigQuery's support for external data sources to query.
    - [ ]

28. You use BigQuery as your centralized analytics platform. New data is loaded every day, and an ETL pipeline modifies the original data and prepares it for the final users. This ETL pipeline is regularly modified and can generate errors, but sometimes the errors are detected only after 2 weeks. You need to provide a method to recover from these errors, and your backups should be optimized for storage costs. How should you organize your data in BigQuery and store your backups?

    - ( ) A. Organize your data in a single table, export, and compress and store the BigQuery data in Cloud Storage.
    - (x) B. Organize your data in separate tables for each month, and export, compress, and store the data in Cloud Storage.
    - ( ) C. Organize your data in separate tables for each month, and duplicate your data on a separate dataset in BigQuery.
    - ( ) D. Organize your data in separate tables for each month, and use snapshot decorators to restore the table to a time prior to the corruption.
    
29. You are managing a Cloud Dataproc cluster. You need to make a job run faster while minimizing costs, without losing work in progress on your clusters. What should you do?

    - ( ) A. Increase the cluster size with more non-preemptible workers.
    - ( ) B. Increase the cluster size with preemptible worker nodes, and configure them to forcefully decommission.
    - ( ) C. Increase the cluster size with preemptible worker nodes, and use Cloud Stackdriver to trigger a script to preserve work.
    - (x) D. Increase the cluster size with preemptible worker nodes, and configure them to use graceful decommissioning.

30. You're using Bigtable for a real-time application, and you have a heavy load that is a mix of read and writes. You've recently identified an additional use case and need to perform hourly an analytical job to calculate certain statistics across the whole database. You need to ensure both the reliability of your production application as well as the analytical workload. What should you do?

    - ( ) A. Export Bigtable dump to GCS and run your analytical job on top of the exported files.
    - ( ) B. Add a second cluster to an existing instance with a multi-cluster routing, use live-traffic app profile for your regular workload and batch-analytics profile for the analytics workload.
    - (x) C. Add a second cluster to an existing instance with a single-cluster routing, use live-traffic app profile for your regular workload and batch-analytics profile for the analytics workload.
    - ( ) D. Increase the size of your existing cluster twice and execute your analytics workload on your new resized cluster.

31. You want to automate execution of a multi-step data pipeline running on Google Cloud. The pipeline includes Dataproc and Dataflow jobs that have multiple dependencies
on each other. You want to use managed services where possible, and the pipeline will run every day. Which tool should you use?

    - ( ) A. cron
    - (x) B. Cloud Composer
    - ( ) C. Cloud Scheduler
    - ( ) D. Workflow Templates on Dataproc

32. You decided to use Cloud Datastore to ingest vehicle telemetry data in real time. You want to build a storage system that will account for the long-term data growth, while keeping the costs low. You also want to create snapshots of the data periodically, so that you can make a point-in-time (PIT) recovery, or clone a copy of the data for Cloud Datastore in a different environment. You want to archive these snapshots for a long time. Which two methods can accomplish this? (Choose two.)

    - (x) A. Use managed export, and store the data in a Cloud Storage bucket using Nearline or Coldline class.
    - (x) B. Use managed export, and then import to Cloud Datastore in a separate project under a unique namespace reserved for that export.
    - ( ) C. Use managed export, and then import the data into a BigQuery table created just for that export, and delete temporary export files.
    - ( ) D. Write an application that uses Cloud Datastore client libraries to read all the entities. Treat each entity as a BigQuery table row via BigQuery streaming insert.
    - ( ) E. Write an application that uses Cloud Datastore client libraries to read all the entities. Format the exported data into a JSON file. Apply compression before storing the data in Cloud Source Repositories.
    
33. You work on a regression problem in a natural language processing domain, and you have 100M labeled examples in your dataset. You have randomly shuffled your data and split your dataset into train and test samples (in a 90/10 ratio). After you trained the neural network and evaluated your model on a test set, you discover that the root-mean-squared error (RMSE) of your model is twice as high on the train set as on the test set. How should you improve the performance of your model?

    - ( ) A. Increase the share of the test sample in the train-test split.
    - ( ) B. Try to collect more data and increase the size of your dataset.
    - ( ) C. Try out regularization techniques (e.g., dropout of batch normalization) to avoid overfitting.
    - (x) D. Increase the complexity of your model by, e.g., introducing an additional layer or increase sizing the size of vocabularies or n-grams used.
34. You are designing a cloud-native historical data processing system to meet the following conditions:
            The data being analyzed is in CSV, Avro, and PDF formats and will be accessed by multiple analysis tools
            including Dataproc, BigQuery, and Compute
            Engine.
            A batch pipeline moves daily data.
            Performance is not a factor in the solution.

    - ( ) A. Create a Dataproc cluster with high availability. Store the data in HDFS, and perform analysis as needed.
    - ( ) B. Store the data in BigQuery. Access the data using the BigQuery Connector on Dataproc and Compute Engine.
    - ( ) C. Store the data in a regional Cloud Storage bucket. Access the bucket directly using Dataproc, BigQuery, and Compute Engine.
    - (x) D. Store the data in a multi-regional Cloud Storage bucket. Access the data directly using Dataproc, BigQuery, and Compute Engine

35.  You are building an application to share financial market data with consumers, who will receive data feeds. Data is collected from the markets in real time.
        Consumers will receive the data in the following ways:
        Real-time event stream
        ANSI SQL access to real-time stream and historical data
        Batch historical exports
        Which solution should you use?

    - ( ) A. Cloud Dataflow, Cloud SQL, Cloud Spanner
    - (x) B. Cloud Pub/Sub, Cloud Storage, BigQuery
    - ( ) C. Cloud Dataproc, Cloud Dataflow, BigQuery
    - ( ) D. Cloud Pub/Sub, Cloud Dataproc, Cloud SQL    

36. You are designing a cloud-native historical data processing system to meet the following conditions:
            The data being analyzed is in CSV, Avro, and PDF formats and will be accessed by multiple analysis tools
            including Dataproc, BigQuery, and Compute
            Engine.

            A batch pipeline moves daily data.

            Performance is not a factor in the solution.

            The solution design should maximize availability.
            How should you design data storage for this solution?

    - ( ) A. Create a Dataproc cluster with high availability. Store the data in HDFS, and perform analysis as needed.
    - ( ) B. Store the data in BigQuery. Access the data using the BigQuery Connector on Dataproc and Compute Engine.
    - ( ) C. Store the data in a regional Cloud Storage bucket. Access the bucket directly using Dataproc, BigQuery, and Compute Engine.
    - (x) D. Store the data in a multi-regional Cloud Storage bucket. Access the data directly using Dataproc, BigQuery, and Compute Engine
    
37. You are building an application to share financial market data with consumers, who will receive data feeds. Data is collected from the markets in real time.

        Consumers will receive the data in the following ways:

        Real-time event stream

        ANSI SQL access to real-time stream and historical data

        Batch historical exports

        Which solution should you use?

    - ( ) A. Cloud Dataflow, Cloud SQL, Cloud Spanner
    - (x) B. Cloud Pub/Sub, Cloud Storage, BigQuery 
    - ( ) C. Cloud Dataproc, Cloud Dataflow, BigQuery
    - ( ) D. Cloud Pub/Sub, Cloud Dataproc, Cloud SQL

38.  You have historical data covering the last three years in BigQuery and a data pipeline that delivers new data to BigQuery daily. You have noticed that when the Data Science team runs a query filtered on a date column and limited to 30 to 90 days of data, the query scans the entire table. You also noticed that your bill is increasing more quickly than you expected. You want to resolve the issue as cost-effectively as possible while maintaining the ability to conduct SQL queries. What should you do?

    - (x) A. Re-create the tables using DDL. Partition the tables by a column containing a TIMESTAMP or DATE Type.
    - ( ) B. Recommend that the Data Science team export the table to a CSV file on Cloud Storage and use Cloud Datalab to explore the data by reading the files directly.
    - ( ) C. Modify your pipeline to maintain the last 3090"€a days of data in one table and the longer history in a different table to minimize full table scans over the entire history.
    - ( ) D. Write an Apache Beam pipeline that creates a BigQuery table per day. Recommend that the Data Science team use wildcards on the table name suffixes to select
the data they need.

39. You have a requirement to insert minute-resolution data from 50,000 sensors into a BigQuery table. You expect significant growth in data volume and need the data to be available within 1 minute of ingestion for real-time analysis of aggregated trends. What should you do?

    - ( ) A. Use bq load to load a batch of sensor data every 60 seconds.
    - (x) B. Use a Cloud Dataflow pipeline to stream data into the BigQuery table.
    - ( ) C. Use the INSERT statement to insert a batch of data every 60 seconds.
    - ( ) D. Use the MERGE statement to apply updates in batch every 60 seconds.

40. A data scientist has created a BigQuery ML model and asks you to create an ML pipeline to serve predictions. You have a REST API application with the requirement to serve predictions for an individual user ID with latency under 100 milliseconds. You use the following query to generate predictions: SELECT predicted_label, user_id FROM M1L.PREDICT (MODEL ‘dataset.model', table user_features). How should you create the ML pipeline?

    - ( ) A. Add a WHERE clause to the query, and grant the BigQuery Data Viewer role to the application service account.
    - ( ) B. Create an Authorized View with the provided query. Share the dataset that contains the view with the application service account.
    - ( ) C. Create a Dataflow pipeline using BigQuerylO to read results from the query. Grant the Dataflow Worker role to the application service account.
    - (x) D. Create a Dataflow pipeline using BigQuerylO to read predictions for all users from the query. Write the results to Bigtable using BigtablelO. Grant the Bigtable Reader role to the application service account so that the application can read predictions for individual users from Bigtable.
    
41. You are building a new data pipeline to share data between two different types of applications: jobs generators and job runners. Your solution must scale to accommodate increases in usage and must accommodate the addition of new applications without negatively affecting the performance of existing ones. What should you do?

    - ( ) A. Create an API using App Engine to receive and send messages to the applications
    - (x) B. Use a Cloud Pub/Sub topic to publish jobs, and use subscriptions to execute them  
    - ( ) C. Create a table on Cloud SQL, and insert and delete rows with the job information
    - ( ) D. Create a table on Cloud Spanner, and insert and delete rows with the job information

42. You are building a new application that you need to collect data from in a scalable way. Data arrives continuously from the application throughout the day, and you expect to generate approximately 150 GB of JSON data per day by the end of the year. Your requirements are:

        Decoupling producer from consumer

        Space and cost-efficient storage of the raw ingested data, which is to be stored indefinitely

        Near real-time SQL query

        Maintain at least 2 years of historical data, which will be queried with SQL
        Which pipeline should you use to meet these requirements?



    - ( ) A. Create an application that provides an API. Write a tool to poll the API and write data to Cloud Storage as gzipped JSON files.
    - ( ) B. Create an application that writes to a Cloud SQL database to store the data. Set up periodic exports of the database to write to Cloud Storage and load into BigQuery.
    - ( ) C. Create an application that publishes events to Cloud Pub/Sub, and create Spark jobs on Cloud Dataproc to convert the JSON data to Avro format, stored on HDFS on Persistent Disk.
    - (x) D. Create an application that publishes events to Cloud Pub/Sub, and create a Cloud Dataflow pipeline that transforms the JSON event payloads to Avro, writing the data to Cloud Storage and BigQuery.

43. You have a query that filters a BigQuery table using a WHERE clause on timestamp and ID columns. By using bq query *"-dry_run you learn that the query triggers a full scan of the table, even though the filter on timestamp and ID select a tiny fraction of the overall data. You want to reduce the amount of data scanned by BigQuery with minimal changes to existing SQL queries. What should you do?
    - ( ) A. Create a separate table for each ID.
    - ( ) B. Use the LIMIT keyword to reduce the number of rows returned.
    - (x) C. Recreate the table with a partitioning column and clustering column.
    - ( ) D. Use the bq query -maximum_bytes_billed flag to restrict the number of bytes billed.

44. You store historic data in Cloud Storage. You need to perform analytics on the historic data. You want to use a solution to detect invalid data entries and perform data
transformations that will not require programming or knowledge of SQL.
What should you do?

    - ( ) A. Use Cloud Dataflow with Beam to detect errors and perform transformations.
    - (x) B. Use Cloud Dataprep with recipes to detect errors and perform transformations.
    - ( ) C. Use Cloud Dataproc with a Hadoop job to detect errors and perform transformations.
    - ( ) D. Use federated tables in BigQuery with queries to detect errors and perform transformations.
    
45. You need to copy millions of sensitive patient records from a relational database to BigQuery. The total size of the database is 10 TB. You need to design a solution that is secure and time-efficient. What should you do?

    - ( ) A. Export the records from the database as an Avro file. Upload the file to GCS using gsutil, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.
    - (x) B. Export the records from the database as an Avro file. Copy the file onto a Transfer Appliance and send it to Google, and then load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.
    - ( ) C. Export the records from the database into a CSV file. Create a public URL for the CSV file, and then use Storage Transfer Service to move the file to Cloud Storage. Load the CSV file into BigQuery using the BigQuery web UI in the GCP Console.
    - ( ) D. Export the records from the database as an Avro file. Create a public URL for the Avro file, and then use Storage Transfer Service to move the file to Cloud Storage. Load the Avro file into BigQuery using the BigQuery web UI in the GCP Console.


46.  You need to migrate a 2TB relational database to Google Cloud Platform. You do not have the resources to significantly refactor the application that uses this database and cost to operate is of primary concern. Which service do you select for storing and serving your data?

    - ( ) A. Cloud Spanner
    - ( ) B. Cloud Bigtable
    - ( ) C. Cloud Firestore
    - (x) D. Cloud SQL

47. You are creating a new pipeline in Google Cloud to stream loT data from Cloud Pub/Sub through Cloud Dataflow to BigQuery. While previewing the data, you notice that roughly 2% of the data appears to be corrupt. You need to modify the Cloud Dataflow pipeline to filter out this corrupt data. What should you do?

    - ( ) A. Add a Sidelnput that returns a Boolean if the element is corrupt.
    - (x) B. Add a ParDo transform in Cloud Dataflow to discard corrupt elements.
    - ( ) C. Add a Partition transform in Cloud Dataflow to separate valid data from corrupt data.
    - ( ) D. Add a GroupByKey transform in Cloud Dataflow to group all of the valid data together and discard the rest.

48. You are designing an Apache Beam pipeline to enrich data from Cloud Pub/Sub with static reference data from BigQuery. The reference data is small enough to fit in memory on a single worker. The pipeline should write enriched results to BigQuery for analysis. Which job type and transforms should this pipeline use?

    - ( ) A. Batch job, PubSublO, side-inputs
    - ( ) B. Streaming job, PubSublO, JdbclO, side-outputs
    - (x) C. Streaming job, PubSublO, BigQueryl0, side-inputs
    - ( ) D. Streaming job, PubSublO, BigQuerylO, side-outputs
    
49. Your company is in the process of migrating its on-premises data warehousing solutions to BigQuery. The existing data warehouse uses trigger-based change data capture (CDC) to apply updates from multiple transactional database sources on a daily basis. With BigQuery, your company hopes to improve its handling of CDC so that changes to the source systems are available to query in BigQuery in near-real time using log-based CDC streams, while also optimizing for the performance of applying changes to the data warehouse. Which two steps should they take to ensure that changes are available in the BigQuery reporting table with minimal latency while reducing compute overhead? (Choose two.)

    - [ ] A. Perform a DML INSERT, UPDATE, or DELETE to replicate each individual CDC record in real time directly on the reporting table.
    - [x] B. Insert each new CDC record and corresponding operation type to a'staging table in real time.
    - [ ] C. Periodically DELETE outdated records from the reporting table.
    - [x] D: Periodically use a DML MERGE to perform several DML INSERT, UPDATE, and DELETE operations at the same time on the reporting table.
    - [ ] E. Insert each new CDC record and corresponding operation type in real time to the reporting table, and use a materialized view to expose only the newest version of each unique record.

50. Your company is in the process of migrating its on-premises data warehousing solutions to BigQuery. The existing data warehouse uses trigger-based change data capture (CDC) to apply updates from multiple transactional database sources on a daily basis. With BigQuery, your company hopes to improve its handling of CDC so that changes to the source systems are available to query in BigQuery in near-real time using log-based CDC streams, while also optimizing for the performance of applying changes to the data warehouse. Which two steps should they take to ensure that changes are available in the BigQuery reporting table with minimal latency while reducing compute overhead? (Choose two.)

    - [ ] A. Perform a DML INSERT, UPDATE, or DELETE to replicate each individual CDC record in real time directly on the reporting table. 
    - [x] B. Insert each new CDC record and corresponding operation type to a'staging table in real time.
    - [ ] C. Periodically DELETE outdated records from the reporting table.
    - [x] D: Periodically use a DML MERGE to perform several DML INSERT, UPDATE, and DELETE operations at the same time on the reporting table.
    - [ ] E. Insert each new CDC record and corresponding operation type in real time to the reporting table, and use a materialized view to expose only the newest version of
each unique record.

51. The marketing team at your organization provides regular updates of a segment of your customer dataset. The marketing team has given you a CSV with 1 million records that must be updated in BigQuery. When you use the UPDATE statement in BigQuery, you receive a quotaExceeded error. What should you do?

    - ( ) A. Reduce the number of records updated each day to stay within the BigQuery UPDATE DML statement limit.
    - ( ) B. Increase the BigQuery UPDATE DML statement limit in the Quota management section of the Google Cloud Platform Console.
    - (x) C. Split the source CSV file into smaller CSV files in Cloud Storage to reduce the number of BigQuery UPDATE DML statements per BigQuery job.
    - ( ) D. Import the new records from the CSV file into a new BigQuery table. Create a BigQuery job that merges the new records with the existing records and writes the
results to a new BigQuery table.
