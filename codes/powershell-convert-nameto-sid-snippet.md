---
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:07.242536+00:00'
updated_at: '2023-04-10T20:26:22.637180+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - sid-lookup
validated: true
---

# powershell-convert-nameto-sid-snippet

## Code

```powershell
Convert-NameToSid target.domain.com\krbtgt
```

## Description

This simple PowerShell snippet uses the built-in Convert-NameToSid cmdlet to resolve a domain account to its SID, useful for initial reconnaissance in AD environments or preparing for SID-based attacks like hijacking.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `target.domain.com` | Target domain name | `parent.domain.com` |
| `krbtgt` | Account to resolve | `administrator` |

## Usage

Execute directly in PowerShell on a domain-joined Windows machine with access to the target domain via trust. Output the SID for use in user creation or ticket forging scripts. Integrate into larger automation for AD enumeration.

## Detection

- PowerShell execution logs (Event ID 4104) showing Convert-NameToSid usage.
- Anomalous AD queries from child to parent domains.
- SIEM alerts on SID resolution patterns.

## Related

- [[procedures/sid-hijacking-for-golden-ticket-attack]]
- [[commands/powershell-convert-nameto-sid]]
