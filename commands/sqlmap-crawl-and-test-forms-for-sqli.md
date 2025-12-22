---
id: 7de45e0f-3a57-455c-8ebf-71348145a503
name: sqlmap-crawl-and-test-forms-for-sqli
type: command
executor: bash
data: >-
  sqlmap -u "$_TARGET_URL" --crawl=$_CRAWL_DEPTH --random-agent --batch --forms
  --threads=$_THREADS --level=5 --risk=3
output: null
created_at: '2023-04-06T03:56:36.369227+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sql-injection
  - web-scanning
verified: true
validated: true
---

# sqlmap-crawl-and-test-forms-for-sqli

## Command

```bash
sqlmap -u "$_TARGET_URL" --crawl=$_CRAWL_DEPTH --random-agent --batch --forms --threads=$_THREADS --level=5 --risk=3
```

## Description

This command uses SQLmap to perform an automated crawl of a web application starting from a base URL, testing forms and parameters for SQL injection vulnerabilities at a high thoroughness level. It is ideal for initial reconnaissance and detection in web pentesting, using multiple threads for speed and random user agents to mimic legitimate traffic.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target web application (e.g., http://example.com) | Yes |
| $_CRAWL_DEPTH | Depth to crawl linked pages (e.g., 1 for shallow, 3 for deeper) | Yes |
| --random-agent | Rotates User-Agent headers to evade detection | No |
| --batch | Runs in non-interactive mode, accepting defaults | No |
| --forms | Parses and tests HTML forms for injection points | No |
| $_THREADS | Number of concurrent threads for faster scanning (e.g., 5) | No |
| --level=5 | Maximum test level (1-5) for comprehensive payload coverage | No |
| --risk=3 | Highest risk level (1-3) including potentially disruptive tests | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com" --crawl=1 --random-agent --batch --forms --threads=5 --level=5 --risk=3
```

### Advanced Usage

```bash
sqlmap -u "https://target.com/login" --crawl=2 --random-agent --batch --forms --threads=10 --level=5 --risk=3 --proxy=http://127.0.0.1:8080
```

## Expected Output

The command outputs a summary of the crawl, tested parameters, and vulnerability results. For example:

```
[INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.4.3
back-end DBMS: MySQL >= 5.0
[INFO] fetched page: http://example.com/
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1' AND 1337=1337--

---
Parameter: id (GET) is vulnerable. Do you want to keep testing the others (if any)? [y/N] (default: N)
```

If no vulnerabilities: "All tests completed and no vulnerabilities were found."

## Related

- [[procedures/Automated-SQL-Injection-Detection-and-Exploitation-with-SQLmap]]
- [[tools/sqlmap]]
