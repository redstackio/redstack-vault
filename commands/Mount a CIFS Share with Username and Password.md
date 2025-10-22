---
id: b35f5598-bbcb-4fb1-b78b-c1e797705649
name: Mount a CIFS Share with Username and Password
type: command
executor: bash
data: mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="$_USERNAME",password="$_PASSWORD"'
  /$_MOUNT_POINT
output: null
created_at: '2019-12-16T22:19:45.822753+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a CIFS Share with Username and Password

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="$_USERNAME",password="$_PASSWORD"' /$_MOUNT_POINT
```
