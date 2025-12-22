---
type: code
language: powershell
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tags:
  - command-injection
  - bypass
  - powershell
platforms:
  - Windows
validated: true
---

# PowerShell-Whoami-Double-Quote-Bypass

## Code

```powershell
w"h"o"am"i
```

## Description

This code snippet is a fragmented version of the 'whoami' command, using double quotes to bypass input filters that block the full keyword. When injected into a vulnerable command execution context (e.g., via PowerShell's Invoke-Expression or direct shell), the Windows shell reassembles and executes it as 'whoami', revealing the current user context for reconnaissance.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This is a static payload string; no variables to substitute. Customize by fragmenting other commands similarly (e.g., replace letters for 'net user'). | N/A |

## Usage

Inject this payload into vulnerable inputs that feed into Windows Command Shell or PowerShell, such as web app parameters executed via system() or similar. For testing: `Invoke-Expression 'w"h"o"am"i'`. Used in command injection scenarios to evade WAFs or app-level filters during initial access or discovery phases.

## Detection

- Monitor for anomalous PowerShell executions with fragmented strings containing multiple quotes (e.g., via Event ID 4104 for ScriptBlock logging).
- WAF rules detecting quote-heavy inputs or patterns like letter-quote-letter.
- Process monitoring for 'whoami' executions from unexpected sources like web servers.

## Related

- [[procedures/Command-Injection-with-Double-Quote-Bypass]]
