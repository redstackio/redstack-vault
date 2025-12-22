---
id: 9adb8704-13aa-4ef7-ad3e-b48371008d10
name: windows-user-enumeration-and-privilege-check
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:28.643074+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/System Owner/User Discovery|T1033 - System Owner/User
    Discovery]]
sub_techniques:
  - '[[sub-techniques/Domain Account|T1087.002 - Domain Account]]'
  - '[[sub-techniques/Local Account|T1087.001 - Local Account]]'
tags:
  - '[[tags/User Enumeration]]'
  - '[[tags/Windows - Privilege Escalation]]'
commands:
  - '[[commands/whoami-groups-windows]]'
  - '[[commands/whoami-privileges-windows]]'
  - '[[commands/net-user-list-all]]'
  - '[[commands/net-accounts-policy]]'
  - '[[commands/net-user-admin-query]]'
  - '[[commands/net-localgroup-list]]'
  - '[[commands/net-localgroup-administrators]]'
  - '[[commands/nltest-dclist-domain]]'
  - '[[commands/nltest-dcname-domain]]'
  - '[[commands/nltest-dsgetdc-domain]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-user-enumeration-and-privilege-check

## Summary

This procedure enumerates user accounts, groups, privileges, and domain controller information on a Windows system to identify potential privilege escalation paths. It uses built-in commands like net, whoami, and nltest to gather details on local and domain users, group memberships, and account policies without requiring additional tools.

## Description

In a compromised Windows environment, attackers often enumerate users and privileges to map the attack surface, identify high-privilege accounts, and spot misconfigurations for escalation. This procedure covers local user discovery, privilege checks, group enumeration (especially Administrators), account policy review, and domain controller identification. It applies to both standalone and domain-joined systems, helping to determine if the current user has admin rights or can target others. The technique relies on native Windows utilities accessible via Command Prompt or PowerShell, making it stealthy and low-footprint. Expected outcomes include lists of users, their statuses, group memberships, and policy details that reveal weak passwords or unlocked accounts for further exploitation.

## Requirements

1. Authenticated access to a Windows system (local or remote shell like PowerShell or CMD)
2. Command line interface (CMD or PowerShell) with basic user privileges
3. For domain-related commands (nltest), domain-joined system or valid domain credentials
4. No external tools required; all use built-in Windows binaries

## Defense

- Implement least privilege: Restrict non-admin users from running enumeration commands via AppLocker or group policies
- Enable advanced auditing: Log process creation and command execution (Event IDs 4688, 4689) to detect whoami, net, and nltest usage
- Use Windows Defender or EDR tools to monitor for anomalous user queries and privilege checks
- Enforce strong account policies: Minimum password lengths, lockouts, and regular audits of admin groups

## Objectives

1. Identify all local and domain users, their statuses, and last logons to find active targets
2. Check current user privileges and group memberships to assess escalation potential
3. Enumerate groups, especially Administrators, to map high-privilege accounts
4. Review account policies for brute-force opportunities or weak configurations
5. Discover domain controllers for lateral movement planning

## Instructions

### Step 1: Retrieve Current Username

**Context**: Start by identifying the current user's identity, which provides context for subsequent enumeration and helps confirm the session.

Execute the following in PowerShell or CMD to get the username via environment variables or whoami.

```powershell
whoami || echo $env:USERNAME
```

This combines cross-shell compatibility. Why: Establishes baseline identity before deeper queries.

**Expected Output**: Displays the current username, e.g., "DOMAIN\username" or "computername\username".

### Step 2: Check User Privileges and Groups

**Context**: Query the current user's privileges and group memberships to determine access levels, such as SeDebugPrivilege or admin group inclusion, indicating escalation viability.

Use [[commands/whoami-privileges-windows]] to list privileges:

```cmd
whoami /priv
```

Then [[commands/whoami-groups-windows]] for groups:

```cmd
whoami /groups
```

Why: Privileges show enabled/disabled rights (e.g., SeImpersonatePrivilege for escalation); groups reveal roles like Domain Admins.

**Expected Output**: Privilege list with states (Enabled/Disabled); group list with SIDs and attributes (e.g., "BUILTIN\Administrators (RID: S-1-5-32-544)").

### Step 3: Enumerate All Local Users

**Context**: List all local users, their enabled status, last logon, and user directories to identify dormant or service accounts for targeting.

Reference [[codes/enumerate-local-users-powershell]] for a comprehensive script:

This runs net user for basic info, whoami /all for current details, Get-LocalUser for statuses, and directory listing for profiles.

Why: Combines legacy and modern cmdlets for complete coverage, revealing hidden or disabled accounts.

**Expected Output**: Table of users with Name, Enabled (True/False), LastLogon dates; list of C:\Users directories.

### Step 4: Review Account Policies

**Context**: Examine password and lockout policies to assess brute-force feasibility or policy weaknesses.

Use [[commands/net-accounts-policy]]:

```cmd
net accounts
```

Why: Reveals min length, age, history, and lockout thresholds; weak policies (e.g., no lockout) enable attacks.

**Expected Output**: Policy details like "Minimum password length: 7", "Lockout threshold: Never".

### Step 5: Query Specific User Details

**Context**: Get detailed info on key accounts like Administrator to check password age, status, and comments for clues.

Use [[commands/net-user-admin-query]] with variations for admin users:

```cmd
net user administrator
net user %USERNAME%
```

Why: Targets built-in or current user for last password set, account active status, and expiration.

**Expected Output**: User info like "Full Name", "Account active: Yes", "Password last set: [date]", "Password expires: Never".

### Step 6: List Local Groups

**Context**: Enumerate all local groups to understand role separations beyond users.

Execute in PowerShell:

```powershell
net localgroup
Get-LocalGroup | Format-Table Name
```

Why: Identifies custom groups that might hold privileges; complements user enumeration.

**Expected Output**: List like "*Administrators", "*Guests", "*Users" in table format.

Use [[commands/net-localgroup-list]] for CMD equivalent.

### Step 7: Enumerate Administrators Group Members

**Context**: Specifically check Administrators group membership to find escalation targets or confirm current access.

Reference [[codes/list-administrators-group-members]]:

This queries net localgroup and Get-LocalGroupMember for English/French variants.

Why: Admin group grants full control; listing members reveals over-privileged users.

**Expected Output**: Members like "DOMAIN\adminuser (Local)", with PrincipalSource.

### Step 8: Discover Domain Controllers

**Context**: If domain-joined, identify DCs for targeting replication or further enumeration.

Reference [[codes/discover-domain-controllers-nltest]] for combined queries, or use individual commands:

[[commands/nltest-dclist-domain]]:

```cmd
nltest /dclist:$_DOMAIN_NAME
```

[[commands/nltest-dcname-domain]]:

```cmd
nltest /dcname:$_DOMAIN_NAME
```

[[commands/nltest-dsgetdc-domain]]:

```cmd
nltest /dsgetdc:$_DOMAIN_NAME
```

Why: DCs hold domain creds; locating them enables Kerberoasting or DCSync attacks.

**Expected Output**: DC list with IPs/sites, e.g., "DC: dc01.domain.com Site: Default-First-Site-Name".
