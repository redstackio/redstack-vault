---
id: 07f3bebc-8d60-45ae-ae78-0741b4d11041
name: Sync the Local System to a Remote System via Anonymous SMB
type: command
executor: bash
data: net time set -S $_DC_IP
output: root@kali:~# net time set -S 10.10.10.5
created_at: '2020-06-24T05:08:26.192653+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Sync the Local System to a Remote System via Anonymous SMB

```bash
net time set -S $_DC_IP
```

## Expected Output

```
root@kali:~# net time set -S 10.10.10.5
```


