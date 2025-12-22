---
id: 0c2024b6-a89a-4c87-82ab-3c2e58242407
name: mssql-xp-cmdshell-print-current-user
type: command
executor: sql
data: EXEC xp_cmdshell 'net user';
output: null
created_at: '2023-04-06T03:56:33.953633+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
platforms:
  - Windows
tags:
  - mssql
  - xp-cmdshell
  - recon
verified: true
validated: true
---

# mssql-xp-cmdshell-print-current-user

## Command

```sql
EXEC xp_cmdshell 'net user';
```

## Description

Executes 'net user' via xp_cmdshell to list local users on the Windows host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'net user' | Windows command to run | Yes |

## Examples

### Basic Usage

Run in SQL shell.

## Expected Output

Result set with user list:

| Output |
|--------|
| New local group added. |
| ... user accounts ... |

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
