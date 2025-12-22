---
id: e732ce42-b42b-4f1e-9288-b71befcd80f1
name: spawn-winrm-shell-with-credentials
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
tools:
  - '[[tools/Evil-WinRM]]'
platforms:
  - Windows
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
---

# spawn-winrm-shell-with-credentials

## Summary

Establish an interactive PowerShell shell on a remote Windows host via WinRM using valid domain credentials obtained from cracking.

## Description

Evil-WinRM provides a Ruby-based shell for WinRM (port 5985), allowing command execution in the context of the provided user, useful for post-credential access in AD lateral movement.

## Requirements

- WinRM enabled on target (port 5985)
- Valid username/password
- Evil-WinRM installed ([[tools/Evil-WinRM]])
- Network access

## Defense

- Disable WinRM or restrict to trusted IPs
- Monitor Event ID 5145 for WinRM shares
- Use certificate-based auth instead of NTLM

## Objectives

1. Gain remote shell access
2. Execute commands in user context
3. Prepare for AD enumeration

## Instructions

### Step 1: Verify WinRM Availability

**Context**: Ensure port is open from prior scan.

No command; use nmap if needed.

> Proceed if open.

### Step 2: Connect with Credentials

**Context**: Launch shell using cracked creds.

**Command** ([[commands/evil-winrm-connect-with-password]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -p $_PASSWORD
```

> Establishes encrypted session.

### Step 3: Interact and Verify

**Context**: Run whoami to confirm context.

In shell: `whoami`.

> Expected: domain\username.

## Expected Output

Evil-WinRM shell prompt: *Evil-WinRM* PS C:\Users\username\>
