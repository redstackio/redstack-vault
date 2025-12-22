---
type: procedure
description: >-
  Uses Mimikatz to perform DCSync attacks for retrieving Active Directory user
  password hashes via the Directory Replication Service.
verified: true
submitted: false
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping AD Domain Credentials]]'
  - '[[tags/Using Mimikatz DCSync]]'
commands:
  - '[[commands/mimikatz-lsadump-dcsync-single-user]]'
  - '[[commands/mimikatz-lsadump-dcsync-all-users]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: intermediate
impact_level: high
detection_risk: high
validated: true
---

# Mimikatz-DCSync-Password-Hash-Dumping

## Summary

This procedure uses the Mimikatz tool to perform a DCSync attack, impersonating a domain controller to replicate and extract password hashes (NTLM) for Active Directory user accounts without direct access to the NTDS.dit file. It leverages the Directory Replication Service Remote Protocol (MS-DRSR) and is effective for credential access in domain environments, enabling subsequent lateral movement or pass-the-hash attacks.

## Description

Mimikatz DCSync simulates domain controller replication to request sensitive data like password hashes from a legitimate domain controller. This technique requires high-privilege access, such as Domain Admin, Enterprise Admin, or control over a domain-joined machine with replication rights. It targets Windows Active Directory environments and can extract hashes for individual users or all domain accounts. The output includes NTLM hashes, which can be cracked offline or used directly in attacks. This method evades many AV solutions since it uses legitimate Windows protocols (RPC over TCP 445). Use this in post-exploitation scenarios after gaining domain privileges to harvest credentials for further compromise.

## Requirements

1. Domain Admin, Enterprise Admin, or equivalent privileges (e.g., membership in Administrators, Domain Admins, or control of a Domain Controller account).
2. Network access to a Domain Controller (TCP port 445 open for SMB/RPC).
3. Mimikatz tool installed or executable on the attacker's machine (Windows x64 preferred).
4. Valid domain-joined session or credentials with replication rights.

## Defense

- Implement least privilege: Restrict replication rights to only necessary accounts and monitor for anomalous DCSync attempts via Directory Services logs (Event ID 4662 for replication access).
- Enable Protected Users group and disable RC4 encryption to limit hash usability.
- Use advanced logging: Enable DRSUAPI auditing and monitor for LSASS access or unusual RPC calls to port 445.
- Deploy EDR tools to detect Mimikatz execution signatures and anomalous credential access patterns.

## Objectives

1. Extract NTLM password hashes for specified or all Active Directory user accounts.
2. Enable offline cracking or direct use of hashes for lateral movement and privilege escalation.
3. Obtain krbtgt hash for potential Golden Ticket attacks if targeting that account.

## Instructions

### Step 1: Launch Mimikatz and Elevate Privileges

**Context**: Start Mimikatz with system-level privileges to ensure access to replication protocols. This step verifies the environment and prepares for DCSync execution.

**Command** ([[commands/mimikatz-elevate-privileges]]):
```bash
privilege::debug
```

> This enables debug privileges required for LSADUMP operations. Expected output: "Privilege '20' OK" confirming elevation success.

### Step 2: Perform DCSync on a Single User

**Context**: Target a specific user (e.g., krbtgt for Golden Ticket potential) to retrieve their NTLM hash and other attributes like SID and supplemental credentials. Use this for focused extraction to minimize noise.

**Command** ([[commands/mimikatz-lsadump-dcsync-single-user]]):
```bash
lsadump::dcsync /domain:$_DOMAIN /user:$_USER
```

> Replace $_DOMAIN with the target domain (e.g., htb.local) and $_USER with the username (e.g., krbtgt). This requests replication data for the user via MS-DRSR. Expected output: User details including NTLM hash, RID, and Kerberos keys in a formatted block.

### Step 3: Perform DCSync on All Domain Users

**Context**: Extract hashes for every user account in the domain for comprehensive credential harvesting. Output in CSV for easy parsing and offline cracking with tools like Hashcat.

**Command** ([[commands/mimikatz-lsadump-dcsync-all-users]]):
```bash
lsadump::dcsync /domain:$_DOMAIN /all /csv
```

> Replace $_DOMAIN with the target domain. The /all flag replicates all users, and /csv formats output as comma-separated values. Expected output: A CSV stream with columns for Username, UserId, LM, NTLM, and other attributes for each account.

### Step 4: Verify and Export Results

**Context**: Save the output for analysis or cracking. Check for successful hash extraction and note any errors indicating insufficient privileges.

**Instructions**: Redirect output to a file if needed (e.g., via console redirection) and validate hashes are present (non-zero NTLM values). Use tools like Hashcat for cracking extracted NTLM hashes.

> Success criteria: Hashes displayed without errors like "Access Denied" or "Invalid Domain".
