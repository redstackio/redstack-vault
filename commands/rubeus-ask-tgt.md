---
type: command
executor: powershell
data: >-
  Rubeus.exe asktgt /user:$_USER /password:$_PASSWORD [/enctype:$_ENCTYPE]
  [/domain:$_DOMAIN] [/dc:$_DOMAIN_CONTROLLER] [/ptt] [/luid]
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - ticket-granting
verified: true
validated: true
---

# rubeus-ask-tgt

## Command

```powershell
Rubeus.exe asktgt /user:$_USER /password:$_PASSWORD [/enctype:$_ENCTYPE] [/domain:$_DOMAIN] [/dc:$_DOMAIN_CONTROLLER] [/ptt] [/luid]
```

## Description

Requests a TGT using provided credentials or hashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /user:$_USER | Username | Yes |
| /password:$_PASSWORD | Password or hash | Yes |
| [/enctype:$_ENCTYPE] | Encryption type (RC4, AES) | No |
| [/domain:$_DOMAIN] | Domain | No |
| [/dc:$_DOMAIN_CONTROLLER] | DC | No |
| [/ptt] | Pass-the-ticket inject | No |
| [/luid] | LUID | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe asktgt /user:attacker /password:Pass123 /domain:example.com /ptt
```

## Expected Output

"TGT request successful" and injected ticket.

## Related

- [[tools/Rubeus]]
