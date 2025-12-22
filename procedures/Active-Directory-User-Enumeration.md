---
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques:
  - '[[techniques/Account-Discovery-Domain-Accounts|T1087.002 - Domain Accounts]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/User Hunting]]'
commands:
  - '[[commands/crackmapexec-enumerate-smb-sessions]]'
  - '[[commands/impacket-smbclient-list-connected-users]]'
  - '[[commands/powerview-invoke-userhunter-basic]]'
  - '[[commands/powerview-invoke-userhunter-by-group]]'
  - '[[commands/powerview-invoke-userhunter-stealth]]'
platforms:
  - Windows
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/Impacket]]'
  - '[[tools/PowerView]]'
validated: true
---

# Active-Directory-User-Enumeration

## Summary

Active Directory User Enumeration involves querying domain resources to identify active users, their sessions, and associated machines. This procedure uses tools like CrackMapExec, Impacket, and PowerView to discover logged-in users, SMB sessions, and targets hosting privileged sessions, aiding in lateral movement planning such as targeting Domain Admin sessions for privilege escalation.

## Description

In an Active Directory environment, attackers with initial foothold or low-privilege credentials can enumerate users to map the attack surface. This includes listing active SMB sessions across the network, checking connected users on specific hosts via SMB, and hunting for machines with sessions from high-privilege users like Domain Admins or group members. The technique leverages LDAP queries, SMB protocol interactions, and PowerShell modules to gather this intelligence without direct AD replication rights. It's commonly used post-initial access to identify pivot points for credential dumping or remote execution. Success depends on network access and valid credentials; detection can be mitigated by using stealth options to reduce noisy queries.

## Requirements

1. Valid domain credentials (e.g., low-privilege user or admin) with SMB/LDAP access.
2. Network connectivity to target domain controllers, workstations, or servers (ports 445/TCP for SMB, 389/636 for LDAP).
3. Installed tools: CrackMapExec, Impacket suite, PowerView PowerShell module.
4. Domain-joined or reachable position in the network.

## Defense

- Enable SMB signing and monitor for anomalous authentication attempts via Event ID 4624/4776.
- Implement LDAP query logging and restrict anonymous binds; use tools like Microsoft ATA for AD anomaly detection.
- Limit PowerShell execution with Constrained Language Mode and enable Script Block Logging (Event ID 4104).
- Use network segmentation and EDR to alert on session enumeration patterns from unusual sources.

## Objectives

1. Identify active users and their logged-in machines for targeted attacks.
2. Locate hosts with privileged sessions (e.g., Domain Admin) for lateral movement.
3. Gather intelligence on user activity to support phishing or password spraying.

## Instructions

### Step 1: Enumerate SMB Sessions Across the Network

**Context**: Start by scanning the target subnet for active SMB sessions using domain credentials. This reveals which users are authenticated to which machines, providing initial user mapping without alerting defenders.

**Command** ([[commands/crackmapexec-enumerate-smb-sessions]]):
```bash
cme smb $_TARGET_SUBNET -u $_USERNAME -p $_PASSWORD --sessions
```

> This command authenticates to each host in the subnet via SMB and lists open sessions. Replace $_TARGET_SUBNET with the network range (e.g., 10.10.10.0/24), $_USERNAME with a domain user, and $_PASSWORD with the password. It performs why this step: to identify user-machine associations efficiently across the domain.

### Step 2: List Connected Users on a Specific Host

**Context**: For a targeted machine identified from prior enumeration, connect via SMB and query active sessions to see exactly who is logged in, helping pinpoint exploitable user contexts.

**Command** ([[commands/impacket-smbclient-list-connected-users]]):
```bash
impacket-smbclient $_USERNAME@$_TARGET_IP
who
```

> Connect to the target host using SMB client, then run 'who' to list active users. Use $_USERNAME (domain user) and $_TARGET_IP (host IP). This step verifies local sessions on a host, useful after identifying interesting machines from Step 1.

### Step 3: Hunt for Domain Admin or Specified User Sessions

**Context**: Use PowerShell to query the domain for computers hosting sessions from Domain Admins or specific users. This targets high-value pivots; run from a compromised domain-joined host.

**Command** ([[commands/powerview-invoke-userhunter-basic]]):
```powershell
Invoke-UserHunter
```

> Executes a basic hunt for Domain Admin sessions across the domain via LDAP queries. No parameters needed for default behavior; it lists computers with DA sessions. This identifies immediate escalation targets.

### Step 4: Hunt for Sessions in a Specific Group

**Context**: Narrow the search to users in a particular group (e.g., RDPUsers) to find machines with sessions from that group, reducing noise and focusing on relevant privileges.

**Command** ([[commands/powerview-invoke-userhunter-by-group]]):
```powershell
Invoke-UserHunter -GroupName $_GROUP_NAME
```

> Specifies a group like "RDPUsers" via $_GROUP_NAME parameter. This queries LDAP for group members and their sessions, helping target group-based access.

### Step 5: Perform Stealthy User Hunter Query

**Context**: Run the hunter in stealth mode to avoid generating excessive network traffic, ideal for evading detection during live operations.

**Command** ([[commands/powerview-invoke-userhunter-stealth]]):
```powershell
Invoke-UserHunter -Stealth
```

> Enables stealth mode, which uses slower, less detectable queries. Use when OPSEC is critical; combines with prior steps for comprehensive but low-profile enumeration.
