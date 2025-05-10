with source as (
    select * from {{ source('raw', 'events') }}
)

select
    id,
    action,
    cast(event_time as timestamp) as event_time
from source
