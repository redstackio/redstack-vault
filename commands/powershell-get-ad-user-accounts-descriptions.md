---
id: new-id-for-powershell
name: powershell-get-ad-user-accounts-descriptions
type: command
executor: powershell
data: >-
  Get-WmiObject -Class Win32_UserAccount -Filter "Domain='$_DOMAIN' AND
  Disabled='False'" | Select Name, Domain, Description
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - ad-enumeration
  - wmi
verified: true
validated: true
---

# powershell-get-ad-user-accounts-descriptions

## Command

```powershell
Get-WmiObject -Class Win32_UserAccount -Filter "Domain='$_DOMAIN' AND Disabled='False'" | Select Name, Domain, Description
```

## Description

This PowerShell command queries WMI for active domain user accounts and selects their descriptions to check for embedded credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Class Win32_UserAccount | WMI class for user accounts | Built-in |
| -Filter "Domain='$_DOMAIN' AND Disabled='False'" | Filter for active domain users | Yes |
| Select Name, Domain, Description | Fields to output | Built-in |
| $_DOMAIN | Target domain name | Yes |

## Examples

### Basic Usage

```powershell
Get-WmiObject -Class Win32_UserAccount -Filter "Domain='LAB' AND Disabled='False'" | Select Name, Domain, Description
```

## Expected Output

```
Name    Domain Description
----    ------ -----------
admin   LAB    Secret: Pass123
```

## Related

- [[procedures/Enumerate-Passwords-in-AD-User-Descriptions]]
- [[commands/enum4linux-grep-user-descriptions]]
