---
id: 39474b96-9cf5-4509-8ac2-b0239a8022f5
name: sqlmap-boolean-blind-test
type: command
executor: bash
data: 'sqlmap --url https://target.mil/ --random-agent -risk 3 --level 5 --batch'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:09.851Z'
platforms:
  - Linux
  - Windows
tags:
  - sqli
  - testing
verified: false
validated: true
submitted: true
---

# sqlmap-boolean-blind-test

## Command

```bash
sqlmap --url https://target.mil/ --random-agent -risk 3 --level 5 --batch
```

## Description

This command runs SQLMap to test for boolean-based blind SQL injection vulnerabilities in a web application, targeting the specified URL with randomized User-Agents and high-risk payloads to detect issues in headers like User-Agent.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Specifies the target URL to test | Yes |
| `--random-agent` | Uses a random User-Agent for each request to evade detection | No |
| `-risk 3` | Sets risk level to 3 (highest) for aggressive, potentially disruptive payloads | No |
| `--level 5` | Sets testing level to 5 (highest) to check all injection points including headers | No |
| `--batch` | Runs in non-interactive mode, selecting defaults automatically | No |

## Examples

### Basic Usage

```bash
sqlmap --url https://target.mil/ --batch
```

### Advanced Usage

```bash
sqlmap --url https://target.mil/ --random-agent -risk 3 --level 5 --batch --dbms=mysql --technique=B
```

## Expected Output

Console logs detailing tested parameters, detected vulnerabilities (e.g., 'boolean-based blind' in User-Agent), and potential database info if exploitable. May include response time analysis and payload examples.

## Related

- [[Related Procedure: Automated-SQL-Injection-Testing-with-SQLMap]]
