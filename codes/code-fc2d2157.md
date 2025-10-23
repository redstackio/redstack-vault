---
id: fc2d2157-1d00-4e3e-bfc0-85c57abb34a6
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:28.232238+00:00'
updated_at: '2023-04-10T20:37:27.909995+00:00'
---

# Code Snippet fc2d2157

**Language**: Powershell

```powershell
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows NT\Terminal Services" /v Shadow /t REG_DWORD /d 4
# 4 – View Session without user’s permission.

# Allowing remote connections to this computer
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f


# Disable UAC remote restriction
reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f

mstsc /v:{ADDRESS} /shadow:{SESSION_ID} /noconsentprompt /prompt
# /v parameter lets specify the {ADDRESS} value that is an IP address or a hostname of a remote host;
# /shadow parameter is used to specify the {SESSION_ID} value that is a shadowee’s session ID;
# /noconsentprompt parameter allows to bypass a shadowee’s permission and shadow their session without their consent;
# /prompt parameter is used to specify a user’s credentials to connect to a remote host.
```


