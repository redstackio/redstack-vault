---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: Spawn-Interactive-Shell-via-WinRM-from-Linux
type: procedure
verified: true
submitted: true
created_at: '2019-11-22T22:40:14.550466+00:00'
updated_at: '2023-05-25T19:42:05.411624+00:00'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - network
  - remote-access
commands:
  - '[[commands/evil-winrm-connect-with-password]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Spawn-Interactive-Shell-via-WinRM-from-Linux

## Summary

Establish an interactive PowerShell shell on a remote Windows host via WinRM using plaintext credentials obtained from cracking.

## Description

WinRM (port 5985/5986) enables remote PowerShell execution. Evil-WinRM provides a Ruby-based client for Linux attackers to connect, upload tools, and execute commands, ideal for post-crack access in AD chains.

## Requirements

- WinRM enabled on target (http:// or https://)
- Valid username/password
- Evil-WinRM gem installed (gem install evil-winrm)
- Port 5985 open

## Defense

- Disable WinRM if not needed or restrict to trusted IPs
- Enable WinRM HTTP logging and monitor Event ID 91/92
- Use Kerberos auth over NTLM and enforce MFA

## Objectives

1. Authenticate remotely via WinRM
2. Obtain interactive shell
3. Execute commands for enumeration/dumping

## Instructions

### Step 1: Verify WinRM Connectivity

**Context**: Ensure service is reachable before attempting login.

Use nmap to confirm port 5985 open.

### Step 2: Connect with Credentials

**Context**: Launch Evil-WinRM session using cracked creds.

**Command** ([[commands/evil-winrm-connect-with-password]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USER -p $_PASSWORD
```

> This connects over HTTP; add -S for HTTPS. Once in, use 'upload' for tools, 'powershell' for cmds.

**Expected Output**: *Evil-WinRM* PS C:\Users\user>

### Step 3: Test Shell Functionality

**Context**: Run basic commands to confirm access level.

Execute `whoami` or `net user` from the shell.

If fails, check creds or WinRM config (winrm quickconfig).
