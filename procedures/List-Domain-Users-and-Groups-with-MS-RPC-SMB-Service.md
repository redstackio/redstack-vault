---
id: 86968dcb-c057-4fd2-95b1-a231974be41e
name: List-Domain-Users-and-Groups-with-MS-RPC-SMB-Service
type: procedure
verified: true
submitted: true
created_at: '2020-03-26T05:23:16.749793+00:00'
updated_at: '2023-05-25T19:46:08.899829+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/System-Owner-User-Discovery|T1033 - System Owner/User
    Discovery]]
sub_techniques: []
platforms:
  - Windows
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/rpcclient-authenticate-with-an-rpc-server]]'
  - '[[commands/enumdomusers-list-domain-users-on-smb-rpc-server]]'
  - '[[commands/enumdomgroups-list-domain-groups-on-smb-rpc-server]]'
tools:
  - '[[tools/rpcclient]]'
validated: true
---

# List-Domain-Users-and-Groups-with-MS-RPC-SMB-Service

## Summary

This procedure uses the rpcclient tool from the Samba suite to connect to a Windows domain controller or SMB server via MS-RPC over SMB and enumerate all domain users and groups. It supports null sessions for anonymous access or authenticated connections, providing a list of users and groups that can reveal privileged accounts for further targeting in reconnaissance or lateral movement.

## Description

In a Windows Active Directory environment, attackers often need to map out user and group structures to identify high-value targets like domain admins or service accounts. This procedure leverages rpcclient to establish an RPC connection to the target server (typically port 445 for SMB) and issues enumeration commands to query the Security Account Manager (SAM) database remotely. It works against domain controllers or member servers with RPC services exposed. Null sessions allow anonymous enumeration if not restricted by Group Policy, but authenticated access provides more complete results. This technique is commonly used in early discovery phases to build a target profile without needing local access.

## Requirements

1. Network access to the target SMB/RPC server on port 445.
2. rpcclient tool installed (part of Samba suite).
3. Valid domain credentials (optional; null session may work if anonymous access is permitted).
4. Attacker machine on the same network or with firewall rules allowing SMB traffic.

## Defense

- Restrict anonymous RPC access via Group Policy (e.g., Network access: Restrict anonymous access to Named Pipes and Shares).
- Monitor SMB/RPC traffic for unusual enumeration queries using tools like Windows Event Logs (Event ID 4625 for failed logons) or network IDS like Snort.
- Implement least privilege: Limit RPC endpoint access to authenticated users only.
- Use network segmentation to isolate domain controllers from untrusted networks.

## Objectives

1. Authenticate with an RPC service on a remote Windows machine to establish a session.
2. Obtain a comprehensive list of domain users for targeting privileged accounts.
3. Obtain a list of domain groups to identify administrative or sensitive group memberships.
4. Use the enumerated information for further reconnaissance, such as phishing or Kerberoasting.

## Instructions

### Step 1: Authenticate with the RPC Server

**Context**: Establish a connection to the target's RPC service over SMB. Use null session by omitting credentials if anonymous access is allowed; otherwise, provide domain credentials. This opens an interactive rpcclient shell for issuing enumeration commands.

**Command** ([[commands/rpcclient-authenticate-with-an-rpc-server]]):
```bash
rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
```

This command initiates the connection. If successful, you will enter the rpcclient interactive prompt (rpcclient $). For null sessions, use empty quotes: rpcclient -U "" $_TARGET_IP. Verify the connection by checking for the prompt without authentication errors.

### Step 2: Enumerate Domain Users

**Context**: Once connected, query the domain for all user accounts. This reveals usernames, SIDs, and types, helping identify potential targets like admins or service accounts. Run this inside the rpcclient shell.

**Command** ([[commands/enumdomusers-list-domain-users-on-smb-rpc-server]]):
```bash
enumdomusers
```

Execute this directly in the rpcclient prompt. It queries the LSA (Local Security Authority) for domain user enumeration. Expected output includes a table of users with relative IDs (RIDs); look for high RIDs (e.g., 500 for Administrator) or patterns like service accounts.

### Step 3: Enumerate Domain Groups

**Context**: Query the domain for group memberships to map administrative privileges. This complements user enumeration by showing groups like Domain Admins or Enterprise Admins, aiding in privilege escalation planning.

**Command** ([[commands/enumdomgroups-list-domain-groups-on-smb-rpc-server]]):
```bash
enumdomgroups
```

Run this in the rpcclient shell after user enumeration. It lists all domain groups with SIDs and descriptions. Success is indicated by a complete list without errors; cross-reference with user data for overlaps.

To exit the rpcclient shell, type 'quit' or Ctrl+C.
