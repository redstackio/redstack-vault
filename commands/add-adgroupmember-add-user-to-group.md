---
id: 9c67f68f-b996-436c-a1de-4b4041440435
name: add-adgroupmember-add-user-to-group
type: command
executor: powershell
data: >-
  Add-ADGroupMember -Identity $_GROUP_NAME -Members $_USER -Credential
  $Credential
output: null
created_at: '2023-01-12T17:29:54.226094+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - powershell
verified: true
validated: true
---

# add-adgroupmember-add-user-to-group

## Command

```powershell
Add-ADGroupMember -Identity $_GROUP_NAME -Members $_USER -Credential $Credential
```

## Description

This PowerShell command adds a specified user to an Active Directory group using provided credentials. It is used in scenarios where the operator has delegated permissions to modify group memberships, enabling privilege escalation or persistence.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity $_GROUP_NAME | The name, GUID, or distinguished name of the target group (e.g., 'Domain Admins') | Yes |
| -Members $_USER | The user(s) to add, specified by name, SID, or DN (e.g., 'attackeruser') | Yes |
| -Credential $Credential | PSCredential object for authentication (created via New-Object PSCredential) | Yes |

## Examples

### Basic Usage

```powershell
Add-ADGroupMember -Identity 'Domain Admins' -Members 'attackeruser' -Credential $Cred
```

### Advanced Usage

```powershell
Add-ADGroupMember -Identity 'CN=Domain Admins,CN=Users,DC=example,DC=com' -Members @('user1','user2') -Credential $Cred -PassThru
```

## Expected Output

The command completed successfully.

If -PassThru is used, it returns the added member object:

SamAccountName : attackeruser
SID             : S-1-5-21-...-1001
...

Errors may include 'Access is denied' if permissions are insufficient.

## Related

- [[procedures/Add-User-to-Group-Using-ADModule-With-Credentials]]
