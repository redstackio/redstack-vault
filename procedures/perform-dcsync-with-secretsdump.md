---
id: 156e682a-001e-4e3f-9653-bb5c6798220f
name: perform-dcsync-with-secretsdump
type: procedure
verified: true
submitted: true
created_at: '2020-03-16T01:39:57.862422+00:00'
updated_at: '2023-05-25T19:44:04.905834+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[DCSync]]'
sub_techniques: []
tags:
  - active-directory
  - administrator
  - ntlm
  - pass-the-hash
commands:
  - '[[commands/secretsdump-dcsync]]'
tools:
  - '[[tools/impacket-secretsdump]]'
platforms:
  - Windows
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
---

# perform-dcsync-with-secretsdump

## Summary

Use DCSync rights to dump all domain password hashes from the NTDS.DIT via Impacket's secretsdump, including admin and krbtgt hashes.

## Description

Secretsdump simulates DC replication over DRSUAPI to extract hashes without direct file access, requiring replication permissions.

## Requirements

- DCSync rights
- Domain creds
- Impacket ([[tools/impacket-secretsdump]])
- DC IP

## Defense

- Monitor replication requests (Event ID 4662)
- Limit Get-Changes rights to DCs
- Enable protected users

## Objectives

1. Dump domain hashes
2. Obtain NTLM for PtH
3. Capture krbtgt for tickets

## Instructions

### Step 1: Verify Rights

**Context**: Ensure user has DCSync.

Test with small query if possible.

### Step 2: Execute Dump

**Context**: Run against DC with creds.

**Command** ([[commands/secretsdump-dcsync]]):
```bash
secretsdump.py $_DOMAIN/$_USER:$_PASSWORD@$_DC_IP
```

> Uses DRSUAPI method.

### Step 3: Parse Output

**Context**: Save hashes for cracking/PtH.

Redirect to file: `... > hashes.txt`.

> Extract admin hashes.

## Expected Output

Lines like domain\Administrator:500:...:ntlm_hash:::
