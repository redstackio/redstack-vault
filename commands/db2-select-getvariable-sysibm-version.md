---
id: d76b9034-c728-4c98-bb90-7ee6112bae94
name: db2-select-getvariable-sysibm-version
type: command
executor: sql
data: select getvariable('sysibm.version') from sysibm.sysdummy1 -- (v8+)
output: null
created_at: '2023-04-06T03:56:32.535787+00:00'
updated_at: '2023-04-10T20:21:57.272196+00:00'
platforms:
  - Database
  - DB2
tags:
  - db2
  - version
  - recon
verified: true
validated: true
---

# db2-select-getvariable-sysibm-version

## Command

```sql
select getvariable('sysibm.version') from sysibm.sysdummy1; -- (v8+)
```

## Description

This SQL command uses the GETVARIABLE function in DB2 (version 8+) to retrieve the product version string from the SYSIBM.VARIABLE registry. It's a lightweight way to get version info without table scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'sysibm.version' | Fixed variable name for DB2 version | N/A |
| sysibm.sysdummy1 | Dummy table to enable the scalar function | N/A |

## Examples

### Basic Usage

```sql
select getvariable('sysibm.version') from sysibm.sysdummy1;
```

## Expected Output

```
1
GETVARIABLE('SYSIBM.VERSION')
-----------------------------
DB2 v11.5.7.0
```

Returns a string like 'DB2 v11.5.7.0' detailing the full product version.

## Related

- [[procedures/Extract-DB2-Database-Version-Information]]
