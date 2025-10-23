---
id: 1383c460-58dc-441b-ab7c-9d43ed0e487c
name: SSH Local Port Forwarding to a Remote Server
type: command
executor: bash
data: ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
output: root@kali:~# ssh -f -N -L 8001:10.10.10.11:80 root@10.10.10.10
created_at: '2019-10-02T01:10:12.259465+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSH Local Port Forwarding to a Remote Server

```bash
ssh -f -N -L $_ATTACKER_PORT:$_REMOTE_IP:$_REMOTE_PORT $_USER@$_TARGET_IP
```

## Expected Output

```
root@kali:~# ssh -f -N -L 8001:10.10.10.11:80 root@10.10.10.10
```


