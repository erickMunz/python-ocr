# GCP Data engineer test part3

---


1. You work for a manufacturing plant that batches application log files together into a single log file once a day at 2:00 AM. You have written a Google Cloud Dataflow job to process that log file. You need to make sure the log file in processed once per day as inexpensively as possible. What should you do?

    - ( ) A. Change the processing job to use Google Cloud Dataproc instead.
    - ( ) B. Manually start the Cloud Dataflow job each morning when you get into the office.
    - (x) C. Create a cron job with Google App Engine Cron Service to run the Cloud Dataflow job.
    - ( ) D. Configure the Cloud Dataflow job as a streaming job so that it processes the log data immediately.

2. CFO Statement -
        The project is too large for us to maintain the hardware and software required for the data and analysis. Also, we cannot afford to staff an operations team to monitor so many data feeds, so we will rely on automation and infrastructure. Google Cloud's machine learning will allow our quantitative researchers to work on our high-value problems instead of problems with our data pipelines.
        You need to compose visualizations for operations teams with the following requirements:

        The report must include telemetry data from all 50,000 installations for the most resent 6 weeks (sampling once every minute).

        The report must not be more than 3 hours delayed from live data.

        The actionable report should only show suboptimal links.

        Most suboptimal links should be sorted to the top.

        Suboptimal links can be grouped and filtered by regional geography.

        User response time to load the report must be <5 seconds.
        Which approach meets the requirements?

    - ( ) A. Load the data into Google Sheets, use formulas to calculate a metric, and use filters/sorting to show only suboptimal links in a table.
    - ( ) B. Load the data into Google BigQuery tables, write Google Apps Script that queries the data, calculates the metric, and shows only suboptimal rows in a table in Google Sheets.
    - ( ) C. Load the data into Google Cloud Datastore tables, write a Google App Engine Application that queries all rows, applies a function to derive the metric, and then renders results in a table using the Google charts and visualization API.
    - (x) D. Load the data into Google BigQuery tables, write a Google Data Studio 360 report that connects to your data, calculates a metric, and then uses a filter expression to show only suboptimal rows in a table.

3. You want to use Google Stackdriver Logging to monitor Google BigQuery usage. You need an instant notification to be sent to your monitoring tool when new data is appended to a certain table using an insert job, but you do not want to receive notifications for other tables. What should you do?

    - ( ) A. Make a call to the Stackdriver API to list all logs, and apply an advanced filter.
    - ( ) B. In the Stackdriver logging admin interface, and enable a log sink export to BigQuery.
    - ( ) C. In the Stackdriver logging admin interface, enable a log sink export to Google Cloud Pub/Sub, and subscribe to the topic from your monitoring tool.
    - (x) D. Using the Stackdriver API, create a project sink with advanced log filter to export to Pub/Sub, and subscribe to the topic from your monitoring tool.

4. Business owners at your company have given you a database of bank transactions. Each row contains the user ID, transaction type, transaction location, and transaction
amount. They ask you to investigate what type of machine learning can be applied to the data. Which three machine learning applications can you use? (Choose three.)



F. Unsupervised learning to predict the location of a transaction.
    - [ ] A. Supervised learning to determine which transactions are most likely to be fraudulent.
    - [x] B. Unsupervised learning to determine which transactions are most likely to be fraudulent.
    - [x] C. Clustering to divide the transactions into N categories based on feature similarity.
    - [x] D. Supervised learning to predict the location of a transaction.
    - [ ] E. Reinforcement learning to predict the location of a transaction.
    - [x] F. Unsupervised learning to predict the location of a transaction.

5. Your company is streaming real-time sensor data from their factory floor into Bigtable and they have noticed extremely poor performance. How should the row key be redesigned to improve Bigtable performance on queries that populate real-time dashboards?

    - ( ) A. Use a row key of the form <timestamp>.
    - ( ) B. Use a row key of the form <sensorid>.
    - (x) C. Use a row key of the form <timestamp>#<sensorid>.
    - ( ) D. Use a row key of the form >#<sensorid>#<timestamp>.

6. You want to use a database of information about tissue samples to classify future tissue samples as either normal or mutated. You are evaluating an unsupervised anomaly detection method for classifying the tissue samples. Which two characteristic support this method? (Choose two.)


    - (x) A. There are very few occurrences of mutations relative to normal samples.
    - ( ) B. There are roughly equal occurrences of both normal and mutated samples in the database.
    - ( ) C. You expect future mutations to have different features from the mutated samples in the database.
    - (x) D. You expect future mutations to have similar features to the mutated samples in the database.
    - ( ) E. You already have labels for which samples are mutated and which are normal in the database.

7. Sample
    - ( )
    - ( )
    - ( )
    - ( )

8. Sample
    - ( )
    - ( )
    - ( )
    - ( )

9. Sample
    - ( )
    - ( )
    - ( )
    - ( )

10. Sample
    - ( )
    - ( )
    - ( )
    - ( )

11. Sample
    - ( )
    - ( )
    - ( )
    - ( )

12. Sample
    - ( )
    - ( )
    - ( )
    - ( )

13. Sample
    - ( )
    - ( )
    - ( )
    - ( )

14. Sample
    - ( )
    - ( )
    - ( )
    - ( )

15. Sample
    - ( )
    - ( )
    - ( )
    - ( )

16. Sample
    - ( )
    - ( )
    - ( )
    - ( )

17. Sample
    - ( )
    - ( )
    - ( )
    - ( )

18. Sample
    - ( )
    - ( )
    - ( )
    - ( )

19. Sample
    - ( )
    - ( )
    - ( )
    - ( )

20. Sample
    - ( )
    - ( )
    - ( )
    - ( )

21. Sample
    - ( )
    - ( )
    - ( )
    - ( )

22. Sample
    - ( )
    - ( )
    - ( )
    - ( )

23. Sample
    - ( )
    - ( )
    - ( )
    - ( )

24. Sample
    - ( )
    - ( )
    - ( )
    - ( )

25. Sample
    - ( )
    - ( )
    - ( )
    - ( )

26. Sample
    - ( )
    - ( )
    - ( )
    - ( )

27. Sample
    - ( )
    - ( )
    - ( )
    - ( )

28. Sample
    - ( )
    - ( )
    - ( )
    - ( )

29. Sample
    - ( )
    - ( )
    - ( )
    - ( )

30. Sample
    - ( )
    - ( )
    - ( )
    - ( )

31. Sample
    - ( )
    - ( )
    - ( )
    - ( )

32. Sample
    - ( )
    - ( )
    - ( )
    - ( )

33. Sample
    - ( )
    - ( )
    - ( )
    - ( )

34. Sample
    - ( )
    - ( )
    - ( )
    - ( )

35. Sample
    - ( )
    - ( )
    - ( )
    - ( )

36. Sample
    - ( )
    - ( )
    - ( )
    - ( )

37. Sample
    - ( )
    - ( )
    - ( )
    - ( )

38. Sample
    - ( )
    - ( )
    - ( )
    - ( )

39. Sample
    - ( )
    - ( )
    - ( )
    - ( )

40. Sample
    - ( )
    - ( )
    - ( )
    - ( )

41. Sample
    - ( )
    - ( )
    - ( )
    - ( )

42. Sample
    - ( )
    - ( )
    - ( )
    - ( )

43. Sample
    - ( )
    - ( )
    - ( )
    - ( )

44. Sample
    - ( )
    - ( )
    - ( )
    - ( )

45. Sample
    - ( )
    - ( )
    - ( )
    - ( )

46. Sample
    - ( )
    - ( )
    - ( )
    - ( )

47. Sample
    - ( )
    - ( )
    - ( )
    - ( )

48. Sample
    - ( )
    - ( )
    - ( )
    - ( )

49. Sample
    - ( )
    - ( )
    - ( )
    - ( )

50. Sample
    - ( )
    - ( )
    - ( )
    - ( )

51. Sample
    - ( )
    - ( )
    - ( )
    - ( )

52. Sample
    - ( )
    - ( )
    - ( )
    - ( )
