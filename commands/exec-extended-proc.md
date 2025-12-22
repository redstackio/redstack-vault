---
type: command
executor: sql
data: EXEC xp_calc
tags:
  - mssql
  - execution
platforms:
  - Windows
verified: true
validated: true
---

# exec-extended-proc

## Command

```sql
EXEC xp_calc
```

## Description

This command executes a loaded extended stored procedure in SQL Server, running the associated DLL's code in the server process context. It is used after loading a custom DLL to trigger its functionality, such as calculations, system commands, or payload delivery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| xp_calc | Name of the extended stored procedure to execute | Yes |

## Examples

### Basic Usage

```sql
EXEC xp_calc
```

### With Parameters (if DLL supports)

```sql
EXEC xp_calc 'param1', 42
```

## Expected Output

Output varies by DLL implementation. For a sample calc DLL:
1 + 1 = 2

For malicious DLLs, output may be empty, but check for side effects like network connections or log entries. Errors: 'Could not find stored procedure xp_calc' if not loaded.

## Related

- [[procedures/Load-DLL-Using-sp_addextendedproc]]
- [[commands/sp-addextendedproc-load-dll]]
