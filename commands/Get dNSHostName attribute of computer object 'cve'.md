---
id: 088f4cc1-fea7-43e4-bd6e-9ba3229f7116
name: Get dNSHostName attribute of computer object 'cve'
type: command
executor: bash
data: python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10
  getObjectAttributes 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName
output: null
created_at: '2023-04-06T03:56:06.137368+00:00'
updated_at: '2023-04-10T20:36:10.281363+00:00'
---

# Get dNSHostName attribute of computer object 'cve'

```bash
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 getObjectAttributes 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName
```


