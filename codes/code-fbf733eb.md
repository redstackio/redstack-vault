---
id: fbf733eb-bb3f-4248-8d50-f22bc7ddd15a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.034520+00:00'
updated_at: '2023-04-10T20:26:23.356429+00:00'
---

# Code Snippet fbf733eb

**Language**: Powershell

```powershell
crackmapexec ldap 10.10.10.10 -u username -p 'Password123' -d 'domain.local' --kdcHost 10.10.10.10 -M MAQ
StandIn.exe --object ms-DS-MachineAccountQuota=*
```
