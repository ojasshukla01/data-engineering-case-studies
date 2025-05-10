with events as (
    select * from "dbt"."main"."stg_events"
)

select
    action,
    count(*) as total_events,
    min(event_time) as first_seen,
    max(event_time) as last_seen
from events
group by action