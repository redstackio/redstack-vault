---
id: 016ec01a-829e-4b74-96a5-67d13a250649
name: Active-Directory-ACL-Scanning-for-User
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.678186+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - >-
    [[techniques/Permission-Groups-Discovery|T1069 - Permission Groups
    Discovery]]
sub_techniques:
  - '[[sub-techniques/Domain-Groups|T1069.002 - Domain Groups]]'
tags:
  - '[[tags/Abusing-Active-Directory-ACLs-ACEs]]'
  - '[[tags/Active-Directory-Attacks]]'
commands:
  - '[[commands/adaclscan-scan-user-permissions]]'
platforms:
  - Windows
tools:
  - '[[tools/ADACLScan]]'
validated: true
---

# Active-Directory-ACL-Scanning-for-User

## Summary

This procedure scans Active Directory Access Control Lists (ACLs) for a specific user to identify the objects they have permissions on, such as groups, OUs, or other domain entities. It reveals effective rights, helping attackers map privilege escalation paths or lateral movement opportunities in an Active Directory environment.

## Description

Active Directory ACLs control permissions on domain objects. Scanning a user's ACLs enumerates all objects where the user has explicit or inherited rights, including read, write, or control access. This technique is useful during post-exploitation to discover misconfigurations, like excessive permissions on sensitive objects. It targets domain-joined systems with authenticated access and can output results in formats like HTML for analysis. Commonly used in red team engagements to build attack graphs, similar to BloodHound but focused on principal-specific permissions. The procedure assumes domain authentication and uses LDAP queries to traverse the directory tree.

## Requirements

1. Domain user credentials with read access to Active Directory objects.
2. PowerShell execution policy allowing script runs (e.g., Bypass).
3. Access to a domain-joined Windows machine or remote LDAP access.
4. ADACLScan.ps1 script downloaded and available in the execution path.

## Defense

- Implement least privilege: Regularly audit and trim ACLs to remove unnecessary permissions.
- Enable Active Directory auditing for directory service access events (Event ID 4662).
- Use tools like BloodHound or Microsoft ATA to monitor for anomalous permission queries.
- Restrict PowerShell script execution via AppLocker or constrained language mode.

## Objectives

1. Enumerate all domain objects a target user has effective permissions on.
2. Identify high-value targets like admin groups or DCs for escalation.
3. Generate a report for further analysis of permission abuse opportunities.

## Instructions

### Step 1: Prepare the Environment

**Context**: Ensure the ADACLScan script is available and you have valid domain credentials. Import necessary modules if required, and set the execution policy.

Run PowerShell as the authenticated user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

> This allows running unsigned scripts for the session. Expected output: Execution policy updated confirmation.

### Step 2: Scan User ACLs

**Context**: Execute the ADACLScan command to query the domain for the user's effective rights on admin objects. Customize the base DN, filter, and principal as needed.

**Command** ([[commands/adaclscan-scan-user-permissions]]):

```powershell
ADACLScan.ps1 -Base "DC=contoso,DC=com" -Filter "(&(AdminCount=1))" -Scope subtree -EffectiveRightsPrincipal User1 -Output HTML -Show
```

> This command starts from the domain root, filters for protected admin objects (AdminCount=1), searches the entire subtree, checks effective rights for 'User1', outputs to HTML, and displays results. Replace 'DC=contoso,DC=com' with your domain DN, 'User1' with the target user, and adjust filter/scope for broader scans. Expected output: Console display of permissions and an HTML file listing objects with access rights like GenericAll, WriteDacl, etc.

### Step 3: Analyze Results

**Context**: Review the output to identify exploitable permissions, such as control over groups or OUs.

Open the generated HTML report in a browser or parse the console output for rights like 'FullControl' on sensitive objects.

> Look for indicators like 'GenericAll' on Domain Admins or 'WriteOwner' on key OUs. If no high-value rights found, expand the filter (e.g., remove AdminCount) for a full domain scan.

Expected output: Structured list of objects, rights, and paths, e.g., 'User1 has DeleteTree on CN=Domain Admins,CN=Users,DC=contoso,DC=com'.
