---
id: dc20dc95-126d-4b56-b389-fd88b300cd67
name: 'View open TCP ports of current machine:'
type: command
executor: bash
data: 'netstat -a -n -p tcp | find "LISTEN"

  '
output: null
created_at: '2020-07-14T18:21:27.746616+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# View open TCP ports of current machine:

```bash
netstat -a -n -p tcp | find "LISTEN"

```
