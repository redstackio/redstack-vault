---
id: 97c12e21-2c9f-4dc4-bb55-54c26b594ee2
name: Kill processes of specific user
type: command
executor: bash
data: 'sudo kill -9 `lsof -t -u username1`

  '
output: null
created_at: '2020-07-14T18:21:25.731374+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Kill processes of specific user

```bash
sudo kill -9 `lsof -t -u username1`

```


