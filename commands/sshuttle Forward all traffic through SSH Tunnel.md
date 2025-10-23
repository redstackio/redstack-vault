---
id: 80bffd2d-b8f4-4dd2-92e6-c89a528aaae1
name: sshuttle Forward all traffic through SSH Tunnel
type: command
executor: bash
data: sshuttle -r root@localhost:2222 0/0
output: 'root@localhost''s password:

  client: Connected.

  '
created_at: '2019-10-16T01:44:10.322144+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# sshuttle Forward all traffic through SSH Tunnel

```bash
sshuttle -r root@localhost:2222 0/0
```

## Expected Output

```
root@localhost's password:
client: Connected.

```


