---
id: 83f0b3b9-df7b-4b70-afc7-ba0de20f787d
name: Check if user is a member of db_owner role
type: command
executor: bash
data: select is_member('db_owner');
output: null
created_at: '2023-04-06T03:56:20.649845+00:00'
updated_at: '2023-04-10T20:36:41.379800+00:00'
---

# Check if user is a member of db_owner role

```bash
select is_member('db_owner');
```
