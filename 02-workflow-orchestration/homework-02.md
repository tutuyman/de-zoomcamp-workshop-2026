# Question 1
Use flow [module_08](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/flows/08_gcp_taxi.yaml)  
or [module_09](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/02-workflow-orchestration/flows/09_gcp_taxi_scheduled.yaml)  
Chose Yellow, year 2020, month 12  
After execute chech in Executions -> Outputs -> extract -> outputFiles -> yellow_tripdata_2020-12.csv  
There you can see the uncompressed file size. The size should be 128.3 MiB

# Question 2  
After running Year 2020 and Month 4
See the file in Executions -> Overview  -> Labels Row  
the answer should be file:green_tripdata_2020-04.csv   

# Question 4  
I do question 4 because green has smaller size  
Using flow 09, set the range from year 2020 month 01 date 01 to year 2020 month 12 date 03(to make sure dataset month 12 include, can using date 1 in month 12 but make sure the time over 9am(09:00))  
Do query in GCP 
SELECT COUNT(*)
FROM `project_id.dataset.green_tripdata`
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2020;  
Use lpep_pickup_datetime because its Partitioned on field  
I got return 1.733.998, abit difference but close enough  

# Question 3
Similar to Question 4, but chose yellow this time and do query in GCP  
SELECT COUNT(*)
FROM `project_id.dataset.yellow_tripdata`
WHERE EXTRACT(YEAR FROM tpep_pickup_datetime) = 2020;
i got return of 24648219, close enough  

# Question 5  
Refer to example 08 and 09  
In trigger section add
triggers:
  - id: schedule  
    type: io.kestra.plugin.core.trigger.Schedule  
    cron: "0 9 1 * *"  
    timezone: America/New_York <-- Add this





