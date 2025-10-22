---
id: b7c52074-3cae-4407-9dff-3ba644403fd4
name: Modify Certificate Template for domain.local/user
type: command
executor: bash
data: python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip
  10.10.10.10 -get-acl
output: null
created_at: '2023-04-06T03:56:05.849730+00:00'
updated_at: '2023-04-10T20:25:59.025048+00:00'
---

# Modify Certificate Template for domain.local/user

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template user -dc-ip 10.10.10.10 -get-acl
```
