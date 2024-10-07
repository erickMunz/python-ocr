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
    - ( ) B. Switch to TFRecords formats (appr. 200MB per file) instead of parquet files.
    - ( ) C. Switch from HDDs to SSDs, copy initial data from GCS to HDFS, run the Spark job and copy results back to GCS.
    - ( ) 


4. Who is the Co-Founder of MaxSoft?
    - [x] A. They have not assigned the timestamp, which causes the job to fail
    - [x] WebBot
    - [ ] Gauge
	- [ ] Selenium
