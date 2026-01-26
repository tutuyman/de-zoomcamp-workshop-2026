# Question 1
pip --version  
What i got is 25.03, maybe some older image use 24.3

# Question 2
postgres:5432

By looking the docker compose of postgres

services:
  db:
    container_name: postgres

ports:
      - '5433:5432'
Access port number is right of colon (:)

# Question 3
```
SELECT COUNT(*) AS trips_le_1_mile
FROM public.green_tripdata_2025_11
WHERE lpep_pickup_datetime >= TIMESTAMP '2025-11-01'
  AND lpep_pickup_datetime <  TIMESTAMP '2025-12-01'
  AND trip_distance <= 1;
```

Return output is 8007

# Question 4
```
SELECT
    DATE(lpep_pickup_datetime) AS pickup_day,
    MAX(trip_distance) AS longest_trip_distance
FROM public.green_tripdata_2025_11
WHERE trip_distance < 100
GROUP BY DATE(lpep_pickup_datetime)
ORDER BY longest_trip_distance DESC
LIMIT 1;
```

Return output is  
2025-11-14  |   88.03

# Question 5
select * from public.zones
limit 100;
```
SELECT
    z."Zone" AS pickup_zone,
    SUM(t.total_amount) AS total_revenue
FROM public.green_tripdata_2025_11 t
JOIN public.zones z
  ON t."PULocationID" = z."LocationID"
WHERE DATE(t.lpep_pickup_datetime) = DATE '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_revenue DESC
LIMIT 1;
```
Return output is  
East Harlem North   |   9281.920000000002

# Question 6
```
SELECT
    dz."Zone" AS dropoff_zone,
    MAX(t."tip_amount") AS largest_tip
FROM public.green_tripdata_2025_11 t
JOIN public.zones pz
  ON t."PULocationID" = pz."LocationID"
JOIN public.zones dz
  ON t."DOLocationID" = dz."LocationID"
WHERE pz."Zone" = 'East Harlem North'
  AND t.lpep_pickup_datetime >= TIMESTAMP '2025-11-01'
  AND t.lpep_pickup_datetime <  TIMESTAMP '2025-12-01'
GROUP BY dz."Zone"
ORDER BY largest_tip DESC
LIMIT 10;
```

Largest tip  
dropoff_zone        largest tip
Yorkville West      81.89

# Question 7
terraform init, terraform apply -auto-approve, terraform destroy

all show in video, but markdown and course question abit difference, in markdown contain "auto-executing the plan".  
but the answer has no option terraform init, terraform apply -y, terraform destroy  
so terraform init, terraform apply -auto-approve, terraform destroy 
