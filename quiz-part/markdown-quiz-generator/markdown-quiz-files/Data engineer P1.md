# GCP Data engineer test

---

1. You have an Apache Kafka cluster on-prem with topics containing web application logs. You need to replicate the data to Google Cloud for analysis in BigQuery and Cloud Storage. The preferred replication method is mirroring to avoid deployment of Kafka Connect plugins. What should you do?
    - (x)  A. Deploy a Kafka cluster on GCE VM Instances. Configure your on-prem cluster to mirror your topics to the cluster running in GCE. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.
    - ( ) B. Deploy a Kafka cluster on GCE VM Instances with the Pub/Sub Kafka connector configured as a Sink connector. Use a Dataproc cluster or Dataflow job to read from Kafka and write to GCS.
    - ( ) C. Deploy the Pub/Sub Kafka connector to your on-prem Kafka cluster and configure Pub/Sub as a Source connector. Use a Dataflow job to read from Pub/Sub and write to GCS.
    - ( ) D. Deploy the Pub/Sub Kafka connector to your on-prem Kafka cluster and configure Pub/Sub as a Sink connector. Use a Dataflow job to read from Pub/Sub and write to GCS.

2. CFO Statement - The project is too large for us to maintain the hardware and software required for the data and analysis. Also, we cannot afford to staff an operations team to monitor so many data feeds, so we will rely on automation and infrastructure. Google Cloud's machine learning will allow our quantitative researchers to work on our high-value problems instead of problems with our data pipelines. 
    MJTelco is building a custom interface to share data. They have these requirements:

        1. They need to do aggregations over their petabyte-scale datasets.
        2. They need to scan specific time range rows with a very fast response time (milliseconds).
        Which combination of Google Cloud Platform products should you recommend?
        
    - ( ) A. Cloud Datastore and Cloud Bigtable
    - ( ) B. Cloud Bigtable and Cloud SQL
    - (x)C. BigQuery and Cloud Bigtable
    - ( )D. BigQuery and Cloud Storage
   

3. Your company is currently setting up data pipelines for their campaign. For all the Google Cloud Pub/Sub streaming data, one of the important business requirements is to be able to periodically identify the inputs and their timings during their campaign. Engineers have decided to use windowing and transformation in Google Cloud Dataflow for this purpose. However, when testing this feature, they find that the Cloud Dataflow job fails for the all streaming insert. What is the most likely cause of this problem?
    - ( ) A. They have not assigned the timestamp, which causes the job to fail
    - ( ) B. They have not set the triggers to accommodate the data coming in late, which causes the job to fail
    - ( ) C. They have not applied a global windowing function, which causes the job to fail when the pipeline is created
	- (x) D. They have not applied a non-global windowing function, which causes the job to fail when the pipeline is created

4. You are using Google BigQuery as your data warehouse. Your users report that the following simple query is running very slowly, no matter when they run the query: SELECT country, state, city FROM [myproject:mydataset.mytable] GROUP BY country. You check the query plan for the query and see the following output in the Read section of Stage:1: What is the most likely cause of the delay for this query?

    - ( ) A. Users are running too many concurrent queries in the system
    - ( ) B. The [myproject:mydataset.mytable] table has too many partitions
    - ( ) C. Either the state or the city columns in the [myproject:mydataset.mytable] table have too many NULL values
    - (x) D. Most rows in the [myproject:mydataset.mytable] table have the same value in the country column, causing data skew



5. An online retailer has built their current application on Google App Engine. A new initiative at the company mandates that they extend their application to allow their customers to transact directly via the application. They need to manage their shopping transactions and analyze combined data from multiple datasets using a business intelligence (BI) tool. They want to use only a single database for this purpose. Which Google Cloud database should they choose?
    - ( ) A. BigQuery
    - (x) B. Cloud SQL
    - ( ) C. Cloud BigTable
	- ( ) D. Cloud Datastore
    

6. You are preparing an organization-wide dataset. You need to preprocess customer data stored in a restricted bucket in Cloud Storage. The data will be used to create consumer analyses. You need to comply with data privacy requirements. What should you do?
    - (x) A. Use Dataflow and the Cloud Data Loss Prevention API to mask sensitive data. Write the processed data in BigQuery.
    - ( ) B. Use customer-managed encryption keys (CMEK) to directly encrypt the data in Cloud Storage. Use federated queries from BigQuery. Share the encryption key by following the principle of least privilege.
    - ( ) C. Use the Cloud Data Loss Prevention API and Dataflow to detect and remove sensitive fields from the data in Cloud Storage. Write the filtered data in BigQuery.
    - ( ) D. Use Dataflow and Cloud KMS to encrypt sensitive fields and write the encrypted data in BigQuery. Share the encryption key by following the principle of least
privilege.

7. You are implementing security best practices on your data pipeline. Currently, you are manually executing jobs as the Project Owner. You want to automate these jobs by taking nightly batch files containing non-public information from Google Cloud Storage, processing them with a Spark Scala job on a Google Cloud Dataproc cluster, and depositing the results into Google BigQuery. How should you securely run this workload?
    - ( ) A. Restrict the Google Cloud Storage bucket so only you can see the files
    - ( ) B. Grant the Project Owner role to a service account, and run the job with it
    - (x) C. Use a service account with the ability to read the batch files and to write to BigQuery
    - ( ) D. Use a user account with the Project Viewer role on the Cloud Dataproc cluster to read the batch files and write to BigQuery

8. Your globally distributed auction application allows users to bid on items. Occasionally, users place identical bids at nearly identical times, and different application servers process those bids. Each bid event contains the item, amount, user, and timestamp. You want to collate those bid events into a single location in real time to determine which user bid first. What should you do?

    - ( ) A. Create a file on a shared file and have the application servers write all bid events to that file. Process the file with Apache Hadoop to identify which user bid first.
    - (x) B. Have each application server write the bid events to Cloud Pub/Sub as they occur. Push the events from Cloud Pub/Sub to a custom endpoint that writes the bid event information into Cloud SQL.
    - ( ) C. Set up a MySQL database for each application server to write bid events into.Periodically query each of those distributed MySQL databases and update a master MySQL database with bid event information.
    - ( )  Have each application server write the bid events to Google Cloud Pub/Sub as they occur. Use a pull subscription to pull the bid events using Google Cloud Dataflow. Give the bid for each item to the user in the bid event that is processed first.

9. You architect a system to analyze seismic data. Your extract, transform, and load (ETL) process runs as a series of MapReduce jobs on an Apache Hadoop cluster. The ETL process takes days to process a data set because some steps are computationally expensive. Then you discover that a sensor calibration step has been omitted. How should you change your ETL process to carry out sensor calibration systematically in the future?
    - ( ) A. Modify the transformMapReduce jobs to apply sensor calibration before they do anything else.
    - (x) B. Introduce a new MapReduce job to apply sensor calibration to raw data, and ensure all other MapReduce jobs are chained after this.
    - ( ) C. Add sensor calibration data to the output of the ETL process, and document that all users need to apply sensor calibration themselves.
    - ( ) D. Develop an algorithm through simulation to predict variance of data output from the last MapReduce job based on calibration factors, and apply the correction to
all data.


10. You need to connect multiple applications with dynamic public IP addresses to a Cloud SQL instance. You configured users with strong passwords and enforced the SSL connection to your Cloud SQL instance. You want to use Cloud SQL public IP and ensure that you have secured connections. What should you do?

    - ( ) A. Add CIDR 0.0.0.0/0 network to Authorized Network. Use Identity and Access Management (IAM) to add users.
    - ( ) B. Add all application networks to Authorized Network and regularly update them.
    - (x) C. Leave the Authorized Network empty. Use Cloud SQL Auth proxy on all applications.
    - ( ) D. Add CIDR 0.0.0.0/0 network to Authorized Network. Use Cloud SQL Auth proxy on all applications

11. CFO Statement:The project is too large for us to maintain the hardware and software required for the data and analysis. Also, we cannot afford to staff an operations team to monitor so many data feeds, so we will rely on automation and infrastructure. Google Cloud's machine learning will allow our quantitative researchers to work on our high-value problems instead of problems with our data pipelines. You need to compose visualization for operations teams with the following requirements:
    1.-  Telemetry must include data from all 50,000 installations for the most recent 6 weeks (sampling once every minute)
    2.- The report must not be more than 3 hours delayed from live data.
    3.- The actionable report should only show suboptimal links.

    Most suboptimal links should be sorted to the top.
    Suboptimal links can be grouped and filtered by regional geography.
    User response time to load the report must be <5 seconds. You create a data source to store the last 6 weeks of data, and create visualizations that allow viewers to see multiple date ranges, distinct geographic regions, and unique installation types. You always show the latest data without any changes to your visualizations. 
    You want to avoid creating and updating new visualizations each month. What should you do?

    - ( ) A. Look through the current data and compose a series of charts and tables, one for each possible combination of criteria.
    - ( ) B. Look through the current data and compose a small set of generalized charts and tables bound to criteria filters that allow value selection.
    - ( ) C. Export the data to a spreadsheet, compose a series of charts and tables, one for each possible combination of criteria, and spread them across multiple tabs.
    - (x) D. Load the data into relational database tables, write a Google App Engine application that queries all rows, summarizes the data across each criteria, and then
renders results using the Google Charts and visualization API.

12. You are a head of BI at a large enterprise company with multiple business units that each have different priorities and budgets. You use on-demand pricing for BigQuery with a quota of 2K concurrent on-demand slots per project. Users at your organization sometimes don't get slots to execute their query and you need to correct this. You'd like to avoid introducing new projects to your account. What should you do?
    - ( ) A. Convert your batch BQ queries into interactive BQ queries.
    - ( ) B. Create an additional project to overcome the 2K on-demand per-project quota.
    - ( ) C. Switch to flat-rate pricing and establish a hierarchical priority model for your projects.
    - (x) D. Increase the amount of concurrent slots per project at the Quotas page at the Cloud Console.

13. You work for an airline and you need to store weather data in a BigQuery table. Weather data will be used as input to a machine learning model. The model only uses the last 30 days of weather data. You want to avoid storing unnecessary data and minimize costs. What should you do?
    - ( ) A. Create a BigQuery table where each record has an ingestion timestamp. Run a scheduled query to delete all the rows with an ingestion timestamp older than 30 days.
    - (x) B. Create a BigQuery table partitioned by datetime value of the weather date. Set up partition expiration to 30 days.
    - ( ) C. Create a BigQuery table partitioned by ingestion time. Set up partition expiration to 30 days.
    - ( ) D. Create a BigQuery table with a datetime column for the day the weather data refers to. Run a scheduled query to delete rows with a datetime value older than 30
days.
   

14. You are integrating one of your internal IT applications and Google BigQuery, so users can query BigQuery from the application's interface. You do not want individual users to authenticate to BigQuery and you do not want to give them access to the dataset. You need to securely access BigQuery from your IT application. What should you do?
    - ( ) A. Create groups for your users and give those groups access to the dataset
    - ( ) B. Integrate with a single sign-on (SSO) platform, and pass each user's credentials along with the query request
    - (x) C. Create a service account and grant dataset access to that account. Use the service account's private key to access the dataset
    - ( ) D. Create a dummy user and grant dataset access to that user. Store the username and password for that user in a file on the files system, and use those credentials
to access the BigQuery dataset

15. You have enabled the free integration between Firebase Analytics and Google BigQuery. Firebase now automatically creates a new table daily in BigQuery in the format
app_events_YYYYMMDD. You want to query all of the tables for the past 30 days in legacy SQL. What should you do?
    - (x) A. Use the TABLE_DATE_RANGE function
    - ( ) B. Use the WHERE_PARTITIONTIME pseudo column
    - ( ) C. Use WHERE date BETWEEN YYYY-MM-DD AND YYYY-MM-DD
    - ( ) D. Use SELECT IF.(date >= YYYY-MM-DD AND date <= YYYY-MM-DD)

16. You have a table that contains millions of rows of sales data, partitioned by date. Various applications and users query this data many times a minute. The query requires aggregating values by using AVG, MAX, and SUM, and does not require joining to other tables. The required aggregations are only computed over the past year of data, though you need to retain full historical data in the base tables. You want to ensure that the query results always include the latest data from the tables, while also reducing computation cost, maintenance overhead, and duration. What should you do?
    - ( ) A. Create a materialized view to aggregate the base table data. Include a filter clause to specify the last one year of partitions.
    - (x) B. Create a materialized view to aggregate the base table data. Configure a partition expiration on the base table to retain only the last one year of partitions.
    - ( ) C. Create a view to aggregate the base table data. Include a filter clause to specify the last year of partitions.
    - ( ) D. Create a new table that aggregates the base table data. Include a filter clause to specify the last year of partitions. Set up a scheduled query to recreate the new
table every hour.

17. You launched a new gaming app almost three years ago. You have been uploading log files from the previous day to a separate Google BigQuery table with the table name
format LOGS_yyyymmdd. You have been using table wildcard functions to generate daily and monthly reports for all time ranges. Recently, you discovered that some
queries that cover long date ranges are exceeding the limit of 1,000 tables and failing. How can you resolve this issue?
    - () A. Convert all daily log tables into date-partitioned tables
    - (x) B. Convert the sharded tables into a single partitioned table
    - ( ) C. Enable query caching so you can cache data from previous months
    - ( ) D. Create separate views to cover each month, and query from these views

18. Your chemical company needs to manually check documentation for customer order. You use a pull subscription in Pub/Sub so that sales agents get details from the order. You must ensure that you do not process orders twice with different sales agents and that you do not add more complexity to this workflow. What should you do?
    - ( )A. Use a Deduplicate PTransform in Dataflow before sending the messages to the sales agents.
    - ( )B. Create a transactional database that monitors the pending messages.
    - (x)C. Use Pub/Sub exactly-once delivery in your pull subscription.
    - ( )D. Create a new Pub/Sub push subscription to monitor the orders processed in the agent's system.


19. You've migrated a Hadoop job from an on-prem cluster to dataproc and GCS. Your Spark job is a complicated analytical workload that consists of many shuffling operations and initial data are parquet files (on average 200-400 MB size each). You see some degradation in performance after the migration to Dataproc, so you'd like to optimize for it. You need to keep in mind that your organization is very cost-sensitive, so you'd like to continue using Dataproc on preemptibles (with 2 non-preemptible workers only) for this workload.
    - (x) A. Increase the size of your parquet files to ensure them to be 1 GB minimum
    - ( ) B. Switch to TFRecords formats (appr. 200MB per file) instead of parquet files.
    - ( )C. Switch from HDDs to SSDs, copy initial data from GCS to HDFS, run the Spark job and copy results back to GCS.
    - ( )D. Switch from HDDs to SSDs, override the preemptible VMs configuration to increase the boot disk size.

20. You're training a model to predict housing prices based on an available dataset with real estate properties. Your plan is to train a fully connected neural net, and you've discovered that the dataset contains latitude and longitude of the property. Real estate professionals have told you that the location of the property is highly influential on price, so you'd like to engineer a feature that incorporates this physical dependency. What should you do?
    - ( ) A. Provide latitude and longitude as input vectors to your neural net.
    - ( ) B. Create a numeric column from a feature cross of latitude and longitude.
    - ( ) C. Create a feature cross of latitude and longitude, bucketize it at the minute level and use L1 regularization during optimization.
    - (x) D. Create a feature cross of latitude and longitude, bucketize it at the minute level and use L2 regularization during optimization.


21. CFO Statement Part of our competitive advantage is that we penalize ourselves for late shipments and deliveries. Knowing where out shipments are at all times has a direct correlation to our bottom line and profitability. Additionally, | don't want to commit capital to building out a server environment. Flowlogistic's management has determined that the current Apache Kafka servers cannot handle the data volume for their real-time inventory tracking system.You need to build a new system on Google Cloud Platform (GCP) that will feed the proprietary tracking software. The system must be able to ingest data from a variety of global sources, process and query in real-time, and store the data reliably. Which combination of GCP products should you choose?
    - (x) A. Cloud Pub/Sub, Cloud Dataflow, and Cloud Storage
    - ( ) B. Cloud Pub/Sub, Cloud Dataflow, and Local SSD
    - ( ) C. Cloud Pub/Sub, Cloud SQL, and Cloud Storage
    - ( ) D. Cloud Load Balancing, Cloud Dataflow, and Cloud Storage
    - ( ) E. Cloud Dataflow, Cloud SQL, and Cloud Storage

6. CFO Statement The project is too large for us to maintain the hardware and software required for the data and analysis. Also, we cannot afford to staff an operations team to monitor so many data feeds, so we will rely on automation and infrastructure. Google Cloud's machine learning will allow our quantitative researchers to work on our high-value problems instead of problems with our data pipelines. Given the record streams MJTelco is interested in ingesting per day, they are concerned about the cost of Google BigQuery increasing. MJTelco asks you to provide a design solution. They require a single large data table called tracking_table. Additionally, they want to minimize the cost of daily queries while performing fine-grained analysis of each day's events. They also want to use streaming ingestion. What should you do?

    - ( )A. Create a table called tracking_table and include a DATE column.
    - (x)B. Create a partitioned table called tracking_table and include a TIMESTAMP column.
    - ( )C. Create sharded tables for each day following the pattern tracking_table_ YYYYMMDD.
    - ( )D. Create a table called tracking_table with a TIMESTAMP column to represent the day.

6. Your team is responsible for developing and maintaining ETLs in your company. One of your Dataflow jobs is failing because of some errors in the input data, and you need to improve reliability of the pipeline (incl. being able to reprocess all failing data). What should you do?
    - ( )A. Add a filtering step to skip these types of errors in the future, extract erroneous rows from logs.
    - ( )B. Add a try/catch block to your DoFn that transforms the data, extract erroneous rows from logs.
    - ( )C. Add a try/catch block to your DoFn that transforms the data, write erroneous rows to Pub/Sub PubSub directly from the DoFn.
    - (x)D. Add a trya/catch block to your DoFn that transforms the data, use a sideOutput to create a PCollection that can be stored to Pub/Sub later.

6.  After migrating ETL jobs to run on BigQuery, you need to verify that the output of the migrated jobs is the same as the output of the original. You've loaded a table containing the output of the original job and want to compare the contents with output from the migrated job to show that they are identical. The tables do not contain a primary key column that would enable you to join them together for comparison. What should you do?

    - ( )A. Select random samples from the tables using the RAND() function and compare the samples.
    - ( )B. Select random samples from the tables using the HASH() function and compare the samples.
    - (x)C. Use a Dataproc cluster and the BigQuery Hadoop connector to read the data from each table and calculate a hash from non-timestamp columns of the table after sorting. Compare the hashes of each table.
    - ( )D. Create stratified random samples using the OVER() function and compare equivalent samples from each table.

6. You need to look at BigQuery data from a specific table multiple times a day. The underlying table you are querying is several petabytes in size, but you want to filter your
data and provide simple aggregations to downstream users. You want to run queries faster and get up-to-date insights quicker. What should you do?
    - ( ) A. Run a scheduled query to pull the necessary data at specific intervals dally.
    - ( ) B. Use a cached query to accelerate time to results.
    - ( ) C. Limit the query columns being pulled in the final result.
    - (x) D. Create a materialized view based off of the query being run.

6. You are migrating a large number of files from a public HTTPS endpoint to Cloud Storage. The files are protected from unauthorized access using signed URLs. You created a TSV file that contains the list of object URLs and started a transfer job by using Storage Transfer Service. You notice that the job has run for a long time and eventually failed. Checking the logs of the transfer job reveals that the job was running fine until one point, and then it failed due to HTTP 403 errors on the remaining files. You verified that there were no changes to the source system. You need to fix the problem to resume the migration process. What should you do?
    - ( ) A. Set up Cloud Storage FUSE, and mount the Cloud Storage bucket on a Compute Engine instance. Remove the completed files from the TSV file. Use a shell script to iterate through the TSV file and download the remaining URLs to the FUSE mount point.
    - ( ) B. Renew the TLS certificate of the HTTPS endpoint. Remove the completed files from the TSV file and rerun the Storage Transfer Service job.
    - (x) C. Create a new TSV file for the remaining files by generating signed URLs with a longer validity period. Split the TSV file into multiple smaller files and submit them as separate Storage Transfer Service jobs in parallel.
    - ( ) D. Update the file checksums in the TSV file from using MD5 to SHA256. Remove the completed files from the TSV file and rerun the Storage Transfer Service job.

6. You are training a spam classifier. You notice that you are overfitting the training data. Which three actions can you take to resolve this problem? (Choose three.)
    - [x] A. Get more training examples
    - [ ] B. Reduce the number of training examples
    - [x] C. Use a smaller set of features
    - [ ] D. Use a larger set of features
    - [x] E. Increase the regularization parameters
    - [x] F. Decrease the regularization parameters

6. Your organization has been collecting and analyzing data in Google BigQuery for 6 months. The majority of the data analyzed is placed in a time-partitioned table named events_partitioned. To reduce the cost of queries, your organization created a view called events, which queries only the last 14 days of data. The view is described in legacy SQL. Next month, existing applications will be connecting to BigQuery to read the events data via an ODBC connection. You need to ensure the applications can connect. Which two actions should you take? (Choose two.)

    - ( ) A. Create a new view over events using standard SQL
    - ( ) B. Create a new partitioned table using a standard SQL query
    - ( ) C. Create a new view over events_partitioned using standard SQL
    - (x) D. Create a service account for the ODBC connection to use for authentication
    - ( ) E. Create a Google Cloud Identity and Access Management (Cloud IAM) role for the ODBC connection and shared 

6. Your organization uses a multi-cloud data storage strategy, storing data in Cloud Storage, and data in Amazon Web Services’ (AWS) $3 storage buckets. All data resides in US regions. You want to query up-to-date data by using BigQuery, regardless of which cloud the data is stored in. You need to allow users to query the tables from BigQuery without giving direct access to the data in the storage buckets. What should you do?
   
    - (x) A. Setup a BigQuery Omni connection to the AWS S3 bucket data. Create BigLake tables over the Cloud Storage and S3 data and query the data using BigQuery directly.
    - ( ) B. Set up a BigQuery Omni connection to the AWS S3 bucket data. Create external tables over the Cloud Storage and S3 data and query the data using BigQuery directly.
    - ( ) C. Use the Storage Transfer Service to copy data from the AWS S3 buckets to Cloud Storage buckets. Create BigLake tables over the Cloud Storage data and query the data using BigQuery directly.
    - ( ) D. Use the Storage Transfer Service to copy data from the AWS S3 buckets to Cloud Storage buckets. Create external tables over the Cloud Storage data and query the data using BigQuery directly.

6. Government regulations in your industry mandate that you have to maintain an auditable record of access to certain types of data. Assuming that all expiring logs will be archived correctly, where should you store data that is subject to that mandate?

    - ( ) A. Encrypted on Cloud Storage with user-supplied encryption keys. A separate decryption key will be given to each authorized user.
    - (x) B. In a BigQuery dataset that is viewable only by authorized personnel, with the Data Access log used to provide the auditability.
    - ( ) C. In Cloud SQL, with separate database user names to each user. The Cloud SQL Admin activity logs will be used to provide the auditability.
    - ( ) D. In a bucket on Cloud Storage that is accessible only by an AppEngine service that collects user information and logs the access before providing a link to the
bucket.

6. You are designing storage for very large text files for a data pipeline on Google Cloud. You want to support ANSI SQL queries. You also want to support compression and
parallel load from the input locations using Google recommended practices. What should you do?
    - ( ) A. Transform text files to compressed Avro using Cloud Dataflow. Use BigQuery for storage and query.
    - (x) B. Transform text files to compressed Avro using Cloud Dataflow. Use Cloud Storage and BigQuery permanent linked tables for query.
    - ( ) C. Compress text files to gzip using the Grid Computing Tools. Use BigQuery for storage and query.
    - ( ) D. Compress text files to gzip using the Grid Computing Tools. Use Cloud Storage, and then import into Cloud Bigtable for query.

6. You are selecting services to write and transform JSON messages from Cloud Pub/Sub to BigQuery for a data pipeline on Google Cloud. You want to minimize service costs. You also want to monitor and accommodate input data volume that will vary in size with minimal manual intervention. What should you do?

    - ( ) A. Use Cloud Dataproc to run your transformations. Monitor CPU utilization for the cluster. Resize the number of worker nodes in your cluster via the command line.
    - ( ) B. Use Cloud Dataproc to run your transformations. Use the diagnose command to generate an operational output archive. Locate the bottleneck and adjust cluster
resources.
    - (x) C. Use Cloud Dataflow to run your transformations. Monitor the job system lag with Stackdriver. Use the default autoscaling setting for worker instances.
    - ( ) D. Use Cloud Dataflow to run your transformations. Monitor the total execution time for a sampling of jobs. Configure the job to use non-default Compute Engine
machine types when needed.

6. Your company receives both batch- and stream-based event data. You want to process the data using Google Cloud Dataflow over a predictable time period. However, you realize that in some instances data can arrive late or out of order. How should you design your Cloud Dataflow pipeline to handle data that is late or out of order?

    - ( ) A. Set a single global window to capture all the data.
    - ( ) B. Set sliding windows to capture all the lagged data.
    - (x) C. Use watermarks and timestamps to capture the lagged data.
    - ( ) D. Ensure every datasource type (stream or batch) has a timestamp, and use the timestamps to define the logic for lagged data.

6. Your company maintains a hybrid deployment with GCP, where analytics are performed on your anonymized customer data. The data are imported to Cloud Storage from your data center through parallel uploads to a data transfer server running on GCP. Management informs you that the daily transfers take too long and have asked you to fix the problem. You want to maximize transfer speeds. Which action should you take?

    - ( ) A. Increase the CPU size on your server.
    - ( ) B. Increase the size of the Google Persistent Disk on your server.
    - (x) C. Increase your network bandwidth from your datacenter to GCP,
    - ( ) D. Increase your network bandwidth from Compute Engine to Cloud Storage.

6. You are developing an application on Google Cloud that will automatically generate subject labels for users’ blog posts. You are under competitive pressure to add this feature quickly, and you have no additional developer resources. No one on your team has experience with machine learning. What should you do?

    - (x) A. Call the Cloud Natural Language API from your application. Process the generated Entity Analysis as labels.
    - ( ) B. Call the Cloud Natural Language API from your application. Process the generated Sentiment Analysis as labels.
    - ( ) C. Build and train a text classification model using TensorFlow. Deploy the model using Cloud Machine Learning Engine. Call the model from your application and
process the results as labels.
    - ( ) D. Build and train a text classification model using TensorFlow. Deploy the model using a Kubernetes Engine cluster. Call the model from your application and process
the results as labels.

6. An organization maintains a Google BigQuery dataset that contains tables with user-level data. They want to expose aggregates of this data to other Google Cloud projects, while still controlling access to the user-level data. Additionally, they need to minimize their overall storage cost and ensure the analysis cost for other projects is assigned to those projects. What should they do?

    - (x) A. Create and share an authorized view that provides the aggregate results.
    - ( ) B. Create and share a new dataset and view that provides the aggregate results.
    - ( ) C. Create and share a new dataset and table that contains the aggregate results.
    - ( ) D. Create dataViewer Identity and Access Management (IAM) roles on the dataset to enable sharing.

6. Your infrastructure includes a set of YouTube channels. You have been tasked with creating a process for sending the YouTube channel data to Google Cloud for analysis. You want to design a solution that allows your world-wide marketing teams to perform ANSI SQL and other types of analysis on up-to-date YouTube channels log data. How should you set up the log data transfer into Google Cloud?

    - ( ) A. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination.
    - ( ) B. Use Storage Transfer Service to transfer the offsite backup files to a Cloud Storage Regional bucket as a final destination.
    - (x) C. Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Multi-Regional storage bucket as a final destination.
    - ( ) D. Use BigQuery Data Transfer Service to transfer the offsite backup files to a Cloud Storage Regional storage bucket as a final destination.

6. You are architecting a data transformation solution for BigQuery. Your developers are proficient with SQL and want to use the ELT development technique. In addition, your developers need an intuitive coding environment and the ability to manage SQL as code. You need to identify a solution for your developers to build these pipelines. What should you do?

    - (x) A. Use Dataform to build, manage, and schedule SQL pipelines.
    - ( ) B. Use Dataflow jobs to read data from Pub/Sub, transform the data, and load the data to BigQuery.
    - ( ) C. Use Data Fusion to build and execute ETL pipelines.
    - ( ) D. Use Cloud Composer to load data and run SQL pipelines by using the BigQuery job operators.

6. You have some data, which is shown in the graphic below. The two dimensions are X and Y, and the shade of each dot represents what class it is. You want to classify this data accurately using a linear algorithm. To do this you need to add a synthetic feature. What should the value of that feature be?

    - (x) A. X2+Y2
    - ( ) B. X2
    - ( ) C. Y2
    - ( ) D. cos(X)

6. You are developing an application that uses a recommendation engine on Google Cloud. Your solution should display new videos to customers based on past views. Your solution needs to generate labels for the entities in videos that the customer has viewed. Your design must be able to provide very fast filtering suggestions based on data from other customer preferences on several TB of data. What should you do?

    - ( ) A. Build and train a complex classification model with Spark MLIib to generate labels and filter the results. Deploy the models using Cloud Dataproc. Call the model from your application.
    - ( ) B. Build and train a classification model with Spark MLlib to generate labels. Build and train a second classification model with Spark MLIib to filter results to match customer preferences. Deploy the models using Cloud Dataproc. Call the models from your application.
    - (x) C. Build an application that calls the Cloud Video Intelligence API to generate labels. Store data in Cloud Bigtable, and filter the predicted labels to match the user's viewing history to generate preferences.
    - ( ) D. Build an application that calls the Cloud Video Intelligence API to generate labels. Store data in Cloud SQL, and join and filter the predicted labels to match the
user's viewing history to generate preferences.


6. You are building a data pipeline on Google Cloud. You need to prepare data using a casual method for a machine-learning process. You want to support a logistic regression model. You also need to monitor and adjust for null values, which must remain real-valued and cannot be removed. What should you do?
   
    - ( ) A. Use Cloud Dataprep to find null values in sample source data. Convert all nulls to ‘none’ using a Cloud Dataproc job.
    - (x) B. Use Cloud Dataprep to find null values in sample source data. Convert all nulls to 0 using a Cloud Dataprep job.
    - ( ) C. Use Cloud Dataflow to find null values in sample source data. Convert all nulls to ‘none’ using a Cloud Dataprep job.
    - ( ) D. Use Cloud Dataflow to find null values in sample source data. Convert all nulls to 0 using a custom script.

6. Your analytics team wants to build a simple statistical model to determine which customers are most likely to work with your company again, based on a few different metrics. They want to run the model on Apache Spark, using data housed in Google Cloud Storage, and you have recommended using Google Cloud Dataproc to execute this job. Testing has shown that this workload can run in approximately 30 minutes on a 15-node cluster, outputting the results into Google BigQuery. The plan is to run this workload weekly. How should you optimize the cluster for cost?

    - ( ) A. Migrate the workload to Google Cloud Dataflow
    - (x) B. Use pre-emptible virtual machines (VMs) for the cluster
    - ( ) C. Use a higher-memory node so that the job runs faster
    - ( ) D. Use SSDs on the worker nodes so that the job can run faster

6. You are managing a Dataplex environment with raw and curated zones. A data engineering team is uploading JSON and CSV files to a bucket asset in the curated zone but the files are not being automatically discovered by Dataplex. What should you do to ensure that the files are discovered by Dataplex?

    - (x) A. Move the JSON and CSV files to the raw zone.
    - ( ) B. Enable auto-discovery of files for the curated zone.
    - ( ) C. Use the bg command-line tool to load the JSON and CSV files into BigQuery tables.
    - ( ) D. Grant object level access to the CSV and JSON files in Cloud Storage.

6. Your neural network model is taking days to train. You want to increase the training speed. What can you do?
    - ( ) A. Subsample your test dataset.
    - (x) B. Subsample your training dataset.
    - ( ) C. Increase the number of input features to your model.
    - ( ) D. Increase the number of layers in your neural network.

6. You are designing storage for two relational tables that are part of a 10-TB database on Google Cloud. You want to support transactions that scale horizontally. You also want to optimize data for range queries on non-key columns. What should you do?

    - ( ) A. Use Cloud SQL for storage. Add secondary indexes to support query patterns.
    - ( ) B. Use Cloud SQL for storage. Use Cloud Dataflow to transform data to support query patterns.
    - (x) C. Use Cloud Spanner for storage. Add secondary indexes to support query patterns.
    - ( ) D. Use Cloud Spanner for storage. Use Cloud Dataflow to transform data to support query patterns.

6. You work for a farming company. You have one BigQuery table named sensors, which is about 500 MB and contains the list of your 5000 sensors, with columns for id, name, and location. This table is updated every hour. Each sensor generates one metric every 30 seconds along with a timestamp, which you want to store in BigQuery. You want to run an analytical query on the data once a week for monitoring purposes. You also want to minimize costs. What data model should you use?
    - ( ) A. 
        1. Create a metrics column in the sensors table.
            2. Set RECORD type and REPEATED mode for the metrics column.
            3. Use an UPDATE statement every 30 seconds to add new metrics.
    - ( ) B. 
        1. Create a metrics column in the sensors table.
            2. Set RECORD type and REPEATED mode for the metrics column.
            3. Use an INSERT statement every 30 seconds to add new metrics.
    - (x) C. 
    1. Create a metrics table partitioned by timestamp.
        2. Create a sensorld column in the metrics table, that points to the id column in the sensors table.
        3. Use an INSERT statement every 30 seconds to append new metrics to the metrics table.

    - ( ) D. 
    1. Create a metrics table partitioned by timestamp.
        2. Create a sensorld column in the metrics table, which points to the id column in the sensors table.
        3. Use an UPDATE statement every 30 seconds to append new metrics to the metrics table.
        4. Join the two tables, if needed, when running the analytical query.

6. You set up a streaming data insert into a Redis cluster via a Kafka cluster. Both clusters are running on Compute Engine instances. You need to encrypt data at rest with encryption keys that you can create, rotate, and destroy as needed. What should you do?

    - [ ] A. Create a dedicated service account, and use encryption at rest to reference your data stored in your Compute Engine cluster instances as part of your API service calls.
    - [x] B. Create encryption keys in Cloud Key Management Service. Use those keys to encrypt your data in all of the Compute Engine cluster instances.
    - [ ] C. Create encryption keys locally. Upload your encryption keys to Cloud Key Management Service. Use those keys to encrypt your data in all of the Compute Engine cluster instances.
    - [x] D. Create encryption keys in Cloud Key Management Service. Reference those keys in your API service calls when accessing the data in your Compute Engine cluster instances.

6. You have a table that contains millions of rows of sales data, partitioned by date. Various applications and users query this data many times a minute. The query requires aggregating values by using AVG, MAX, and SUM, and does not require joining to other tables. The required aggregations are only computed over the past year of data, though you need to retain full historical data in the base tables. You want to ensure that the query results always include the latest data from the tables, while also reducing computation cost, maintenance overhead, and duration. What should you do?

    - ( ) A. Create a materialized view to aggregate the base table data. Include a filter clause to specify the last one year of partitions.
    - (x) B. Create a materialized view to aggregate the base table data. Configure a partition expiration on the base table to retain only the last one year of partitions.
    - ( ) C. Create a view to aggregate the base table data. Include a filter clause to specify the last year of partitions.
    - ( ) D. Create a new table that aggregates the base table data. Include a filter clause to specify the last year of partitions. Set up a scheduled query to recreate the new table every hour.

6. You are designing storage for 20 TB of text files as part of deploying a data pipeline on Google Cloud. Your input data is in CSV format. You want to minimize the cost of querying aggregate values for multiple users who will query the data in Cloud Storage with multiple engines. Which storage service and schema design should you use?

    - ( ) A. Use Cloud Bigtable for storage. Install the HBase shell on a Compute Engine instance to query the Cloud Bigtable data.
    - ( ) B. Use Cloud Bigtable for storage. Link as permanent tables in BigQuery for query.
    - (x) C. Use Cloud Storage for storage. Link as permanent tables in BigQuery for query.
    - ( ) D. Use Cloud Storage for storage. Link as temporary tables in BigQuery for query.

6.  You are responsible for writing your company's ETL pipelines to run on an Apache Hadoop cluster. The pipeline will require some checkpointing and splitting pipelines. Which method should you use to write the pipelines?

    - (x) A. PigLatin using Pig
    - ( ) B. HiveQL using Hive
    - ( ) C. Java using MapReduce
    - ( ) D. Python using MapReduce

6. Your financial services company is moving to cloud technology and wants to store 50 TB of financial time-series data in the cloud. This data is updated frequently and new data will be streaming in all the time. Your company also wants to move their existing Apache Hadoop jobs to the cloud to get insights into this data. Which product should they use to store the data?

    - (x) A. Cloud Bigtable
    - ( ) B. Google BigQuery
    - ( ) C. Google Cloud Storage
    - ( ) D. Google Cloud Datastore

6. Sample
    - ( )
    - ( )
    - ( )
    - ( )

6. Sample
    - ( )
    - ( )
    - ( )
    - ( )

6. Sample
    - ( )
    - ( )
    - ( )
    - ( )

6. Sample
    - ( )
    - ( )
    - ( )
    - ( )