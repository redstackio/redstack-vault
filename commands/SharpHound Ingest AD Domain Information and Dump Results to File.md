---
id: c7f78e78-40b6-4eb9-b292-a59d1329a88e
name: SharpHound Ingest AD Domain Information and Dump Results to File
type: command
executor: command_prompt
data: SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD
output: 'PS C:\Windows\Tasks\> .\SharpHound.exe -c All -d megabank.local --ldapusername bob --ldappassword s3cr3tPASS

  -----------------------------------------------

  Initializing SharpHound at 4:16 PM on 3/15/2020

  -----------------------------------------------


  Resolved Collection Methods: Group, Sessions, LoggedOn, Trusts, ACL, ObjectProps,
  LocalGroups, SPNTargets, Container


  [+] Creating Schema map for domain MEGABANK.LOCAL using path CN=Schema,CN=Configuration,DC=MEGABANK,DC=LOCAL

  [+] Cache File not Found: 0 Objects in cache


  [+] Pre-populating Domain Controller SIDS

  Status: 0 objects finished (+0) -- Using 30 MB RAM

  Status: 123 objects finished (+123 61.5)/s -- Using 38 MB RAM

  Enumeration finished in 00:00:02.4653677

  Compressing data to .\20200315161607_BloodHound.zip

  You can upload this file directly to the UI


  SharpHound Enumeration Completed at 4:16 PM on 3/15/2020! Happy Graphing!'
created_at: '2020-03-15T23:15:05.164898+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SharpHound Ingest AD Domain Information and Dump Results to File

```command_prompt
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD
```

## Expected Output

```
PS C:\Windows\Tasks\> .\SharpHound.exe -c All -d megabank.local --ldapusername bob --ldappassword s3cr3tPASS
-----------------------------------------------
Initializing SharpHound at 4:16 PM on 3/15/2020
-----------------------------------------------

Resolved Collection Methods: Group, Sessions, LoggedOn, Trusts, ACL, ObjectProps, LocalGroups, SPNTargets, Container

[+] Creating Schema map for domain MEGABANK.LOCAL using path CN=Schema,CN=Configuration,DC=MEGABANK,DC=LOCAL
[+] Cache File not Found: 0 Objects in cache

[+] Pre-populating Domain Controller SIDS
Status: 0 objects finished (+0) -- Using 30 MB RAM
Status: 123 objects finished (+123 61.5)/s -- Using 38 MB RAM
Enumeration finished in 00:00:02.4653677
Compressing data to .\20200315161607_BloodHound.zip
You can upload this file directly to the UI

SharpHound Enumeration Completed at 4:16 PM on 3/15/2020! Happy Graphing!
```


