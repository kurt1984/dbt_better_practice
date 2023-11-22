select *
from {{ source('hosp', 'omr') }}
limit 10
