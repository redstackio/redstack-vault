---
type: command
executor: powershell
data: $SecurePass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
platforms:
  - Windows
tags:
  - powershell
  - credentials
verified: true
validated: true
---

# PowerShell Create Secure String

## Command

```powershell
$SecurePass = ConvertTo-SecureString -String "$_PASSWORD" -AsPlainText -Force
```

## Description

This command converts a plain-text password string into a secure string object, which is required for secure credential handling in PowerShell scripts and modules like PowerView.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PASSWORD | The plain-text password to convert (e.g., "P@ssw0rd123") | Yes |

## Examples

### Basic Usage

```powershell
$SecurePass = ConvertTo-SecureString -String "secretpass" -AsPlainText -Force
```

### Advanced Usage

```powershell
$pass = Read-Host "Enter Password" -AsSecureString
# Or from variable
$plainPass = "complexpass!"
$SecurePass = ConvertTo-SecureString -String $plainPass -AsPlainText -Force
```

## Expected Output

No console output; the $SecurePass variable holds a System.Security.SecureString object. You can verify with: `$SecurePass.GetType()` showing SecureString.

## Related

- [[procedures/change-ad-domain-user-password]]
- [[commands/powershell-create-pscredential-object]]
