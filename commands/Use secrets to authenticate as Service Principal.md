---
id: c4db6739-7970-4c2b-8ed6-34e76b103d08
name: Use secrets to authenticate as Service Principal
type: command
executor: bash
data: 'PS > $password = ConvertTo-SecureString ''<SECRET/PASSWORD>'' -AsPlainText
  -Force

  PS > $creds = New-Object System.Management.Automation.PSCredential(''<AppID>'',
  $password)

  PS > Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant ''<TenantID>'''
output: null
created_at: '2023-05-24T20:21:06.337686+00:00'
updated_at: '2023-05-24T20:21:06.612131+00:00'
---

# Use secrets to authenticate as Service Principal

```bash
PS > $password = ConvertTo-SecureString '<SECRET/PASSWORD>' -AsPlainText -Force
PS > $creds = New-Object System.Management.Automation.PSCredential('<AppID>', $password)
PS > Connect-AzAccount -ServicePrincipal -Credential $creds -Tenant '<TenantID>'
```


