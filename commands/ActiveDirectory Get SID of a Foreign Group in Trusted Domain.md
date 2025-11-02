---
id: 9142864f-8f0f-4f85-b586-21ff04aa1f67
name: ActiveDirectory Get SID of a Foreign Group in Trusted Domain
type: command
executor: powershell
data: Get-ADGroup "$_GROUP" -Server "$_REMOTE_DOMAIN_DC"
output: 'PS C:\> Get-ADGroup "Enterprise Admins" -Server "dc-main.bank.local"



  RunspaceId        : 95bdcd5b-75ec-4763-ac5d-adcc32fa4a28

  DistinguishedName : CN=Enterprise Admins,CN=Users,DC=BANK,DC=LOCAL

  GroupCategory     : Security

  GroupScope        : Universal

  Name              : Enterprise Admins

  ObjectClass       : group

  ObjectGUID        : c55a6741-d278-467a-bc62-4ccdeea90fdc

  SamAccountName    : Enterprise Admins

  SID               : S-1-5-21-3428605742-3005092657-1212549955-519'
created_at: '2020-07-01T22:19:32.737990+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[ps]]'
---

# ActiveDirectory Get SID of a Foreign Group in Trusted Domain

```powershell
Get-ADGroup "$_GROUP" -Server "$_REMOTE_DOMAIN_DC"
```

## Expected Output

```
PS C:\> Get-ADGroup "Enterprise Admins" -Server "dc-main.bank.local"


RunspaceId        : 95bdcd5b-75ec-4763-ac5d-adcc32fa4a28
DistinguishedName : CN=Enterprise Admins,CN=Users,DC=BANK,DC=LOCAL
GroupCategory     : Security
GroupScope        : Universal
Name              : Enterprise Admins
ObjectClass       : group
ObjectGUID        : c55a6741-d278-467a-bc62-4ccdeea90fdc
SamAccountName    : Enterprise Admins
SID               : S-1-5-21-3428605742-3005092657-1212549955-519
```


