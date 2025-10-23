---
id: 2604fd6c-a900-4b8d-8549-3d260fa9acbc
type: code
language: Powershell
verified: false
created_at: '2023-05-24T20:18:59.344545+00:00'
updated_at: '2023-05-24T20:19:54.196627+00:00'
---

# Code Snippet 2604fd6c

**Language**: Powershell

```powershell
# Add secrets
PS > . C:\Tools\Add-AzADAppSecret.ps1
PS > Add-AzADAppSecret -GraphToken $graphtoken -Verbose

# Use secrets to authenticate as Service Principal
PS > $password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force
PS > $creds = New-Object System.Management.Automation.PSCredential('<AppID>', $password)
PS > Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
```


