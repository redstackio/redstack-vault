---
type: code
language: powershell
verified: true
tags:
  - chaining
  - command-injection
  - payload
platforms:
  - Windows
validated: true
---

# powershell-command-chaining-operators

## Code

```powershell
original_cmd_by_server; ls
original_cmd_by_server && ls
original_cmd_by_server | ls
original_cmd_by_server || ls   # Only if the first cmd fail
```

## Description

This PowerShell code snippet illustrates chaining multiple commands using operators for unconditional (`;`), success-based (`&&`), pipe (`|`), and failure-based (`||`) execution. It is designed for injection into vulnerable PowerShell invocations to perform sequential actions like reconnaissance or escalation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| original_cmd_by_server | The original vulnerable command executed by the server | Get-Date |
| ls | Placeholder for injected command (use Get-ChildItem for PowerShell native) | Get-ChildItem |

## Usage

Inject this into a PowerShell-executing input field, such as a web app running `Invoke-Expression` on user data. Start with simple chains for testing, then replace `ls` with payloads like downloading tools or exfiltrating files. Use in red team scenarios to simulate multi-stage attacks from a single injection point.

## Detection

- Monitor PowerShell logs for unusual operator usage in ScriptBlock or Module logging.
- Look for chained commands in process arguments via Sysmon or ETW.
- Anomaly detection on execution patterns, e.g., reconnaissance commands following benign ones.

## Related

- [[procedures/Command-Injection-Chaining-Commands]]
