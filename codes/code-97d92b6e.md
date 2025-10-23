---
id: 97d92b6e-536c-4c31-b6bf-9de9945cfcb8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:03.238836+00:00'
updated_at: '2023-04-10T20:26:35.780565+00:00'
---

# Code Snippet 97d92b6e

**Language**: Powershell

```powershell
smbclient -U username //10.0.0.1/SYSVOL
smbclient //10.0.0.1/Share

# Download a folder recursively
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> lcd '/path/to/go/'
smb: \> mget *
```


