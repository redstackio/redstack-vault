---
id: db892aee-e4c4-47c6-b80f-c41963c124ea
name: Dump DNS Zones from Active Directory
type: command
executor: bash
data: adidnsdump -u DOMAIN\\user --print-zones dc.domain.corp --dns-tcp
output: null
created_at: '2023-04-06T03:56:06.634632+00:00'
updated_at: '2023-04-10T20:26:13.842619+00:00'
---

# Dump DNS Zones from Active Directory

```bash
adidnsdump -u DOMAIN\\user --print-zones dc.domain.corp --dns-tcp
```
