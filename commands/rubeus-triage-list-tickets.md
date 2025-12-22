---
type: command
executor: cmd
data: Rubeus.exe triage
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - credential-access
verified: true
validated: true
---

# rubeus-triage-list-tickets

## Command

```cmd
Rubeus.exe triage
```

## Description

This command uses Rubeus to perform a triage of all Kerberos tickets in the current logon session, listing details like user accounts, services, LUIDs, and encryption types without exporting them.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| triage | Flag to enumerate and display cached tickets | Yes |

## Examples

### Basic Usage

```cmd
Rubeus.exe triage
```

### Specify User Session

```cmd
Rubeus.exe triage /user:DOMAIN\username
```

## Expected Output

A table of tickets similar to:

User: DOMAIN\user
Service: krbtgt/DOMAIN.LOCAL
LUID: 0x12d1f7
Enc Type: AES256

## Related

- [[procedures/Dump-Kerberos-Tickets]]
- [[tools/Rubeus]]
