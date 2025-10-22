---
id: f5c950bc-bd83-4b3a-b300-65b73b8d7b0e
name: Create process on remote machine
type: command
executor: bash
data: wmic /node:target.domain /user:domain\user /password:password process call create
  "C:\Windows\System32\calc.exe”
output: null
created_at: '2023-04-06T03:56:31.252966+00:00'
updated_at: '2023-04-10T20:38:05.894594+00:00'
---

# Create process on remote machine

```bash
wmic /node:target.domain /user:domain\user /password:password process call create "C:\Windows\System32\calc.exe”
```
