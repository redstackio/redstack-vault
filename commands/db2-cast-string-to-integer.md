---
id: 55450309-81ab-4d69-8e8e-8a76d4ff049f
name: db2-cast-string-to-integer
type: command
executor: sql
data: select cast('123' as integer) from sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.991165+00:00'
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

# db2-cast-string-to-integer

## Command

```sql
select cast('123' as integer) from sysibm.sysdummy1;
```

## Description

This command demonstrates converting a string literal to an integer type in DB2 using the CAST function. It queries the system dummy table to return the converted value, useful for testing type conversion behavior in SQL injection scenarios where string inputs need to mimic integers to bypass validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'123'` | The string value to cast (replace with injection payload for exploitation) | Yes |
| `integer` | Target data type for conversion | Yes |
| `sysibm.sysdummy1` | Dummy table for execution without affecting real data | Yes |

## Examples

### Basic Usage

```sql
select cast('123' as integer) from sysibm.sysdummy1;
```

### Advanced Usage (Injection Simulation)

```sql
select cast('1; DROP TABLE users--' as integer) from sysibm.sysdummy1;
```

## Expected Output

A single row with the integer value 123 (or error if invalid conversion). For example:

```
1
-----------
         123

  1 record(s) selected.
```

## Related

- [[procedures/DB2-Integer-Conversion-SQL-Injection]]
- [[commands/db2-cast-integer-to-char]]
