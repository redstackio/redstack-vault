---
id: cmd-uuid-4
data: 'curl -i http://127.0.0.1:3000//hackerone.com'
tags:
  - test
  - http
  - redirect
type: command
output: >-
  HTTP/1.1 307 Temporary Redirect with Location: //hackerone.com/ and HTML
  redirect message
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.074Z'
verified: false
validated: true
submitted: true
---
# test-open-redirect

## Command

```bash
curl -i http://127.0.0.1:3000//hackerone.com
```

## Description

Sends an HTTP GET request to the vulnerable path on the hekto server to trigger and observe the open redirect response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Include response headers | Yes |
| http://127.0.0.1:3000//hackerone.com | Target URL with double slash | Yes |

## Examples

### Basic Usage

```bash
curl -i http://127.0.0.1:3000//hackerone.com
```

### Advanced Usage

```bash
curl -i -L http://127.0.0.1:3000//example.com
```

## Expected Output

Headers: HTTP/1.1 307 Temporary Redirect
Location: //hackerone.com/
Body: HTML with meta refresh to the redirect URL.

## Related

- [[Related Procedure|procedures/Test-Open-Redirect]]
