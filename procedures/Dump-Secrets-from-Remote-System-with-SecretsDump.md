---
id: 156e682a-001e-4e3f-9653-bb5c6798220f
name: Dump-Secrets-from-Remote-System-with-SecretsDump
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T01:39:57.862422+00:00'
updated_at: '2023-05-25T19:44:04.905834+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credential Dumping]]'
sub_techniques:
  - '[[DCSync]]'
tags:
  - active-directory
  - administrator
  - ntlm
  - pass-the-hash
commands:
  - '[[commands/secretsdump-py-dump-remote-hashes]]'
platforms:
  - Windows
tools:
  - '[[tools/Impacket]]'
validated: true
---

# Dump-Secrets-from-Remote-System-with-SecretsDump

## Summary

This procedure uses Impacket's secretsdump.py to extract password hashes from a remote Windows system via SMB, supporting methods like DCSync, LSA secrets, and SAM dumps, requiring admin or DCSync rights.

## Description

Secretsdump emulates legitimate protocols to pull credentials: DCSync for domain hashes, SAMR for local, LSASS for memory. Outputs LM/NTLM hashes and TGTs for cracking or PtH, critical for full compromise.

## Requirements

- Admin or DCSync creds
- SMB access (445)
- Impacket installed

## Defense

- Protect LSASS with Credential Guard
- Monitor DRSUAPI calls
- Use Just-Enough-Administration (JEA)

## Objectives

1. Authenticate to target
2. Dump relevant credential stores
3. Extract usable hashes

## Instructions

### Step 1: Prepare Creds

**Context**: Use DCSync-enabled user.

No command; note domain/user/pass.

### Step 2: Execute Dump

**Context**: Target DC for domain creds; use -just-dc for DCSync.

**Command** ([[commands/secretsdump-py-dump-remote-hashes]]):
```bash
python3 secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_IP -just-dc
```

> For local: omit -just-dc. Saves to file if -outputfile specified.

### Step 3: Parse Output

**Context**: Identify key hashes like krbtgt.

No command; grep for :nthash.

**Expected Output**: Lines like 'domain\user:500:aad3b...:ntlmhash:::'. 

## Expected Output

[*] Dumping Domain Credentials
username:rid:lm:nthash
