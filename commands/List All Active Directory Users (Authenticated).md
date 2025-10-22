---
id: fb6ad137-2f98-48ff-b799-d84df4f4e934
name: List All Active Directory Users (Authenticated)
type: command
executor: bash
data: GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
output: "root@kali:~# GetADUsers.py 'host.domain/DomainUser:secretpassword' -dc-ip\
  \ 10.10.10.10 -all \nImpacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation\n\
  \n[*] Querying 10.10.10.10 for information about domain.\nName                 \
  \ Email                           PasswordLastSet      LastLogon           \n--------------------\
  \  ------------------------------  -------------------  -------------------\nAdministrator\
  \                                         2018-07-18 15:06:40.351723  2018-07-30\
  \ 13:17:40.656520 \nGuest                                                 <never>\
  \              <never>             \nkrbtgt                                    \
  \            2018-07-18 14:50:36.972031  <never>             \nDomainUser      \
  \                                         2018-07-18 16:14:38.402764  2018-07-21\
  \ 10:01:30.320277"
created_at: '2019-12-04T19:07:19.054377+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# List All Active Directory Users (Authenticated)

```bash
GetADUsers.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -all
```

## Expected Output

```
root@kali:~# GetADUsers.py 'host.domain/DomainUser:secretpassword' -dc-ip 10.10.10.10 -all 
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[*] Querying 10.10.10.10 for information about domain.
Name                  Email                           PasswordLastSet      LastLogon           
--------------------  ------------------------------  -------------------  -------------------
Administrator                                         2018-07-18 15:06:40.351723  2018-07-30 13:17:40.656520 
Guest                                                 <never>              <never>             
krbtgt                                                2018-07-18 14:50:36.972031  <never>             
DomainUser                                               2018-07-18 16:14:38.402764  2018-07-21 10:01:30.320277
```
