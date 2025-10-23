---
id: f62a4196-f84b-4bb6-be88-31f8aa2f72ac
name: Remote desktop connection to 10.10.10.10 with DOMAIN credentials and shared
  folder
type: command
executor: bash
data: rdesktop -d DOMAIN -u username -p password 10.10.10.10 -g 70 -r disk:share=/home/user/myshare
output: null
created_at: '2023-04-06T03:56:31.072288+00:00'
updated_at: '2023-04-10T20:38:03.093770+00:00'
---

# Remote desktop connection to 10.10.10.10 with DOMAIN credentials and shared folder

```bash
rdesktop -d DOMAIN -u username -p password 10.10.10.10 -g 70 -r disk:share=/home/user/myshare
```


