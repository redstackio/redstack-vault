---
id: 3aff3b3f-9d45-4d48-ad47-a2f2c7b5460a
name: winrm test connection to winrm service
type: command
executor: ''
data: winrm identify -r:http://$TARGET_IP:5985 -auth:basic -u:$USERNAME -p:$PASSWORD
  -encoding:utf-8
output: null
created_at: '2020-07-16T15:11:47.929201+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# winrm test connection to winrm service

```bash
winrm identify -r:http://$TARGET_IP:5985 -auth:basic -u:$USERNAME -p:$PASSWORD -encoding:utf-8
```


