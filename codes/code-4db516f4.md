---
id: 4db516f4-192e-4b09-ad89-d9f14aa9c09d
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:31.279075+00:00'
updated_at: '2023-04-10T20:38:00.046573+00:00'
---

# Code Snippet 4db516f4

**Language**: ps1

```ps1
cp user.ccache /tmp/krb5cc_1045
ssh -o GSSAPIAuthentication=yes user@domain.local -vv
```
