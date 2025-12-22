---
type: command
executor: powershell
data: >-
  Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT',
  'AES128-CTS-HMAC-SHA1-96'
tags:
  - kerberos
  - encryption
platforms:
  - Windows
verified: true
validated: true
---

# powershell-set-aduser-kerberos-encryption-type

## Command

```powershell
Set-ADUser -Identity $_USERNAME -KerberosEncryptionType $_ENC_TYPES
```

## Description

Configures Kerberos encryption types for a user account to ensure compatibility with domain policies during ticket requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_USERNAME | Username to update | Yes |
| -KerberosEncryptionType $_ENC_TYPES | Encryption types (e.g., 'RC4-HMAC-NT', 'AES128-CTS-HMAC-SHA1-96') | Yes |

## Examples

### Basic Usage

```powershell
Set-ADUser -Identity 'User1' -KerberosEncryptionType 'RC4-HMAC-NT'
```

## Expected Output

No output on success.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
