---
id: 2531e058-1a98-452a-9f87-52ac02588cd8
name: Establish-Remote-Shell-with-PsExec
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T20:10:15.053531+00:00'
updated_at: '2023-05-25T19:58:04.662024+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Remote Services|T1021.002 - SMB/Windows Admin Shares]]'
sub_techniques: []
platforms:
  - Windows
tags:
  - network
  - service-attacks
commands:
  - '[[commands/impacket-psexec-connect-and-spawn-shell]]'
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Establish-Remote-Shell-with-PsExec

## Summary

This procedure uses PSExec via Impacket to upload and execute a payload on a remote Windows host, spawning a cmd shell with admin privileges.

## Description

PSExec exploits admin shares (ADMIN$) to create a temporary service that runs cmd.exe. Requires admin creds; common for lateral movement post-credential theft.

## Requirements

- Admin credentials
- Target IP with SMB/admin shares
- Impacket psexec.py

## Defense

- Disable admin shares (HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\RequireSecuritySignature)
- Use WDAC to block unsigned executables
- Monitor service creation (Event ID 7045)

## Objectives

1. Authenticate and upload payload
2. Create/start service
3. Interact with shell

## Instructions

### Step 1: Connect and Spawn Shell

**Context**: Targets ADMIN$ for execution.

**Command** ([[commands/impacket-psexec-connect-and-spawn-shell]]):
```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

> Outputs shell; use 'help' for commands.

### Step 2: Execute Post-Exploitation

**Context**: Run whoami, net user in shell.

In shell: whoami /priv; exit to close.

> Success if cmd prompt appears.
