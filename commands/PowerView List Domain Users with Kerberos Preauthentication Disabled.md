---
id: 6a6ccc53-b2f8-4f59-a7b0-8f0809643fe5
name: PowerView List Domain Users with Kerberos Preauthentication Disabled
type: command
executor: powershell
data: Get-DomainUser -PreauthNotRequired
output: 'PS C:\Users\steve> Get-DomainUser -PreauthNotRequired



  logoncount                    : 0

  badpasswordtime               : 12/31/1600 4:00:00 PM

  distinguishedname             : CN=svc-appsrv,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL

  objectclass                   : {top, person, organizationalPerson, user}

  name                          : svc-appsrv

  objectsid                     : S-1-5-21-1576920733-1301476157-954876328-1109

  samaccountname                : svc-appsrv

  codepage                      : 0

  samaccounttype                : USER_OBJECT

  accountexpires                : 12/31/1600 4:00:00 PM

  countrycode                   : 0

  whenchanged                   : 7/1/2020 10:52:12 PM

  instancetype                  : 4

  usncreated                    : 13133

  objectguid                    : c781954d-22ec-457e-b434-d00aa3174952

  lastlogoff                    : 12/31/1600 4:00:00 PM

  objectcategory                : CN=Person,CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL

  dscorepropagationdata         : 1/1/1601 12:00:00 AM

  lastlogon                     : 12/31/1600 4:00:00 PM

  badpwdcount                   : 0

  cn                            : svc-appsrv

  useraccountcontrol            : NORMAL_ACCOUNT, DONT_REQ_PREAUTH

  whencreated                   : 7/1/2020 10:51:59 PM

  primarygroupid                : 513

  pwdlastset                    : 7/1/2020 3:51:59 PM

  msds-supportedencryptiontypes : 0

  usnchanged                    : 13137'
created_at: '2020-07-01T22:54:44.509214+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PowerView List Domain Users with Kerberos Preauthentication Disabled

```powershell
Get-DomainUser -PreauthNotRequired
```

## Expected Output

```
PS C:\Users\steve> Get-DomainUser -PreauthNotRequired


logoncount                    : 0
badpasswordtime               : 12/31/1600 4:00:00 PM
distinguishedname             : CN=svc-appsrv,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
objectclass                   : {top, person, organizationalPerson, user}
name                          : svc-appsrv
objectsid                     : S-1-5-21-1576920733-1301476157-954876328-1109
samaccountname                : svc-appsrv
codepage                      : 0
samaccounttype                : USER_OBJECT
accountexpires                : 12/31/1600 4:00:00 PM
countrycode                   : 0
whenchanged                   : 7/1/2020 10:52:12 PM
instancetype                  : 4
usncreated                    : 13133
objectguid                    : c781954d-22ec-457e-b434-d00aa3174952
lastlogoff                    : 12/31/1600 4:00:00 PM
objectcategory                : CN=Person,CN=Schema,CN=Configuration,DC=TESLA,DC=LOCAL
dscorepropagationdata         : 1/1/1601 12:00:00 AM
lastlogon                     : 12/31/1600 4:00:00 PM
badpwdcount                   : 0
cn                            : svc-appsrv
useraccountcontrol            : NORMAL_ACCOUNT, DONT_REQ_PREAUTH
whencreated                   : 7/1/2020 10:51:59 PM
primarygroupid                : 513
pwdlastset                    : 7/1/2020 3:51:59 PM
msds-supportedencryptiontypes : 0
usnchanged                    : 13137
```


