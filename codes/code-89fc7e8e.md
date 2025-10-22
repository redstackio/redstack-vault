---
id: 89fc7e8e-c5ad-4937-a144-c6bc8d62aa44
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.771746+00:00'
updated_at: '2023-04-06T03:56:07.771746+00:00'
---

# Code Snippet 89fc7e8e

**Language**: Powershell

```powershell
Rubeus.exe hash /password:'Weakest123*' /user:swktest$  /domain:factory.lan
[*] Input password             : Weakest123*
[*] Input username             : swktest$
[*] Input domain               : factory.lan
[*] Salt                       : FACTORY.LANswktest
[*]       rc4_hmac             : F8E064CA98539B735600714A1F1907DD
[*]       aes128_cts_hmac_sha1 : D45DEADECB703CFE3774F2AA20DB9498
[*]       aes256_cts_hmac_sha1 : 0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347
[*]       des_cbc_md5          : BA297CFD07E62A5E
```
