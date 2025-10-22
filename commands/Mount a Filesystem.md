---
id: 045d9046-9c91-4493-a88c-14808b4a3caf
name: Mount a Filesystem
type: command
executor: bash
data: mount $_FILESYSTEM $_MOUNT_POINT
output: mount /dev/mapper/crypt-home /mnt/
created_at: '2019-11-04T20:35:41.684536+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Mount a Filesystem

```bash
mount $_FILESYSTEM $_MOUNT_POINT
```

## Expected Output

```
mount /dev/mapper/crypt-home /mnt/
```
