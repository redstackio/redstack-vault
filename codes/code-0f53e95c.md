---
id: 0f53e95c-9a79-4aa6-94a0-68fbc4d139a6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.918701+00:00'
updated_at: '2023-04-10T20:19:39.403175+00:00'
---

# Code Snippet 0f53e95c

**Language**: Powershell

```powershell
# Enumerate application that have Proxy
PS C:\Tools> Get-AzureADApplication -All $true | %{try{GetAzureADApplicationProxyApplication -ObjectId $_.ObjectID;$_.DisplayName;$_.ObjectID}catch{}}
PS C:\Tools> Get-AzureADServicePrincipal -All $true | ?{$_.DisplayName -eq "Finance Management System"}
PS C:\Tools> . C:\Tools\GetApplicationProxyAssignedUsersAndGroups.ps1
PS C:\Tools> Get-ApplicationProxyAssignedUsersAndGroups -ObjectId <OBJECT-ID>
```
