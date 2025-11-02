---
id: 61c888bd-566b-44a3-877b-6c1e391671a9
name: PowerView List AD Accounts with SPN Set
type: command
executor: powershell
data: Get-DomainUser -SPN
output: 'PS C:\Users\steve> Get-DomainUser -SPN


  logoncount            : 0

  badpasswordtime       : 12/31/1600 4:00:00 PM

  distinguishedname     : CN=svc-mssql,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  objectclass           : {top, person, organizationalPerson, user}

  name                  : svc-mssql

  objectsid             : S-1-5-21-1576920733-1301476157-954876328-1108

  samaccountname        : svc-mssql

  codepage              : 0

  samaccounttype        : USER_OBJECT

  accountexpires        : 12/31/1600 4:00:00 PM

  countrycode           : 0

  whenchanged           : 7/1/2020 10:13:53 PM

  instancetype          : 4

  objectguid            : 9b4e2061-5f6c-4cce-a26e-9fcd5bcbf0e3

  lastlogon             : 12/31/1600 4:00:00 PM

  lastlogoff            : 12/31/1600 4:00:00 PM

  objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL

  dscorepropagationdata : 1/1/1601 12:00:00 AM

  serviceprincipalname  : WS01/svc-mssql.DEV.TESLA.LOCAL:60111

  whencreated           : 7/1/2020 10:13:01 PM

  badpwdcount           : 0

  cn                    : svc-mssql

  useraccountcontrol    : NORMAL_ACCOUNT

  usncreated            : 13113

  primarygroupid        : 513

  pwdlastset            : 7/1/2020 3:13:01 PM

  usnchanged            : 13117

  ...'
created_at: '2020-07-01T22:54:44.508711+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[PowerView]]'
- '[[SET]]'
- '[[ps]]'
---

# PowerView List AD Accounts with SPN Set

```powershell
Get-DomainUser -SPN
```

## Expected Output

```
PS C:\Users\steve> Get-DomainUser -SPN

logoncount            : 0
badpasswordtime       : 12/31/1600 4:00:00 PM
distinguishedname     : CN=svc-mssql,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
objectclass           : {top, person, organizationalPerson, user}
name                  : svc-mssql
objectsid             : S-1-5-21-1576920733-1301476157-954876328-1108
samaccountname        : svc-mssql
codepage              : 0
samaccounttype        : USER_OBJECT
accountexpires        : 12/31/1600 4:00:00 PM
countrycode           : 0
whenchanged           : 7/1/2020 10:13:53 PM
instancetype          : 4
objectguid            : 9b4e2061-5f6c-4cce-a26e-9fcd5bcbf0e3
lastlogon             : 12/31/1600 4:00:00 PM
lastlogoff            : 12/31/1600 4:00:00 PM
objectcategory        : CN=Person,CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL
dscorepropagationdata : 1/1/1601 12:00:00 AM
serviceprincipalname  : WS01/svc-mssql.DEV.TESLA.LOCAL:60111
whencreated           : 7/1/2020 10:13:01 PM
badpwdcount           : 0
cn                    : svc-mssql
useraccountcontrol    : NORMAL_ACCOUNT
usncreated            : 13113
primarygroupid        : 513
pwdlastset            : 7/1/2020 3:13:01 PM
usnchanged            : 13117
...
```


