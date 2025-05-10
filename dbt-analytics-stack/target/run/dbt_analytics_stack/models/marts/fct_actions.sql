
  
    
    

    create  table
      "events"."main"."fct_actions__dbt_tmp"
  
    as (
      with events as (
    select * from "events"."main"."stg_events"
)

select
    action,
    count(*) as total_events,
    min(event_time) as first_seen,
    max(event_time) as last_seen
from events
group by action
    );
  
  