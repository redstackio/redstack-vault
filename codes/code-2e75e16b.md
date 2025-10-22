---
id: 2e75e16b-f281-4e43-a138-c02a2751bc4a
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.453940+00:00'
updated_at: '2023-04-10T20:36:00.037291+00:00'
---

# Code Snippet 2e75e16b

**Language**: Powershell

```powershell
# From https://github.com/samratashok/ADModule
PS> Get-ADComputer -Filter {TrustedForDelegation -eq $True}
```
