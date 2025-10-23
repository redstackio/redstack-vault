---
id: 4081dbfa-d614-4fb1-8972-8374c08927cd
name: ActiveDirectory Get SIDs of Trusted Domains
type: command
executor: powershell
data: (Get-ADForest).Domains| %{Get-ADDomain -Server $_}|select name, domainsid
output: 'PS C:\> (Get-ADForest).Domains| %{Get-ADDomain -Server $_}|select name, domainsid


  Name  DomainSID

  ----  ---------

  DEV   S-1-5-21-1576920733-1301476157-954876328

  BANK S-1-5-21-3428605742-3005092657-1212549955'
created_at: '2020-07-01T22:19:32.737787+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# ActiveDirectory Get SIDs of Trusted Domains

```powershell
(Get-ADForest).Domains| %{Get-ADDomain -Server $_}|select name, domainsid
```

## Expected Output

```
PS C:\> (Get-ADForest).Domains| %{Get-ADDomain -Server $_}|select name, domainsid

Name  DomainSID
----  ---------
DEV   S-1-5-21-1576920733-1301476157-954876328
BANK S-1-5-21-3428605742-3005092657-1212549955
```


