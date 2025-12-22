---
id: new-uuid-1
name: enumerate-domain-users-and-groups-via-rpc-smb
type: procedure
verified: true
submitted: true
created_at: '2023-01-01T00:00:00+00:00'
updated_at: '2023-06-01T00:00:00+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
commands:
  - '[[commands/rpcclient-enumdomusers]]'
  - '[[commands/rpcclient-enumdomgroups]]'
tools:
  - '[[tools/rpcclient]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: low
detection_risk: low
validated: true
---

# enumerate-domain-users-and-groups-via-rpc-smb

## Summary

Use anonymous RPC/SMB connections to enumerate domain users and groups from a Windows Active Directory server, building a wordlist for targeted attacks like AS-REP roasting.

## Description

This procedure leverages null sessions via rpcclient to query the SAMR pipe for user and group information without credentials, common in misconfigured AD environments. It provides usernames for further exploitation.

## Requirements

- Port 445 open on target
- rpcclient installed ([[tools/rpcclient]] from Samba)
- Target IP

## Defense

- Disable null sessions in SMB configuration
- Monitor Event ID 4625 for failed logons
- Restrict RPC bindings

## Objectives

1. Extract domain usernames
2. List group memberships
3. Identify potential targets with weak flags

## Instructions

### Step 1: Connect and Enumerate Users

**Context**: Establish null session and query domain users to get a list of accounts.

**Command** ([[commands/rpcclient-enumdomusers]]):
```bash
rpcclient -U "" -N $_TARGET_IP -c "enumdomusers"
```

> Outputs RID:Username pairs; save to users.txt for roasting.

### Step 2: Enumerate Groups

**Context**: Query domain groups to understand structure and privileged accounts.

**Command** ([[commands/rpcclient-enumdomgroups]]):
```bash
rpcclient -U "" -N $_TARGET_IP -c "enumdomgroups"
```

> Lists groups like Domain Admins; cross-reference with users.

### Step 3: Parse and Filter

**Context**: Clean output to focus on user accounts without preauth.

No command; use grep or manual review to filter interesting users.

> Expected: 50+ usernames ready for next steps.

## Expected Output

Lists of users and groups, e.g., user:[Administrator] rid:[0x1f4].
