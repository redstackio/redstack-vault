---
id: 3fa71f92-b5d0-4b40-8e63-95d89c15d9f9
name: Command
type: command
executor: bash
data: 'Add-Type -AssemblyName System.IdentityModel; New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken
  -ArgumentList "MSSQLSvc/host.domain.com"

  '
output: null
created_at: '2020-07-14T18:21:07.837558+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Command

```bash
Add-Type -AssemblyName System.IdentityModel; New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "MSSQLSvc/host.domain.com"

```
