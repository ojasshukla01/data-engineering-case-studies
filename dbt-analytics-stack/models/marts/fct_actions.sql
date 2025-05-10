with events as (
    select * from {{ ref('stg_events') }}
)

select
    action,
    count(*) as total_events,
    min(event_time) as first_seen,
    max(event_time) as last_seen
from events
group by action
