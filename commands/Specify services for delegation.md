---
id: 9b912949-3d37-4d26-bdeb-8fc31e864336
name: Specify services for delegation
type: command
executor: bash
data: Set-ADUser -Identity 'User1' -ServicePrincipalNames 'http/Server1.domain.com',
  'http/Server2.domain.com'
output: null
created_at: '2023-04-06T03:56:07.951472+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Specify services for delegation

```bash
Set-ADUser -Identity 'User1' -ServicePrincipalNames 'http/Server1.domain.com', 'http/Server2.domain.com'
```
