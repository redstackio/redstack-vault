---
id: d2a98965-4601-4996-9597-1ecfde65cc0c
name: Add sudo permissions for user 'username'
type: command
executor: bash
data: echo "username ALL=(ALL:ALL) ALL">>/etc/sudoers
output: null
created_at: '2023-04-06T03:56:19.284495+00:00'
updated_at: '2023-04-10T20:34:29.642335+00:00'
---

# Add sudo permissions for user 'username'

```bash
echo "username ALL=(ALL:ALL) ALL">>/etc/sudoers
```


