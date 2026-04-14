-- Union green and yellow taxi data into a single dataset
-- Demonstrates how to combine data from multiple sources with slightly different schemas

with green_trips as (
    select *
    from {{ ref("stg_green_tripdata") }}
),

yellow_trips as (
    select *
    from {{ ref("stg_yellow_tripdata") }}
),

trips_unioned as(
    select * from green_trips
    union all
    select * from yellow_trips
)

select distinct pickup_location_id from trips_unioned