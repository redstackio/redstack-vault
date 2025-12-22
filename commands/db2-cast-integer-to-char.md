---
id: cccc8d58-d116-4c99-8141-02d03758375c
name: db2-cast-integer-to-char
type: command
executor: sql
data: select cast(1 as char) from sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.991217+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - db2
  - casting
  - sqli
verified: true
validated: true
---

# db2-cast-integer-to-char

## Command

```sql
select cast(1 as char) from sysibm.sysdummy1;
```

## Description

This command converts an integer literal to a character (string) type in DB2 using CAST. It is applied against the dummy table and helps in obfuscating numeric payloads or extracting data in string contexts during SQL injection attacks exploiting type mismatches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `1` | The integer value to cast (can be a subquery result for advanced use) | Yes |
| `char` | Target data type for conversion | Yes |
| `sysibm.sysdummy1` | Dummy table to avoid impacting production data | Yes |

## Examples

### Basic Usage

```sql
select cast(1 as char) from sysibm.sysdummy1;
```

### Advanced Usage (Data Exfiltration Simulation)

```sql
select cast((SELECT COUNT(*) FROM users) as char) from sysibm.sysdummy1;
```

## Expected Output

Returns the value as a string, e.g., '1'.

```
1
----
 1

  1 record(s) selected.
```

## Related

- [[procedures/DB2-Integer-Conversion-SQL-Injection]]
- [[commands/db2-cast-string-to-integer]]
