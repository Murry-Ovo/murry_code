select
*
from
logs_bigquery.data_access_friendly
where
query_initiator = 'andrew.morris@ovoenergy.com'
and query_sql like ('%v_Customer%')
and lower(query_sql) like ('%is_bad%')