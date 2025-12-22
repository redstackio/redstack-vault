---
id: c0d65753-4e05-4b51-b177-90ae5367f0b7
type: command
executor: powershell
data: Set-Role -Role $_ROLE -User $_USER -Resource $_RESOURCE
output: null
created_at: '2023-04-06T03:56:14.587034+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - role
  - rbac
verified: true
validated: true
---

# powerzure-set-role-on-resource

## Command

```powershell
Set-Role -Role $_ROLE -User $_USER -Resource $_RESOURCE
```

## Description

Assigns a role to a user on an Azure resource using Owner privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Role, $_ROLE | Role name (e.g., Contributor) | Yes |
| -User, $_USER | User email | Yes |
| -Resource, $_RESOURCE | Resource name | Yes |

## Examples

### Basic Usage

```powershell
Set-Role -Role Contributor -User test@contoso.com -Resource Win10VMTest
```

## Expected Output

Role assignment confirmation.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]
