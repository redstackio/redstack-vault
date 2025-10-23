---
id: df19ec68-5d8f-4ed0-a346-f6c48255826c
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:24.119983+00:00'
updated_at: '2023-04-10T20:37:01.479470+00:00'
---

# Code Snippet df19ec68

**Language**: ps1

```ps1
$pass = "01000000d08c9ddf0115d1118c7a00c04fc297eb01000000e4a07bc7aaeade47925c42c8be5870730000000002000000000003660000c000000010000000d792a6f34a55235c22da98b0c041ce7b0000000004800000a00000001000000065d20f0b4ba5367e53498f0209a3319420000000d4769a161c2794e19fcefff3e9c763bb3a8790deebf51fc51062843b5d52e40214000000ac62dab09371dc4dbfd763fea92b9d5444748692" | convertto-securestring
$user = "HTB\Tom"
$cred = New-Object System.management.Automation.PSCredential($user, $pass)
$cred.GetNetworkCredential() | fl

```


