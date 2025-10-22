---
id: 0d241a40-a23f-4a15-a205-33589cbbf414
name: net Sync a Computer's Time with a Remote Server
type: command
executor: bash
data: net time set -S $_TARGET_IP
output: root@kali:~# net time set -S 10.10.10.5
created_at: '2020-06-25T00:11:34.104899+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# net Sync a Computer's Time with a Remote Server

```bash
net time set -S $_TARGET_IP
```

## Expected Output

```
root@kali:~# net time set -S 10.10.10.5
```
