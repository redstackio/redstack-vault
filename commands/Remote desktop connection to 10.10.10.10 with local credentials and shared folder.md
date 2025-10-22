---
id: 9e3acc3c-c9df-4b3b-affc-d781f0ea03dc
name: Remote desktop connection to 10.10.10.10 with local credentials and shared folder
type: command
executor: bash
data: rdesktop -u username -p password -g 70% -r disk:share=/tmp/myshare 10.10.10.10
output: null
created_at: '2023-04-06T03:56:31.072359+00:00'
updated_at: '2023-04-10T20:38:03.093770+00:00'
---

# Remote desktop connection to 10.10.10.10 with local credentials and shared folder

```bash
rdesktop -u username -p password -g 70% -r disk:share=/tmp/myshare 10.10.10.10
```
