---
id: e6da6fba-3f43-4dbd-b186-d12805e6b35d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:02.228913+00:00'
updated_at: '2023-04-06T21:33:38.760126+00:00'
---

# Code Snippet e6da6fba

**Language**: Powershell

```powershell
Get-NetUser
Get-NetUser -SamAccountName <user> 
Get-NetUser | select cn
Get-UserProperty

#Check last password change
Get-UserProperty -Properties pwdlastset

#Get a specific "string" on a user's attribute
Find-UserField -SearchField Description -SearchTerm "wtver"

#Enumerate user logged on a machine
Get-NetLoggedon -ComputerName <ComputerName>

#Enumerate Session Information for a machine
Get-NetSession -ComputerName <ComputerName>

#Enumerate domain machines of the current/specified domain where specific users are logged into
Find-DomainUserLocation -Domain <DomainName> | Select-Object UserName, SessionFromName
```


