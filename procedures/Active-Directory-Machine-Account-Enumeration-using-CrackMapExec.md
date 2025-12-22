---
id: 2779c9fb-0f35-4003-865c-b035fa8a008c
name: Active-Directory-Machine-Account-Enumeration-using-CrackMapExec
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:03.040390+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account-Discovery|T1087 - Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Enumeration]]'
  - '[[tags/Machine Accounts]]'
commands:
  - '[[commands/crackmapexec-ldap-enumerate-machine-account-quota]]'
  - '[[commands/standin-query-machine-account-quota]]'
platforms:
  - Windows
  - Active Directory
tools:
  - '[[tools/CrackMapExec]]'
  - '[[tools/StandIn]]'
validated: true
---

# Active-Directory-Machine-Account-Enumeration-using-CrackMapExec

## Summary

This procedure uses CrackMapExec (CME) to query Active Directory for machine account quota information, which reveals details about the number of machine accounts allowed in the domain. This enumeration helps attackers understand domain policies for machine account creation and identify potential abuse vectors for privilege escalation or lateral movement.

## Description

In Active Directory environments, the ms-DS-MachineAccountQuota attribute defines how many machine accounts a user can create without admin privileges (default is 10). Enumerating this quota via LDAP queries provides insights into domain security posture and can inform attacks like creating rogue machine accounts for resource-based constrained delegation (RBCD). CrackMapExec's MAQ module performs the LDAP query against a domain controller, followed by using StandIn.exe to extract specific object details. This technique is useful during internal reconnaissance after initial access, targeting Windows domain controllers over LDAP (port 389) or LDAPS (636). Prerequisites include valid domain credentials with query permissions.

## Requirements

1. Valid domain user credentials with LDAP query access to the domain controller.
2. Network access to the domain controller (TCP 389 or 636).
3. CrackMapExec installed on a Linux-based attack machine (e.g., Kali).
4. StandIn.exe downloaded and available (Windows executable, can be run via wine or on a Windows host).

## Defense

- Monitor LDAP queries for ms-DS-MachineAccountQuota attribute access using tools like Microsoft ATA or SIEM rules for anomalous enumeration.
- Implement least privilege: Restrict LDAP query rights and set low MachineAccountQuota values.
- Enable advanced auditing for directory service access events (Event ID 4662) on domain controllers.

## Objectives

1. Retrieve the domain's machine account quota to assess policy weaknesses.
2. Identify the default quota value and any custom configurations.
3. Gather intelligence for potential machine account spraying or RBCD attacks.

## Instructions

### Step 1: Query Machine Account Quota with CrackMapExec

**Context**: Use CrackMapExec's LDAP module with the MAQ (Machine Account Quota) module to perform an authenticated LDAP query against the domain controller. This step authenticates with provided credentials and retrieves quota-related information from the domain's configuration partition.

**Command** ([[commands/crackmapexec-ldap-enumerate-machine-account-quota]]):
```bash
crackmapexec ldap $DC_IP -u $USERNAME -p $PASSWORD -d $DOMAIN --kdcHost $DC_IP -M MAQ
```

> This command connects to the domain controller at $DC_IP, authenticates as $USERNAME, and runs the MAQ module to enumerate the quota. Replace placeholders with actual values (e.g., DC_IP=10.10.10.10, USERNAME=username, PASSWORD=Password123, DOMAIN=domain.local). Expected output includes the quota value, such as "Machine Account Quota: 10", confirming successful enumeration.

### Step 2: Extract Detailed Quota Object with StandIn

**Context**: After obtaining initial quota data from CME, use StandIn.exe to query Active Directory objects matching the ms-DS-MachineAccountQuota attribute. This provides deeper details on quota configurations and associated objects, helping validate and expand on the CME results.

**Command** ([[commands/standin-query-machine-account-quota]]):
```bash
StandIn.exe --object ms-DS-MachineAccountQuota=*
```

> Run StandIn.exe (on a Windows machine or via compatibility layer) to search for all objects with the ms-DS-MachineAccountQuota attribute set. This outputs a list of matching domain objects and their quota values. Expected output includes details like "CN=System,DC=domain,DC=local: ms-DS-MachineAccountQuota=10". If no output or errors occur, verify credentials and network access.
