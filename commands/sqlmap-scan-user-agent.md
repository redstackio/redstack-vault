---
id: cmd-uuid-001
data: 'sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3'
tags:
  - sqli
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.972Z'
verified: false
validated: true
submitted: true
---
# sqlmap-scan-user-agent

## Command

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3
```

## Description

This command uses sqlmap to scan a target URL for SQL injection vulnerabilities, emphasizing HTTP headers like User-Agent, in a non-interactive mode with evasion techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Target URL to test for injections | Yes |
| `--batch` | Run without user prompts, using defaults | No |
| `--random-agent` | Rotate random User-Agent strings to avoid detection | No |
| `--level 5` | Test all vectors including headers (highest level) | No |
| `--risk 3` | Include risky payloads like blind techniques (highest risk) | No |

## Examples

### Basic Usage

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3
```

### Advanced Usage

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3 --dbms=mysql
```

## Expected Output

Detection messages like 'Parameter: User-Agent (User-Agent) Type: boolean-based blind Title: OR boolean-based blind - WHERE or HAVING clause Payload: -5127 OR 2687=2687--' and DBMS info such as 'back-end DBMS: MySQL >= 8.0.0 (MariaDB fork)'.

## Related

- [[commands/sqlmap-confirm-injection]]
- [[procedures/Scan-Target-for-SQL-Injection-Vulnerabilities]]
