---
id: cmd-curl-test-post
data: >-
  curl -X POST https://target.com/██████████_flight/images -d
  "advanced_val=test123" -H "Content-Type: application/x-www-form-urlencoded" -v
tags:
  - web
  - testing
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.760Z'
verified: false
validated: true
submitted: true
---
# curl-test-post-parameter

## Command

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=test123" -H "Content-Type: application/x-www-form-urlencoded" -v
```

## Description

Sends a test POST request to probe the `advanced_val` parameter for reflection in the response, useful for initial XSS vulnerability identification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Data payload | Yes |
| `-H` | Custom header for content type | Yes |
| `-v` | Verbose output for inspection | No |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=test123" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://target.com/██████████_flight/images -d "advanced_val=test123&other=val" -H "Content-Type: application/x-www-form-urlencoded" -v -o response.html
```

## Expected Output

HTTP response with body containing the echoed `test123` string, visible in verbose mode or saved file.

## Related

- [[Related Procedure|procedures/Identify-Vulnerable-XSS-Endpoint]]
