---
id: 6f8d4da6-59ab-4baf-8d26-963f146a239a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:02.526477+00:00'
updated_at: '2023-04-10T20:26:38.483967+00:00'
---

# Code Snippet 6f8d4da6

**Language**: ps1

```ps1
nslookup domain.com
nslookup -type=srv _ldap._tcp.dc._msdcs.<domain>.com
nltest /dclist:domain.com
Get-ADDomainController -filter * | Select-Object name
gpresult /r
$Env:LOGONSERVER 
echo %LOGONSERVER%
```


