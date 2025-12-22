---
id: 279d8f09-7a4e-4cd4-9f56-1d05e66beb01
name: rubeus-obtain-tgt-hash
type: command
executor: powershell
data: >-
  .\Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$
  /password:'iUAL)l<i$;UzD7W'
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - ticket
verified: true
validated: true
---

# rubeus-obtain-tgt-hash

## Command

```powershell
.\Rubeus.exe hash /domain:purple.lab /user:WVLFLLKZ$ /password:'iUAL)l<i$;UzD7W'
```

## Description

Obtains a TGT using NTLM hash or password for the specified user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /domain:purple.lab | Target domain | Yes |
| /user:WVLFLLKZ$ | Username | Yes |
| /password:'iUAL)l<i$;UzD7W' | Password | Yes |

## Examples

### Basic Usage

```powershell
.\Rubeus.exe hash /domain:example.com /user:test$ /password:'pass123'
```

## Expected Output

[TGT] Ticket generated, base64 encoded.

## Related

- [[procedures/WebDAV-Relay-Attack]]
