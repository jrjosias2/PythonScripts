
  
    

        create or replace transient table AIRBNB.DEV.dim_hosts_cleansed
         as
        (WITH src_hosts AS (
    SELECT * FROM AIRBNB.DEV.src_hosts
)
SELECT
    host_id,
    NVL(host_name,'Anonymous') AS host_name,
    is_superhost,
    created_at,
    updated_at
FROM src_hosts
        );
      
  