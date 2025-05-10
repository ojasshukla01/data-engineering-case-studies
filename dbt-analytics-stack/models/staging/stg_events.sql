with source as (
    select * from {{ ref('events') }}
)

select
    id,
    action,
    cast(event_time as timestamp) as event_time
from source
