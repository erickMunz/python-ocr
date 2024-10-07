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
	- ( ) D. They have not applied a non-global windowing function, which causes the job to fail when the pipeline is created

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


10. You need to connect multiple applications with dynamic public IP addresses to a Cloud SQL instance. You configured users with strong passwords and enforced the SSL
connection to your Cloud SQL instance. You want to use Cloud SQL public IP and ensure that you have secured connections. What should you do?
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
    - ( ) B. Create a BigQuery table partitioned by datetime value of the weather date. Set up partition expiration to 30 days.
    - ( ) C. Create a BigQuery table partitioned by ingestion time. Set up partition expiration to 30 days.
    - ( ) D. Create a BigQuery table with a datetime column for the day the weather data refers to. Run a scheduled query to delete rows with a datetime value older than 30
days.
   

14. You are integrating one of your internal IT applications and Google BigQuery, so users can query BigQuery from the application's interface. You do not want individual users to authenticate to BigQuery and you do not want to give them access to the dataset. You need to securely access BigQuery from your IT application. What should you do?
    - ( ) A. Create groups for your users and give those groups access to the dataset
    - ( ) B. Integrate with a single sign-on (SSO) platform, and pass each user's credentials along with the query request
    - ( ) C. Create a service account and grant dataset access to that account. Use the service account's private key to access the dataset
    - ( ) D. Create a dummy user and grant dataset access to that user. Store the username and password for that user in a file on the files system, and use those credentials
to access the BigQuery dataset

15. You have enabled the free integration between Firebase Analytics and Google BigQuery. Firebase now automatically creates a new table daily in BigQuery in the format
app_events_YYYYMMDD. You want to query all of the tables for the past 30 days in legacy SQL. What should you do?
    - (x) A. Use the TABLE_DATE_RANGE function
    - ( ) B. Use the WHERE_PARTITIONTIME pseudo column
    - ( ) C. Use WHERE date BETWEEN YYYY-MM-DD AND YYYY-MM-DD
    - ( ) D. Use SELECT IF.(date >= YYYY-MM-DD AND date <= YYYY-MM-DD

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


21. Sample
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