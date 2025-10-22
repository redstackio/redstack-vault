---
id: e0dc72e2-10cb-4f34-abe5-f73d891a95a1
name: Enumerate GenericAll rights on AD Object
type: command
executor: ''
data: Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights
  -eq "GenericAll"}
output: '(...)

  IdentityReference: DOMAIN\User

  ActiveDirectoryRights: GenericAll

  (...)'
created_at: '2023-01-12T18:36:32.650238+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Enumerate GenericAll rights on AD Object

```bash
Get-ObjectAcl -SamAccountName $USERNAME -ResolveGUIDs | ? {$_.ActiveDirectoryRights -eq "GenericAll"}
```

## Expected Output

```
(...)
IdentityReference: DOMAIN\User
ActiveDirectoryRights: GenericAll
(...)
```
