---
id: 0230cd4e-8507-4faf-9301-4cda4dfb57f5
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:08.524944+00:00'
updated_at: '2023-04-10T20:36:14.405008+00:00'
---

# Code Snippet 0230cd4e

**Language**: Powershell

```powershell
$ ls /tmp/ | grep krb5cc
krb5cc_1000
krb5cc_1569901113
krb5cc_1569901115

$ export KRB5CCNAME=/tmp/krb5cc_1569901115
```
