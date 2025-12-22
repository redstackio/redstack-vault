---
id: ae82a731-3119-4ab3-a44e-013f169c1389
name: add-user-to-automation-admins-group
type: command
executor: powershell
data: >-
  Add-AzureADGroupMember -ObjectId $_GROUP_OBJECT_ID -RefObjectId
  $_USER_OBJECT_ID -Verbose
output: null
created_at: '2023-05-24T22:50:53.199630+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - privilege-escalation
verified: true
validated: true
---

# add-user-to-automation-admins-group

## Command

```powershell
Add-AzureADGroupMember -ObjectId $_GROUP_OBJECT_ID -RefObjectId $_USER_OBJECT_ID -Verbose
```

## Description

This PowerShell command adds a user to an Azure AD group, such as "Automation Admins", to elevate privileges for accessing and managing Azure Automation Accounts. Use it when initial access is limited but group modification is possible.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_GROUP_OBJECT_ID | The Object ID of the target Azure AD group (e.g., Automation Admins) | Yes |
| $_USER_OBJECT_ID | The Object ID of the user to add as a member | Yes |
| -Verbose | Provides detailed output during execution | No |

## Examples

### Basic Usage

```powershell
Add-AzureADGroupMember -ObjectId "group-obj-id" -RefObjectId "user-obj-id" -Verbose
```

### Advanced Usage

Combine with Get-AzureADGroup to dynamically fetch IDs before adding.

## Expected Output

Verbose output confirming the user was added to the group, including details like group name and member count. Success looks like: "User added to group successfully."

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/get-user-role-on-automation-account]]
