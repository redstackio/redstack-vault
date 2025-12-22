---
id: new-uuid-for-this
name: List-Domain-Users-and-Groups-via-MS-RPC-over-SMB
type: procedure
verified: true
submitted: false
created_at: '2020-03-13T23:58:22.902373+00:00'
updated_at: '2023-05-29T16:48:53.162677+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
  - '[[Permission Groups Discovery]]'
sub_techniques: []
tags:
  - active-directory
  - enumeration
  - rpc
commands:
  - '[[commands/rpcclient-enumdomusers]]'
  - '[[commands/rpcclient-enumdomgroups]]'
platforms:
  - Linux
tools:
  - '[[tools/Impacket]]'
validated: true
---

# List-Domain-Users-and-Groups-via-MS-RPC-over-SMB

## Summary

This procedure connects to a Windows SMB server using rpcclient to enumerate domain users and groups via MS-RPC, often possible with null sessions, providing a wordlist for further attacks like AS-REP roasting.

## Description

MS-RPC over SMB (port 445) allows enumeration of AD objects without authentication in misconfigured environments. This reveals usernames and groups, aiding in targeting preauth-disabled users. It's a key discovery step in AD attacks.

## Requirements

- SMB access to target (port 445 open)
- Impacket tools installed
- Null session or low-priv creds

## Defense

- Disable null sessions on SMB
- Restrict RPC endpoints with Group Policy
- Monitor for rpcclient connections in logs

## Objectives

1. Enumerate all domain users
2. List domain groups for privilege mapping
3. Build username list for brute-forcing

## Instructions

### Step 1: Enumerate Domain Users

**Context**: Connect via null session and query for user accounts to obtain a list of potential targets.

**Command** ([[commands/rpcclient-enumdomusers]]):
```bash
rpcclient -U "" //$_TARGET_IP -c "enumdomusers"
```

> Outputs user RIDs and names. If access denied, try authenticated session with -U user%pass.

### Step 2: Enumerate Domain Groups

**Context**: Query for groups to understand hierarchy and target sensitive ones like Domain Admins.

**Command** ([[commands/rpcclient-enumdomgroups]]):
```bash
rpcclient -U "" //$_TARGET_IP -c "enumdomgroups"
```

> Lists group names and SIDs. Save to file: rpcclient ... > groups.txt.

### Step 3: Verify and Save Results

**Context**: Combine outputs into wordlists, removing invalid entries.

No command; manual processing.

**Expected Output**: Text files with users.txt (e.g., 'user1:0x1f4') and groups.txt.

## Expected Output

User enumeration:

user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]

Group enumeration:

group:[Domain Admins] rid:[0x201]
