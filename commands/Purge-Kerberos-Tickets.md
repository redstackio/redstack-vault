---
id: 6e364f1c-f70c-4c80-b25c-ad959078b8cd
name: Purge-Kerberos-Tickets
type: command
executor: powershell
data: 'kerberos::purge'
output: null
created_at: '2023-04-06T03:56:28.444637+00:00'
updated_at: '2023-04-10T20:37:25.781492+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - ticket-management
verified: true
validated: true
---

# Purge-Kerberos-Tickets

## Command

```powershell
kerberos::purge
```

## Description

This command purges all Kerberos tickets from the current user's session cache, clearing any existing TGTs or service tickets. It is used to reset the authentication state before injecting forged tickets like Golden Tickets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; clears all tickets in the session | N/A |

## Examples

### Basic Usage

```powershell
kerberos::purge
```

Run this in a PowerShell session on a domain-joined Windows machine with Rubeus loaded.

### Verification After Purge

```powershell
klist
```

This should show no tickets listed.

## Expected Output

Typically no output on success, or a confirmation message like "[*] Action: Purging tickets...". If errors occur (e.g., no tickets present), it may state "No tickets found to purge."

## Related

- [[procedures/Golden-Ticket-Creation-via-Kerberos-Purge]]
- [[tools/Rubeus]]
