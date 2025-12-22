---
id: 496410c0-15dc-4442-b904-fbd41c1e8ad7
name: Abuse-WriteDACL-to-Grant-Group-Membership-Permissions
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:06.859369+00:00'
updated_at: '2023-04-10T20:36:10.606929+00:00'
tactics:
  - '[[Credential Access]]'
  - '[[Discovery]]'
  - '[[Persistence]]'
techniques:
  - '[[Account Manipulation]]'
  - '[[Permission Groups Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Abusing Active Directory ACLs/ACEs]]'
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/WriteDACL]]'
commands:
  - '[[commands/add-writemembers-acl-to-interesting-group-for-user1]]'
  - '[[commands/add-user1-to-interesting-group-via-net]]'
  - '[[commands/set-genericall-permission-on-interesting-group-via-bloodyad]]'
  - '[[commands/remove-genericall-permission-on-interesting-group-via-bloodyad]]'
platforms:
  - Windows
  - Active Directory
tools: []
validated: true
---

# Abuse-WriteDACL-to-Grant-Group-Membership-Permissions

## Summary

This procedure demonstrates how to abuse WriteDACL permissions in Active Directory to grant a user (e.g., User1) the ability to modify membership of an interesting group (e.g., INTERESTING_GROUP), such as an admin or privileged group. By adding a WriteMembers access control entry (ACE) to the group's security descriptor, the attacker can then add themselves or others to the group, escalating privileges. This is commonly used in lateral movement or persistence scenarios within domain environments.

## Description

In Active Directory, WriteDACL permission allows modification of an object's Discretionary Access Control List (DACL), enabling the addition of custom ACEs. This procedure leverages tools like PowerView (via Add-DomainObjectAcl) to grant WriteMembers rights to a target user on a sensitive group, followed by adding the user to the group. Additionally, it covers setting GenericAll (full control) permissions using the bloodyAD.py script for broader access. The target environment is a Windows domain with Active Directory Domain Services (AD DS). Prerequisites include valid credentials with existing WriteDACL access on the target group. Success allows unauthorized group membership changes, potentially leading to privilege escalation, data access, or persistence. From a defender's perspective, this highlights the risks of misconfigured ACLs on privileged groups.

## Requirements

1. Valid domain credentials with WriteDACL permission on the target group (e.g., via prior enumeration of ACLs).
2. Access to a Windows machine joined to the domain or a Linux machine with network access to the domain controller.
3. Installed tools: PowerView module (for PowerShell commands) or Impacket suite (for bloodyAD.py).
4. Network connectivity to the domain controller (ports 445/TCP for SMB, 389/TCP for LDAP).

## Defense

- Implement least privilege: Regularly audit and remove unnecessary WriteDACL permissions on sensitive objects using tools like BloodHound or AD auditing.
- Enable advanced auditing for directory service changes to log ACL modifications.
- Use protected groups (AdminSDHolder) to prevent unauthorized changes on high-privilege groups.
- Monitor for anomalous group membership changes via SIEM rules on Event IDs 4728/4732.

## Objectives

1. Grant WriteMembers permission to a user on a target group to enable membership modifications.
2. Add the user to the group for immediate access.
3. Optionally grant or revoke GenericAll (full control) for advanced manipulation.
4. Achieve persistence or escalation by controlling group-based access to resources.

## Instructions

### Step 1: Grant WriteMembers ACL to User on Target Group

**Context**: This step abuses existing WriteDACL access to add an ACE granting the target user (e.g., User1) the WriteMembers right on the interesting group. WriteMembers allows modifying group membership without full ownership. Use PowerView's Add-DomainObjectAcl cmdlet, which requires loading the module first (e.g., Import-Module PowerView.ps1).

**Command** ([[commands/add-writemembers-acl-to-interesting-group-for-user1]]):
```powershell
Add-DomainObjectAcl -TargetIdentity "$_GROUP_NAME" -Rights WriteMembers -PrincipalIdentity "$_USER_NAME"
```

> This PowerShell command modifies the group's DACL to include the specified principal with WriteMembers rights. Run it from a domain-joined Windows machine with the credentials that have WriteDACL on the group. Expected output includes confirmation of the ACE addition, such as "Access control entry added successfully."

### Step 2: Add User to the Target Group

**Context**: With WriteMembers now granted, add the user to the group to gain membership benefits (e.g., access to restricted resources). This uses the native net command, which leverages the new permission.

**Command** ([[commands/add-user1-to-interesting-group-via-net]]):
```cmd
net group "$_GROUP_NAME" "$_USER_NAME" /add /domain
```

> Execute this from a command prompt with the user's credentials. The /domain flag ensures domain context. Expected output: "The command completed successfully." Verify membership with `net group "$_GROUP_NAME" /domain`.

### Step 3: Set GenericAll Permission on the Group

**Context**: For full control (including DACL modifications), use bloodyAD.py from the Impacket suite to grant GenericAll to a user (e.g., devil_user1). This requires LDAP access and is useful if WriteDACL is insufficient. Install Impacket via `pip install impacket` if needed.

**Command** ([[commands/set-genericall-permission-on-interesting-group-via-bloodyad]]):
```bash
python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$GROUP_NAME,dc=$_DOMAIN"
```

> This sets full control for the target user on the group's DN. Run from a Linux machine with network access. Expected output: Confirmation like "GenericAll set successfully for [user] on [group]." Use the principal's credentials with sufficient access.

### Step 4: Remove GenericAll Permission (Cleanup or Reversal)

**Context**: To revoke the GenericAll right, rerun the bloodyAD.py command with the False flag. This is essential for opsec or testing reversal.

**Command** ([[commands/remove-genericall-permission-on-interesting-group-via-bloodyad]]):
```bash
python bloodyAD.py -U "$_USERNAME" -P "$_PASSWORD" --host $_DC_HOST -d $_DOMAIN setGenericAll "$_TARGET_USER" "cn=$GROUP_NAME,dc=$_DOMAIN" False
```

> Similar to Step 3, but adds False to remove the permission. Expected output: "GenericAll removed successfully."

### Step 5: Verify Changes

**Context**: Confirm the permissions and membership took effect to ensure success.

**Instructions**: Query the group's members with `net group "$_GROUP_NAME" /domain` and check ACLs using `Get-DomainObjectAcl -Identity "$_GROUP_NAME"` (PowerView). If successful, the user should appear in the membership list, and ACLs should reflect the new ACEs.
