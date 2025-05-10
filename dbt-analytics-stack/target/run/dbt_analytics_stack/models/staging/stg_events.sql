
  
  create view "events"."main"."stg_events__dbt_tmp" as (
    with source as (
    select * from "events"."main"."events"
)

select
    id,
    action,
    cast(event_time as timestamp) as event_time
from source
  );
