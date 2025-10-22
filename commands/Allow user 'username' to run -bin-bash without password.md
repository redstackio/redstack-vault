---
id: 05e968df-e9c4-492c-8b1d-f1e8c731a0f0
name: Allow user 'username' to run /bin/bash without password
type: command
executor: bash
data: 'echo "username ALL=NOPASSWD: /bin/bash" >>/etc/sudoers'
output: null
created_at: '2023-04-06T03:56:19.286503+00:00'
updated_at: '2023-04-10T20:34:29.642335+00:00'
---

# Allow user 'username' to run /bin/bash without password

```bash
echo "username ALL=NOPASSWD: /bin/bash" >>/etc/sudoers
```
