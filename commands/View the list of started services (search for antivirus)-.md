---
id: 8569e131-bd18-448d-ba9a-d81f71e9d098
name: 'View the list of started services (search for antivirus):'
type: command
executor: bash
data: 'net start

  sc query

  '
output: null
created_at: '2020-07-14T18:21:27.742888+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# View the list of started services (search for antivirus):

```bash
net start
sc query

```


