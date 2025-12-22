---
type: procedure
description: >-
  Use enum4linux to enumerate network-facing Samba services on Windows targets,
  including users, groups, shares, and policies.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/enum4linux-enumerate-smb-services]]'
platforms:
  - Windows
tools:
  - '[[tools/enum4linux]]'
validated: true
---

# Enumerate-Samba-Services-on-Windows

## Summary

This procedure uses the enum4linux tool to perform comprehensive enumeration of Samba (SMB) services on Windows targets. It gathers information on users, groups, shares, domain policies, and RPC services, helping identify potential entry points for further exploitation in a network environment.

## Description

Samba services on Windows enable file and printer sharing via SMB protocol. Enumerating these services reveals sensitive information such as user accounts, group memberships, accessible shares, and password policies without requiring authentication in many cases. This technique is commonly used during reconnaissance to map the attack surface in Active Directory or standalone Windows environments. The procedure leverages enum4linux, a Perl-based tool that wraps smbclient, rpcclient, and other utilities to automate enumeration. It is effective against Windows servers with SMB enabled (ports 139/445) and assumes the target is reachable over the network.

## Requirements

1. Network access to the target Windows host on ports 139 (NetBIOS) and 445 (SMB direct).
2. enum4linux tool installed on a Linux-based attacker machine (e.g., Kali Linux).
3. No credentials required for anonymous enumeration, but valid credentials can unlock more details.
4. Basic understanding of SMB protocol and Windows networking.

## Defense

Defensive measures include disabling SMBv1, enforcing SMB signing, restricting anonymous access via Group Policy (e.g., 'Network access: Do not allow anonymous enumeration of SAM accounts'), and monitoring for unusual SMB traffic with tools like Windows Event Logs (ID 4625 for failed logons) or network IDS signatures for enum4linux patterns.

## Objectives

1. Identify exposed users and groups for potential credential attacks.
2. Discover accessible shares for data reconnaissance.
3. Enumerate domain policies to assess password complexity and lockout settings.
4. Map RPC services for lateral movement opportunities.

## Instructions

### Step 1: Verify Target Reachability and SMB Service

**Context**: Before enumeration, confirm the target is online and SMB ports are open to avoid unnecessary scans.

**Command** ([[commands/enum4linux-enumerate-smb-services]] with basic flags):
```bash
nmap -p139,445 $_TARGET_IP
```

> This step uses nmap (assumed pre-installed) to check port status. Replace $_TARGET_IP with the target's IP address.

### Step 2: Perform Basic Anonymous Enumeration

**Context**: Run enum4linux without credentials to gather publicly available SMB information, such as shares and basic user lists.

**Command** ([[commands/enum4linux-enum4linux-enumerate-smb-services]]):
```bash
enum4linux -a $_TARGET_IP
```

> The -a flag performs all enumeration modules. Expected output includes sections like 'Share Enumeration', listing shares such as IPC$, ADMIN$, C$, and any custom shares.

### Step 3: Enumerate Users and Groups Specifically

**Context**: Focus on user and group discovery to identify privileged accounts or interesting group memberships.

**Command** ([[commands/enum4linux-enumerate-users-and-groups]]):
```bash
enum4linux -U -G $_TARGET_IP
```

> -U enumerates users, -G enumerates groups. Output shows user SIDs, RIDs, and group members. Look for accounts like Administrator (RID 500) or Domain Admins.

### Step 4: Check Domain Policies and RID Cycling

**Context**: Retrieve password policies and test for RID cycling vulnerabilities to enumerate more users.

**Command** ([[commands/enum4linux-check-policies]]):
```bash
enum4linux -P -o $_TARGET_IP
```

> -P gets password policy info (e.g., min length, lockout threshold), -o enables RID cycling for user enumeration. Success is indicated by policy details and additional user lists if vulnerable.

### Step 5: Verify and Document Findings

**Context**: Review output for actionable intelligence and save results for reporting.

**Instructions**: Pipe output to a file for analysis:
```bash
enum4linux -a $_TARGET_IP | tee enum_results.txt
```

> Parse the file for shares with write access or high-privilege users. If null sessions are blocked, try with credentials using -u username -p password flags.

## Expected Output

Successful execution produces a multi-section report, e.g.:

====== Users found from the NODE @@: 
DANIEL\Administrator             SID: S-1-5-21-3525720511-529123456-1018739112-500  
DANIEL\Guest                      SID: S-1-5-21-3525720511-529123456-1018739112-501

Share Enumeration:
IPC$                  IPC Service () 
ADMIN$                Remote Admin 
C$                    Default share

Domain Policy: Password History:5, Min Length:7, Lockout:3 attempts.
