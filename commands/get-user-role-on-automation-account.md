---
id: e6a66c0b-2934-40d9-9b96-97367504fb54
name: get-user-role-on-automation-account
type: command
executor: powershell
data: >-
  Get-AzRoleAssignment -Scope
  /subscriptions/$_SUBSCRIPTION_ID/resourceGroups/$_RESOURCE_GROUP_NAME/providers/Microsoft.Automation/automationAccounts/$_AUTOMATION_ACCOUNT_NAME
output: null
created_at: '2023-05-24T22:50:53.200677+00:00'
updated_at: '2023-05-24T22:50:54.391095+00:00'
platforms:
  - Cloud
tags:
  - azure
  - discovery
verified: true
validated: true
---

# get-user-role-on-automation-account

## Command

```powershell
Get-AzRoleAssignment -Scope /subscriptions/$_SUBSCRIPTION_ID/resourceGroups/$_RESOURCE_GROUP_NAME/providers/Microsoft.Automation/automationAccounts/$_AUTOMATION_ACCOUNT_NAME
```

## Description

This Azure PowerShell command retrieves role assignments for a specific Automation Account scope, helping verify if the user has sufficient privileges (e.g., Contributor) to create and run runbooks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SUBSCRIPTION_ID | Azure subscription ID | Yes |
| $_RESOURCE_GROUP_NAME | Resource group name | Yes |
| $_AUTOMATION_ACCOUNT_NAME | Automation Account name | Yes |

## Examples

### Basic Usage

```powershell
Get-AzRoleAssignment -Scope "/subscriptions/1234/resourceGroups/MyRG/providers/Microsoft.Automation/automationAccounts/MyAccount"
```

### Advanced Usage

Filter for current user: Get-AzRoleAssignment -Scope ... | Where-Object { $_.DisplayName -eq $env:USERNAME }

## Expected Output

Table of role assignments, e.g., Role: Contributor, PrincipalName: user@domain.com. Empty for no access.

## Related

- [[procedures/Create-and-Execute-Malicious-Azure-Runbook]]
- [[commands/add-user-to-automation-admins-group]]
