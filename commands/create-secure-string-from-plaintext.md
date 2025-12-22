---
id: 84f78f12-7740-4c96-bc62-7c083cd4bca5
name: create-secure-string-from-plaintext
type: command
executor: powershell
data: $password = "$_NEW_PASSWORD" | ConvertToSecureString -AsPlainText -Force
output: null
created_at: '2023-04-06T03:56:15.848056+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
  - Cloud
tags:
  - password-management
  - azure-ad
verified: true
validated: true
---

# create-secure-string-from-plaintext

## Command

```powershell
$password = "$_NEW_PASSWORD" | ConvertToSecureString -AsPlainText -Force
```

## Description

This command converts a plaintext password string into a secure string object in PowerShell, which is necessary for securely passing passwords to Azure AD cmdlets like password resets. Use this when preparing credentials for administrative actions in Azure AD.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NEW_PASSWORD | The plaintext password to convert | Yes |
| -AsPlainText | Treats input as plaintext (no encoding) | Yes |
| -Force | Suppresses confirmation prompts | Yes |

## Examples

### Basic Usage

```powershell
$password = "P@ssw0rd123" | ConvertToSecureString -AsPlainText -Force
```

### Advanced Usage

Combine with variable assignment for reuse:

```powershell
$newPass = Read-Host "Enter new password" -AsSecureString
$password = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($newPass))
```

## Expected Output

No direct output; creates a `SecureString` object in the `$password` variable. Verify with `$password.GetType()` showing `System.Security.SecureString`. Success if no errors and variable is populated.

## Related

- [[commands/set-azuread-user-password-by-upn]]
- [[procedures/Azure-AD-Administrative-Unit-Management]]
