Im using the python version because the jupyter always failed to authenticated the gcp  

## Question 1  
SELECT COUNT(*) AS total_records
FROM `zoomcamp.yellow_taxi_external`;  
the output should 20332093

## Question 2
### Do this query but the result is not the focus
SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations
FROM `zoomcamp.yellow_taxi_external`;  


## Question 4
SELECT COUNT(*) AS zero_fare_trips
FROM `zoomcamp.yellow_taxi_external`
WHERE fare_amount = 0;  
the result is 8333