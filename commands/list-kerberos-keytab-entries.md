---
id: 5953c79b-aca4-4268-a6a3-4ab533ea2d2b
name: list-kerberos-keytab-entries
type: command
executor: powershell
data: 'klist -t -K -e -k FILE:$_KEYTAB_PATH'
output: null
created_at: '2023-04-06T03:56:08.671054+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# list-kerberos-keytab-entries

## Command

```powershell
klist -t -K -e -k FILE:$_KEYTAB_PATH
```

## Description

Lists all service principal entries, keys, encryption types, and timestamps from a Kerberos keytab file. Useful for initial reconnaissance of available credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KEYTAB_PATH | Full path to the keytab file (e.g., C:\Users\User\downloads\krb5.keytab) | Yes |
| -t | Display timestamps | Built-in |
| -K | Show keys | Built-in |
| -e | Show encryption types | Built-in |
| -k | Specify keytab file | Built-in |

## Examples

### Basic Usage

```powershell
klist -t -K -e -k FILE:C:\Users\User\downloads\krb5.keytab
```

### Advanced Usage

On Linux equivalent, use `ktutil -k /etc/krb5.keytab list` for similar output.

## Expected Output

```
[26] Service principal: host/COMPUTER@DOMAIN
     KVNO: 25
     Key type: 23
     Key: 31d6cfe0d16ae931b73c59d7e0c089c0
     Time stamp: Oct 07,  2019 09:12:02
```

Lists principals, KVNO, key types (e.g., 23 for RC4-HMAC), keys, and timestamps.

## Related

- [[procedures/Extract-Service-Principal-Keys-from-Keytab]]
