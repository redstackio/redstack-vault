---
id: a4dd141f-c210-4e1a-b238-1112bde5e936
name: powershell-clear-scriptblock-signatures-cache
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:25.973740+00:00'
updated_at: '2023-04-10T20:36:17.635844+00:00'
platforms:
  - Windows
tags:
  - powershell
  - defense-evasion
  - signature-clearing
validated: true
---

# powershell-clear-scriptblock-signatures-cache

## Code

```powershell
[Ref].Assembly.GetType("System.Management.Automation.ScriptBlock").GetField("signatures","NonPublic,static").SetValue($null, (New-Object 'System.Collections.Generic.HashSet[string]'))
```

## Description

This PowerShell code snippet clears the internal signatures cache used by ScriptBlock objects to store verified script hashes. By resetting it to an empty HashSet via reflection, it removes any cached verifications of previously executed scripts, forcing re-verification on subsequent runs and erasing forensic evidence. Use this after executing malicious scripts to cover tracks in memory without affecting disk-based logs.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | This code has no variables or parameters; it directly targets the static signatures field. | N/A |

## Usage

Execute this code in a PowerShell session immediately after running potentially logged scripts, especially in conjunction with disabling ScriptBlock logging. It can be delivered via remote execution tools like Invoke-Command or embedded in a larger post-exploitation script. Ideal for maintaining persistence by periodically clearing caches during long-term operations.

## Detection

- Monitor PowerShell process for reflection API calls (e.g., GetType, GetField) using ETW tracing or Sysmon Event ID 1 with suspicious DLL loads.
- Check for anomalous empty HashSet creations in PowerShell internals via advanced logging (Module Logging enabled).
- Behavioral detection: Look for scripts that execute without triggering signature verification events in audit logs.

## Related

- [[procedures/Disable-PowerShell-Script-Logging-and-Clear-Signatures]]
