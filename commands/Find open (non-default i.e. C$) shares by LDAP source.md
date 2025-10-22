---
id: 4bf5f74e-b243-4368-94ea-a823f4487f89
name: Find open (non-default i.e. C$) shares by LDAP source
type: command
executor: bash
data: 'Invoke-ShareFinder -ComputerADSPath "LDAP://OU=Servers,OU=IT,DC=domain,DC=com"
  -CheckShareAccess -ExcludeStandard | Out-File -Encoding ascii c:\windows\temp\server_shares.txt
  Invoke-ShareFinder -ExcludePrint -ExcludeIPC -CheckShareAccess

  '
output: null
created_at: '2020-07-14T18:21:07.165578+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Find open (non-default i.e. C$) shares by LDAP source

```bash
Invoke-ShareFinder -ComputerADSPath "LDAP://OU=Servers,OU=IT,DC=domain,DC=com" -CheckShareAccess -ExcludeStandard | Out-File -Encoding ascii c:\windows\temp\server_shares.txt Invoke-ShareFinder -ExcludePrint -ExcludeIPC -CheckShareAccess

```
