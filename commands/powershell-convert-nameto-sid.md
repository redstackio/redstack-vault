---
type: command
executor: powershell
data: Convert-NameToSid 'parent.domain.com\\krbtgt'
output: null
created_at: '2023-04-06T03:56:07.242700+00:00'
updated_at: '2023-04-10T20:26:22.640650+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - sid-lookup
verified: true
validated: true
---

# powershell-convert-nameto-sid

## Command

```powershell
Convert-NameToSid '$_DOMAIN\\$_ACCOUNT'
```

## Description

This PowerShell cmdlet resolves a domain account (user or group) to its Security Identifier (SID) via Active Directory queries. Use it in cross-domain scenarios to obtain parent domain SIDs from a child domain context, enabling SID hijacking attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_DOMAIN` | Target domain in format domain.com (e.g., parent.domain.com) | Yes |
| `$_ACCOUNT` | Account name to resolve (e.g., krbtgt, administrator) | Yes |

## Examples

### Basic Usage

```powershell
Convert-NameToSid 'parent.domain.com\\krbtgt'
```

### Advanced Usage

```powershell
Convert-NameToSid 'parent.domain.com\\Domain Admins'
```

## Expected Output

```
S-1-5-21-2941561648-383941485-1389968811-502
```

A single line with the full SID string. Errors if account doesn't exist or no trust access.

## Related

- [[procedures/sid-hijacking-for-golden-ticket-attack]]
