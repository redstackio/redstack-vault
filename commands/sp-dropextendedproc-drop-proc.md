---
type: command
executor: sql
data: sp_dropextendedproc 'xp_calc'
tags:
  - mssql
  - cleanup
platforms:
  - Windows
verified: true
validated: true
---

# sp-dropextendedproc-drop-proc

## Command

```sql
sp_dropextendedproc 'xp_calc'
```

## Description

This command removes a registered extended stored procedure from SQL Server, unloading its associated DLL and cleaning up metadata. It is essential for post-execution cleanup to evade detection in audits or logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'xp_calc' | Name of the extended stored procedure to drop | Yes |

## Examples

### Basic Usage

```sql
sp_dropextendedproc 'xp_calc'
```

## Expected Output

Command(s) completed successfully.

No output on success. Verify with:
```sql
SELECT * FROM sys.extended_procedures WHERE name = 'xp_calc'
```
Expected: No rows returned.

Errors: 'There is no extended stored procedure by that name' if not present.

## Related

- [[procedures/Load-DLL-Using-sp_addextendedproc]]
- [[commands/exec-extended-proc]]
