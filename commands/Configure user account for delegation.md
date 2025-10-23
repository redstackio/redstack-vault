---
id: 5af144db-2c27-46f2-afb7-5fb3b7ff4a4f
name: Configure user account for delegation
type: command
executor: bash
data: Set-ADUser -Identity 'User1' -TrustedForDelegation $true
output: null
created_at: '2023-04-06T03:56:07.951421+00:00'
updated_at: '2023-04-10T20:26:20.679788+00:00'
---

# Configure user account for delegation

```bash
Set-ADUser -Identity 'User1' -TrustedForDelegation $true
```


