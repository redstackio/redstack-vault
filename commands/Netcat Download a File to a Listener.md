---
id: ebc2dbae-c2e2-4aa3-9c41-c7cff9760062
name: Netcat Download a File to a Listener
type: command
executor: bash
data: nc $_TARGET_IP $_TARGET_PORT > $_FILENAME
output: nc 10.10.10.10 443 > foo
created_at: '2019-10-29T22:25:12.734722+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Netcat Download a File to a Listener

```bash
nc $_TARGET_IP $_TARGET_PORT > $_FILENAME
```

## Expected Output

```
nc 10.10.10.10 443 > foo
```
