---
id: b66c5b3d-8dfb-42c9-9b15-e5e917d49c6b
name: db2-concatenate-ascii-values
type: command
executor: sql
data: SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:33.067173+00:00'
updated_at: '2023-04-10T20:22:01.550894+00:00'
platforms:
  - Database
  - DB2
tags:
  - sql-injection
  - db2
  - ascii
verified: true
validated: true
---

# db2-concatenate-ascii-values

## Command

```sql
SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1
```

## Description

This SQL command in DB2 concatenates characters derived from ASCII values using the CHR() function and the || operator, forming a string without using quotes. It is used in SQL injection to bypass filters that block quoted strings, allowing construction of payloads for data extraction or manipulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| chr(65) | Converts ASCII 65 to 'A' | Yes |
| chr(68) | Converts ASCII 68 to 'D' | Yes |
| chr(82) | Converts ASCII 82 to 'R' | Yes |
| chr(73) | Converts ASCII 73 to 'I' | Yes |
| sysibm.sysdummy1 | Dummy table for single-row execution | Yes |

## Examples

### Basic Usage

```sql
SELECT chr(65)||chr(68)||chr(82)||chr(73) FROM sysibm.sysdummy1
```

### Advanced Usage

To form a space-padded string like 'ADRI ':

```sql
SELECT chr(65)||chr(68)||chr(82)||chr(73)||chr(32) FROM sysibm.sysdummy1
```

## Expected Output

```
ADRI

1 record(s) selected.
```

This output confirms the string 'ADRI' is formed successfully. In an injection context, expect application-specific responses like unauthorized data display or errors revealing structure.

## Related

- [[procedures/DB2-SQL-Injection-Using-ASCII-Concatenation]]
- [[codes/DB2-ASCII-Concatenation-Example]]
