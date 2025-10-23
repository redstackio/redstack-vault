---
id: 57f9512a-6525-412f-b993-38a0cdd5405d
name: Mount a CIFS Share with a NULL Session
type: command
executor: bash
data: mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="",password=""' /$_MOUNT_POINT
output: null
created_at: '2019-12-16T22:19:45.822999+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a CIFS Share with a NULL Session

```bash
mount -t cifs //$_TARGET_IP/$_SHARE -o 'username="",password=""' /$_MOUNT_POINT
```


