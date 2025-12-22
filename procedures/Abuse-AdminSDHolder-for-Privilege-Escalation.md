---
id: 9b6cf7c4-f65f-4271-a3f1-7474fd19e3a5
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.441626+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Account Manipulation]]'
  - '[[Group Policy Modification]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Active Directory Groups]]'
  - '[[tags/AdminSDHolder Abuse]]'
commands:
  - '[[commands/backup-adminsdholder-descriptor]]'
  - '[[commands/add-full-control-acl-to-adminsdholder]]'
  - '[[commands/grant-all-rights-to-adminsdholder]]'
  - '[[commands/grant-reset-password-right-on-user]]'
  - '[[commands/modify-adminsdholder-propagation]]'
  - '[[commands/restore-adminsdholder-descriptor]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Abuse-AdminSDHolder-for-Privilege-Escalation

## Summary

This procedure exploits the AdminSDHolder object in Active Directory to escalate privileges by modifying its access control list (ACL) to grant an attacker full control or specific rights, which then propagate to protected groups like Administrators and Domain Admins via the SDProp process. This allows unauthorized access to sensitive accounts, password resets, or full domain control, bypassing standard protections on privileged groups.

## Description

AdminSDHolder is a predefined security descriptor in Active Directory stored under CN=AdminSDHolder,CN=System,DC=domain,DC=com. It serves as a template that the SDProp.exe process applies every hour (or manually) to all protected groups and users, such as Built-in Administrators and Domain Admins, to enforce strict permissions and prevent unauthorized modifications. An attacker with sufficient initial privileges (e.g., delegated rights or another admin account) can abuse this by adding their own user or a controlled account to the AdminSDHolder ACL with Full Control or specific rights like Reset Password. Once propagated, these rights apply to all protected objects, enabling privilege escalation, persistence, or lateral movement. This technique is effective in environments with misconfigured delegation or where the attacker has write access to AD objects. It requires domain-joined access and can be detected through AD change auditing.

## Requirements

1. Valid domain credentials with permissions to modify AD objects (e.g., via another admin account or delegated rights).
2. Access to a domain controller or machine with AD PowerShell modules (e.g., ActiveDirectory or PowerView/PowerSploit).
3. PowerShell execution policy allowing script execution; SDProp requires running on a DC.
4. Knowledge of the target domain's DN structure (e.g., DC=domain,DC=local).

## Defense

- Monitor changes to the AdminSDHolder object and protected groups using AD auditing (Event IDs 4624, 4670, 4728).
- Implement least privilege by restricting who can modify AD schema or system objects.
- Regularly review ACLs on critical AD objects and enable Protected Users group for high-privilege accounts.
- Use tools like BloodHound to detect anomalous permission paths leading to AdminSDHolder.

## Objectives

1. Escalate privileges by gaining control over protected AD groups.
2. Enable actions like password resets on admin accounts for persistence or lateral movement.
3. Maintain access by propagating custom ACLs across the domain.

## Instructions

### Step 1: Backup the Current AdminSDHolder Descriptor

**Context**: Before making modifications, back up the existing security descriptor to allow restoration if needed. This uses SDProp to create a backup without verbose output.

**Command** ([[commands/backup-adminsdholder-descriptor]]):
```powershell
SDProp /backup /quiet
```

> This command runs on a domain controller and silently backs up the AdminSDHolder template. It ensures you can revert changes to avoid permanent misconfigurations.

### Step 2: Add Full Control ACL to AdminSDHolder for Attacker User

**Context**: Grant the attacker's user full control over the AdminSDHolder object using PowerView or similar module. This allows propagation of rights to protected groups.

**Command** ([[commands/add-full-control-acl-to-adminsdholder]]):
```powershell
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=$_DOMAIN" -PrincipalIdentity $_USERNAME -Rights All -Verbose
```

> The command adds an ACL entry for the specified principal (username) with all rights on the AdminSDHolder object. Replace $_DOMAIN with your domain (e.g., domain,local) and $_USERNAME with the target user. Verbose output confirms the addition.

### Step 3: Grant Specific Rights Example - Reset Password on Target User

**Context**: As an example of targeted right abuse, grant a controlled account (titi) the ability to reset passwords on a high-privilege user (toto). This can be part of broader escalation.

**Command** ([[commands/grant-reset-password-right-on-user]]):
```powershell
Add-ObjectACL -TargetSamAccountName $_TARGET_ACCOUNT -PrincipalSamAccountName $_PRINCIPAL_ACCOUNT -Rights ResetPassword
```

> This adds a specific ACL for password reset rights. Use this after gaining broader access via AdminSDHolder. Expected success: No errors, rights applied immediately.

### Step 4: Grant All Rights to Another Account on AdminSDHolder

**Context**: Similar to Step 2, grant all rights to a different controlled account (e.g., toto) on the AdminSDHolder object for redundancy or testing.

**Command** ([[commands/grant-all-rights-to-adminsdholder]]):
```powershell
Add-ObjectAcl -TargetADSprefix "CN=AdminSDHolder,CN=System" -PrincipalSamAccountName $_PRINCIPAL_ACCOUNT -Verbose -Rights All
```

> This uses a different syntax (possibly from another module) to add full rights. The prefix targets the object directly. Verbose mode shows details of the ACL change.

### Step 5: Force Propagation of Modified Descriptor

**Context**: Trigger the SDProp process to apply the new ACL from AdminSDHolder to all protected objects immediately, rather than waiting for the hourly cycle.

**Command** ([[commands/modify-adminsdholder-propagation]]):
```powershell
SDProp /modify /quiet
```

> Run this on the PDC emulator or any DC to propagate changes silently. It applies the template to all protected users/groups, activating the new rights.

### Step 6: Restore Previous Descriptor if Needed

**Context**: If testing or cleanup is required, restore the backed-up descriptor to revert changes and avoid detection.

**Command** ([[commands/restore-adminsdholder-descriptor]]):
```powershell
SDProp /restore /quiet
```

> This silently restores the previously backed-up AdminSDHolder template, removing custom ACLs.

**Expected Output**: For all steps, successful execution shows no errors in PowerShell output. Verbose commands display details like "ACE added successfully." Propagation may take seconds; verify by checking group memberships or attempting privileged actions (e.g., password reset on an admin account).
