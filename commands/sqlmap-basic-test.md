---
id: cmd-sqlmap-basic-001
data: 'sqlmap -u "https://www.zomato.com/app?param=value" --batch --level=1 --risk=1'
tags:
  - sqli
  - scan
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.091Z'
verified: false
validated: true
submitted: true
---
# sqlmap-basic-test

## Command

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --batch --level=1 --risk=1
```

## Description

Runs a basic SQL injection test using sqlmap on a target URL to detect vulnerabilities without user interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| --batch | Non-interactive mode | No |
| --level=1 | Testing intensity (1-5) | No |
| --risk=1 | Risk level (1-3) | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com/search?q=test" --batch
```

### Advanced Usage

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --level=2 --risk=2 --dbms=mysql
```

## Expected Output

Vulnerability detection message, e.g., "[INFO] the back-end DBMS is MySQL" and exploitation details.

## Related

- [[Related Procedure: Identify-SQL-Injection-Endpoint]]
