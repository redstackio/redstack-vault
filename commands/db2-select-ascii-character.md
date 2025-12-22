---
id: 5a29c994-a6c1-465e-8819-d25f3658a080
name: db2-select-ascii-character
type: command
executor: sql
data: select ascii('$_CHARACTER') from sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.965507+00:00'
updated_at: '2023-04-10T20:22:04.471021+00:00'
platforms:
  - Database
  - DB2
tags:
  - DB2
  - SQL Injection
  - ASCII
verified: true
validated: true
---

# db2-select-ascii-character

## Command

```sql
select ascii('$_CHARACTER') from sysibm.sysdummy1
```

## Description

This SQL command queries a DB2 database to retrieve the ASCII code value of a specified character using the built-in ASCII() function. It selects from the sysibm.sysdummy1 system table, which acts as a dummy row source for testing functions without needing a real table. Use this in SQL injection scenarios to convert characters to numeric values, bypassing filters that block direct strings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CHARACTER | The single character to convert to ASCII (e.g., 'A', '1') | Yes |
| sysibm.sysdummy1 | Fixed dummy table for row generation | Built-in |

## Examples

### Basic Usage

```sql
select ascii('A') from sysibm.sysdummy1
```

### Advanced Usage (in Injection Context)

```sql
select ascii(substr(user,1,1)) from sysibm.sysdummy1 -- Extract first char of 'user' table
```

## Expected Output

When executed successfully, the query returns a single integer value representing the ASCII code of the input character. For 'A':

```
ASCII
-----
65

1 record(s) selected.
```

If used in a blind injection, the output may be inferred via boolean responses (e.g., time delays or conditional errors) rather than direct display.

## Related

- [[procedures/DB2-SQL-Injection-Using-ASCII-Function]]
