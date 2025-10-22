---
id: 72ae7f60-eba9-498f-80e6-d78ed8be916b
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.390408+00:00'
updated_at: '2023-05-24T20:18:08.783896+00:00'
---

# Code Snippet 72ae7f60

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
