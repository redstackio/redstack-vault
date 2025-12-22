---
id: cmd-sqlmap-enum-dbs-001
data: sqlmap -r request.txt --dbs --batch
tags:
  - sqli
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.146Z'
verified: false
validated: true
submitted: true
---
# sqlmap-enum-dbs

## Command

```bash
sqlmap -r request.txt --dbs --batch
```

## Description

This command exploits a SQL injection point to enumerate all database names on the target DBMS, useful after vulnerability confirmation for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-r request.txt` | Load HTTP request from file | Yes |
| `--dbs` | Enumerate DBMS databases | Yes |
| `--batch` | Non-interactive mode | No |

## Examples

### Basic Usage

```bash
sqlmap -r request.txt --dbs
```

### Advanced Usage

```bash
sqlmap -r request.txt --dbs --batch --threads=5
```

## Expected Output

A list of databases, e.g., "Database: sony_main\nDatabase: users_db", indicating successful schema extraction.

## Related

- [[Related Procedure: Enumerate-Database-Names-via-SQL-Injection]]
