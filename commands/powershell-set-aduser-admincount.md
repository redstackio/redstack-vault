---
type: command
executor: powershell
data: 'Set-ADUser -Identity $_TARGET_USER -Replace @{adminCount=1}'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - active-directory
  - modification
verified: true
validated: true
---

# powershell-set-aduser-admincount

## Command

```powershell
Set-ADUser -Identity $_TARGET_USER -Replace @{adminCount=1}
```

## Description

Modifies the AdminCount attribute on a specific user to 1, marking it as protected by AdminSDHolder.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Identity | sAMAccountName or DN of the target user | Yes |
| -Replace | Hashtable to set adminCount=1 | Yes |
| $_TARGET_USER | Target username (e.g., testuser) | Yes |

## Examples

### Basic Usage

```powershell
Set-ADUser -Identity testuser -Replace @{adminCount=1}
```

### Advanced Usage

```powershell
Set-ADUser -Identity testuser -Replace @{adminCount=1} -WhatIf
```

## Expected Output

```
# Silent success; verify with Get-ADUser -Identity testuser -Properties adminCount
```

## Related

- [[procedures/AdminCount-Abuse]]
- [[commands/powershell-get-aduser-admincount]]
