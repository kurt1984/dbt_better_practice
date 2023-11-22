with seed as (
    select *
    from {{ ref('readmissions__potentially_planned_icd_10_pcs') }}
)

select *
from seed
limit 10