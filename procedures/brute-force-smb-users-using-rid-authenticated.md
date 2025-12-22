---
id: 021d64ab-15d2-49b0-90f1-37dd538bdd14
name: brute-force-smb-users-using-rid-authenticated
type: procedure
verified: true
submitted: false
created_at: '2019-12-27T22:38:42.691840+00:00'
updated_at: '2023-05-25T19:42:32.339817+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques: []
tags:
  - network
  - service-attacks
commands:
  - '[[commands/crackmapexec-brute-force-smb-users-using-rid]]'
  - '[[commands/impacket-lookupsid-brute-force-smb-users-using-rid]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Impacket]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
---

# brute-force-smb-users-using-rid-authenticated

## Summary

Using authenticated SMB access, this procedure enumerates domain users by brute-forcing Relative Identifiers (RIDs) via SID cycling, revealing account names without null sessions.

## Description

RIDs are sequential in AD (500=Administrator), allowing prediction. Authenticated queries via LSARPC pipe enumerate without alerts, ideal after initial brute-force.

## Requirements

1. Valid SMB credentials
2. Target IP with domain-joined SMB
3. CrackMapExec or Impacket

## Defense

- Disable RID cycling via registry (RestrictAnonymous)
- Monitor LSARPC calls in event logs
- Use just-in-time admin privileges

## Objectives

1. List domain users and SIDs
2. Identify privileged accounts
3. Expand target list for further attacks

## Instructions

### Step 1: Authenticate and Prep

**Context**: Confirm creds work.

smbclient //$_TARGET_IP/C$ -U user%pass

> Exit after connect.

### Step 2: Run RID Brute-Force with CME

**Context**: Cycle RIDs 500-1000+ for users.

**Command** ([[commands/crackmapexec-brute-force-smb-users-using-rid]]):
```bash
crackmapexec smb $_TARGET_IP -u $_USERNAME -p $_PASSWORD --rid-brute
```

> Lists users like 1001: DOMAIN\user.

### Step 3: Alternative with Impacket

**Context**: If CME fails, use lookupsid for same result.

**Command** ([[commands/impacket-lookupsid-brute-force-smb-users-using-rid]]):
```bash
lookupsid.py '$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

> Parses domain SID and enumerates; compare outputs.
