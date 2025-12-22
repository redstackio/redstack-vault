---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: Establish-WinRM-Remote-Shell
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T22:40:14.550466+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
sub_techniques:
  - '[[.001]] WinRM'
platforms:
  - Windows
tags:
  - network
commands:
  - '[[commands/evil-winrm-connect-to-server]]'
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Establish-WinRM-Remote-Shell

## Summary

This procedure leverages WinRM (port 5985) and valid credentials to spawn an interactive PowerShell shell on a remote Windows host, enabling command execution and lateral movement.

## Description

WinRM is Microsoft's remote management protocol, often enabled for admin tasks. Evil-WinRM provides a Ruby-based client for authenticated sessions, bypassing some PSRemoting restrictions. It's post-exploitation for running commands, file transfer, or persistence. Assumes HTTP (non-SSL); use -S for HTTPS.

## Requirements

- Valid domain or local credentials
- WinRM enabled on target (winrm quickconfig)
- Network access to TCP/5985
- Evil-WinRM installed (gem install evil-winrm)

## Defense

- Disable WinRM if unused (Disable-PSRemoting)
- Restrict WinRM to trusted IPs via firewall
- Enable WinRM logging (Event ID 91/92 for connections)
- Use certificate auth instead of basic

## Objectives

- Authenticate via WinRM
- Obtain interactive shell
- Execute remote commands

## Instructions

### Step 1: Connect to WinRM Service

**Context**: Use credentials to establish the session. Handles NTLM auth automatically.

**Command** ([[commands/evil-winrm-connect-to-server]]):
```bash
evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> -i host, -u user, -p pass. Expected: PS prompt. If fails (e.g., 'WinRM refused'), check service/port/creds. Decision: For HTTPS, add --ssl.
