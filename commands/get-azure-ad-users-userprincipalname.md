---
id: b761ecd6-34e2-43a9-9f45-c3957e851486
name: get-azure-ad-users-userprincipalname
type: command
executor: powershell
data: Get-AzureADUser -All $true | Select-Object UserPrincipalName
output: null
created_at: '2023-05-23T19:33:22.164808+00:00'
updated_at: '2023-05-23T19:33:22.785549+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - enumeration
  - users
verified: true
validated: true
---

# Get Azure AD Users UserPrincipalName

## Command

```powershell
Get-AzureADUser -All $true | Select-Object UserPrincipalName
```

## Description

Extracts only the User Principal Names from all Azure AD users, providing a concise list of emails for targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Retrieves all users | Built-in |
| Select-Object | PowerShell cmdlet to project specific properties | Built-in |
| UserPrincipalName | Property to select (email-like identifier) | Built-in |

## Examples

### Basic Usage

```powershell
Get-AzureADUser -All $true | Select-Object UserPrincipalName
```

### Advanced Usage

Export to file: Get-AzureADUser -All $true | Select-Object UserPrincipalName | Export-Csv -Path users.csv -NoTypeInformation

## Expected Output

UserPrincipalName
-----------------
john.doe@contoso.onmicrosoft.com
jane.smith@contoso.onmicrosoft.com
guest@external.com

## Related

- [[procedures/azure-ad-enumeration-using-powershell-with-credentials]]
- [[commands/get-all-azure-ad-users]]
