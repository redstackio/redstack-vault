---
id: 2cb321f2-2c9c-451b-a9ce-37471d29f90c
type: code
language: Powershell
verified: false
created_at: '2023-05-24T20:21:06.335217+00:00'
updated_at: '2023-05-24T20:21:06.595444+00:00'
---

# Code Snippet 2cb321f2

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


