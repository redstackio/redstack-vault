---
id: f7577401-5977-4544-9488-6b1d661f7342
name: get-user-with-specific-string-in-description
type: command
executor: powershell
data: >-
  Get-ADUser -Filter 'Description -like "*wtver*"' -Properties Description |
  Select-Object Name, Description
output: null
created_at: '2023-04-06T03:56:02.419468+00:00'
updated_at: '2023-04-10T20:36:08.324465+00:00'
platforms:
  - Windows
tags:
  - ad-recon
  - user-enumeration
verified: true
validated: true
---

# get-user-with-specific-string-in-description

## Command

```powershell
Get-ADUser -Filter 'Description -like "*$_SearchString*"' -Properties Description | Select-Object Name, Description
```

## Description

Searches for users whose description contains a specific string pattern.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Filter 'Description -like "*$_SearchString*"' | LDAP filter for description match | Yes |
| -Properties Description | Includes description attribute | Yes |
| Select-Object Name, Description | Limits output fields | Yes |

## Examples

### Basic Usage

```powershell
Get-ADUser -Filter 'Description -like "*admin*"' -Properties Description | Select-Object Name, Description
```

## Expected Output

Matching users:

```
Name        Description
----        -----------
AdminUser   Admin access
```

## Related

- [[procedures/active-directory-recon-using-ad-module]]
- [[commands/get-all-properties-of-specific-user]]
