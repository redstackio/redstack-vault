---
id: 0d3d3f39-2c9c-4855-83f0-42fedc66e956
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.229545+00:00'
updated_at: '2023-04-06T21:33:38.760126+00:00'
---

# Code Snippet 0d3d3f39

**Language**: Powershell

```powershell
Get-NetGroupMember -GroupName "<GroupName>" -Domain <DomainName>

#Enumerate the members of a specified group of the domain
Get-DomainGroup -Identity <GroupName> | Select-Object -ExpandProperty Member

#Returns all GPOs in a domain that modify local group memberships through Restricted Groups or Group Policy Preferences
Get-DomainGPOLocalGroup | Select-Object GPODisplayName, GroupName
```
