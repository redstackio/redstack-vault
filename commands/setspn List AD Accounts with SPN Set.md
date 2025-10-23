---
id: 2b41d1b0-52a2-4f92-a8eb-d2e5f810990a
name: setspn List AD Accounts with SPN Set
type: command
executor: command_prompt
data: setspn.exe -T $_DOMAIN -Q */*
output: "PS C:\\> setspn.exe -T dev.tesla.local -Q */*\nChecking domain DC=DEV,DC=TESLA,DC=LOCAL\n\
  CN=krbtgt,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL\n        kadmin/changepw\nCN=svc-mssql,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL\n\
  \        WS01/svc-mssql.DEV.TESLA.LOCAL:60111\nCN=WS01,CN=Computers,DC=DEV,DC=TESLA,DC=LOCAL\n\
  \        WSMAN/WS01\n        WSMAN/WS01.DEV.TESLA.LOCAL\n        RestrictedKrbHost/WS01\n\
  \        HOST/WS01\n        RestrictedKrbHost/WS01.DEV.TESLA.LOCAL\n        HOST/WS01.DEV.TESLA.LOCAL\n\
  CN=DC-DEV,OU=Domain Controllers,DC=DEV,DC=TESLA,DC=LOCAL\n        ldap/DC-DEV.DEV.TESLA.LOCAL/ForestDnsZones.TESLA.LOCAL\n\
  \        Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/DC-DEV.DEV.TESLA.LOCAL\n    \
  \    DNS/DC-DEV.DEV.TESLA.LOCAL\n        GC/DC-DEV.DEV.TESLA.LOCAL/TESLA.LOCAL\n\
  \        RestrictedKrbHost/DC-DEV.DEV.TESLA.LOCAL\n        RestrictedKrbHost/DC-DEV\n\
  \        RPC/c3a77e68-53c8-414e-9f29-a218c2f9e887._msdcs.TESLA.LOCAL\n        HOST/DC-DEV/DEV\n\
  \        HOST/DC-DEV.DEV.TESLA.LOCAL/DEV\n        HOST/DC-DEV\n        HOST/DC-DEV.DEV.TESLA.LOCAL\n\
  \        HOST/DC-DEV.DEV.TESLA.LOCAL/DEV.TESLA.LOCAL\n        E3514235-4B06-11D1-AB04-00C04FC2DCD2/c3a77e68-53c8-414e-9f29-a218c2f9e887/DEV.TESLA.LOCAL\n\
  \        ldap/DC-DEV/DEV\n        ldap/c3a77e68-53c8-414e-9f29-a218c2f9e887._msdcs.TESLA.LOCAL\n\
  \        ldap/DC-DEV.DEV.TESLA.LOCAL/DEV\n        ldap/DC-DEV\n        ldap/DC-DEV.DEV.TESLA.LOCAL\n\
  \        ldap/DC-DEV.DEV.TESLA.LOCAL/DEV.TESLA.LOCAL"
created_at: '2020-07-01T22:19:32.737391+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# setspn List AD Accounts with SPN Set

```command_prompt
setspn.exe -T $_DOMAIN -Q */*
```

## Expected Output

```
PS C:\> setspn.exe -T dev.tesla.local -Q */*
Checking domain DC=DEV,DC=TESLA,DC=LOCAL
CN=krbtgt,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
        kadmin/changepw
CN=svc-mssql,CN=Users,DC=DEV,DC=TESLA,DC=LOCAL
        WS01/svc-mssql.DEV.TESLA.LOCAL:60111
CN=WS01,CN=Computers,DC=DEV,DC=TESLA,DC=LOCAL
        WSMAN/WS01
        WSMAN/WS01.DEV.TESLA.LOCAL
        RestrictedKrbHost/WS01
        HOST/WS01
        RestrictedKrbHost/WS01.DEV.TESLA.LOCAL
        HOST/WS01.DEV.TESLA.LOCAL
CN=DC-DEV,OU=Domain Controllers,DC=DEV,DC=TESLA,DC=LOCAL
        ldap/DC-DEV.DEV.TESLA.LOCAL/ForestDnsZones.TESLA.LOCAL
        Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/DC-DEV.DEV.TESLA.LOCAL
        DNS/DC-DEV.DEV.TESLA.LOCAL
        GC/DC-DEV.DEV.TESLA.LOCAL/TESLA.LOCAL
        RestrictedKrbHost/DC-DEV.DEV.TESLA.LOCAL
        RestrictedKrbHost/DC-DEV
        RPC/c3a77e68-53c8-414e-9f29-a218c2f9e887._msdcs.TESLA.LOCAL
        HOST/DC-DEV/DEV
        HOST/DC-DEV.DEV.TESLA.LOCAL/DEV
        HOST/DC-DEV
        HOST/DC-DEV.DEV.TESLA.LOCAL
        HOST/DC-DEV.DEV.TESLA.LOCAL/DEV.TESLA.LOCAL
        E3514235-4B06-11D1-AB04-00C04FC2DCD2/c3a77e68-53c8-414e-9f29-a218c2f9e887/DEV.TESLA.LOCAL
        ldap/DC-DEV/DEV
        ldap/c3a77e68-53c8-414e-9f29-a218c2f9e887._msdcs.TESLA.LOCAL
        ldap/DC-DEV.DEV.TESLA.LOCAL/DEV
        ldap/DC-DEV
        ldap/DC-DEV.DEV.TESLA.LOCAL
        ldap/DC-DEV.DEV.TESLA.LOCAL/DEV.TESLA.LOCAL
```


