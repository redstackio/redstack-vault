---
id: 19cf629a-9b36-4863-b29f-f89fe75ca4aa
name: Add-User-to-Group-Using-ADModule-With-Credentials
type: procedure
verified: true
submitted: false
created_at: '2023-01-12T17:29:54.291622+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[Persistence]]'
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Manipulation]]'
sub_techniques: []
tags:
  - persistence
  - privilege-escalation
  - active-directory
  - powershell
commands:
  - '[[commands/add-adgroupmember-add-user-to-group]]'
platforms:
  - Windows
tools: []
validated: true
---

# Add-User-to-Group-Using-ADModule-With-Credentials

## Summary

This procedure demonstrates how to add a user to an Active Directory group using the ActiveDirectory PowerShell module with provided credentials. It is useful in post-exploitation scenarios where an attacker has obtained credentials with sufficient permissions (e.g., GenericAll on the target group) to modify group memberships, enabling persistence or privilege escalation by granting the user elevated access.

## Description

In Active Directory environments, group memberships control access to resources and privileges. If an attacker compromises credentials that allow modification of group memberships—such as through delegated permissions like GenericAll on a group—they can add a controlled user account to a privileged group (e.g., Domain Admins). This procedure uses the Add-ADGroupMember cmdlet from the ActiveDirectory module, which requires the RSAT-AD-PowerShell feature or domain-joined access. The technique assumes the attacker has valid credentials and is executed on a Windows system with PowerShell remoting or direct console access. Success grants the added user the group's permissions, potentially allowing lateral movement or data access. This maps to account manipulation for persistence or escalation in MITRE ATT&CK.

## Requirements

1. Windows system with ActiveDirectory PowerShell module installed (via RSAT tools or domain controller access).
2. Valid credentials with permissions to modify the target group (e.g., owner or GenericAll rights).
3. PowerShell execution policy allowing script runs (bypass if needed).
4. Network access to a domain controller for AD queries.

## Defense

Defensive measures and detection strategies:

- Monitor Active Directory changes via auditing (enable Group Membership auditing in AD).
- Use tools like Microsoft Advanced Threat Analytics or SIEM to alert on unexpected Add-ADGroupMember executions.
- Implement least privilege: Limit delegated permissions and review group owners regularly.
- Enable PowerShell logging (Module, Script Block) to capture cmdlet invocations.

## Objectives

1. Add a specified user to a target Active Directory group to gain elevated privileges.
2. Verify the membership change to confirm success.
3. Maintain persistence without triggering immediate alerts on high-privilege actions.

## Instructions

### Step 1: Import the ActiveDirectory Module and Establish Credentials

**Context**: Begin by importing the required module and creating a secure credential object using the provided username and password. This authenticates the session for AD operations without prompting interactively.

**Command** ([[commands/add-adgroupmember-add-user-to-group]]):
```powershell
$SecurePassword = ConvertTo-SecureString '$_PASSWORD' -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PSCredential('$_USERNAME', $SecurePassword)
Import-Module ActiveDirectory
```

> This step sets up the credential object ($_USERNAME and $_PASSWORD are placeholders for the attacker's obtained creds) and loads the module. Expected output: No errors; module import confirmation if verbose.

### Step 2: Add the User to the Target Group

**Context**: Use the Add-ADGroupMember cmdlet with the established credentials to append the user to the group. Specify the group identity and user via distinguished name or samAccountName for precision.

**Command** ([[commands/add-adgroupmember-add-user-to-group]]):
```powershell
Add-ADGroupMember -Identity $_GROUP_NAME -Members $_USER -Credential $Credential
```

> Replace $_GROUP_NAME with the target group (e.g., 'Domain Admins') and $_USER with the user (e.g., 'attackeruser'). This executes the addition under the provided creds. Expected output: 'The command completed successfully' or similar confirmation; no errors if permissions suffice.

### Step 3: Verify the Group Membership

**Context**: Confirm the addition by querying the group's members to ensure the user was added, validating the persistence mechanism.

**Command** ([[commands/add-adgroupmember-add-user-to-group]]):
```powershell
Get-ADGroupMember -Identity $_GROUP_NAME -Credential $Credential | Where-Object {$_.SamAccountName -eq $_USER}
```

> This lists members and filters for the added user. Expected output: Details of the user object if successful, including name and SID; empty if failed.
