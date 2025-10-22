---
id: 8c601f18-733a-418e-bf4b-eef7777c8f71
name: Allow user 'username' to use sudo without password
type: command
executor: bash
data: 'echo "username ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers'
output: null
created_at: '2023-04-06T03:56:19.286323+00:00'
updated_at: '2023-04-10T20:34:29.642335+00:00'
---

# Allow user 'username' to use sudo without password

```bash
echo "username ALL=(ALL) NOPASSWD: ALL" >>/etc/sudoers
```
