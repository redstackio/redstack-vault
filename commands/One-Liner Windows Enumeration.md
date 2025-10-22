---
id: 9e86415a-6321-4a1b-a104-fb7f5080a4a0
name: One-Liner Windows Enumeration
type: command
executor: bash
data: 'whoami & hostname & ipconfig /all & net user /domain 2>&1 & net group /domain
  2>&1 & net group "domain admins" /domain 2>&1 & net group "Exchange Trusted Subsystem"
  /domain 2>&1 & net accounts /domain 2>&1 & net user 2>&1 & net localgroup administrators
  2>&1 & netstat -an 2>&1 & tasklist 2>&1 & sc query 2>&1 & systeminfo 2>&1 & reg
  query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" 2>&1
  & net view & net view /domain & net user %USERNAME% /domain & nltest /dclist & gpresult
  /z

  '
output: null
created_at: '2020-07-14T18:21:27.748164+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# One-Liner Windows Enumeration

```bash
whoami & hostname & ipconfig /all & net user /domain 2>&1 & net group /domain 2>&1 & net group "domain admins" /domain 2>&1 & net group "Exchange Trusted Subsystem" /domain 2>&1 & net accounts /domain 2>&1 & net user 2>&1 & net localgroup administrators 2>&1 & netstat -an 2>&1 & tasklist 2>&1 & sc query 2>&1 & systeminfo 2>&1 & reg query "HKEY_CURRENT_USER\Software\Microsoft\Terminal Server Client\Default" 2>&1 & net view & net view /domain & net user %USERNAME% /domain & nltest /dclist & gpresult /z

```
