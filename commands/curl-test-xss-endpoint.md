---
id: cmd-curl-test-xss
data: 'curl -X GET "https://m.vk.com/chatjoin?param=test" -v'
tags:
  - xss
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:33.650Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-endpoint

## Command

```bash
curl -X GET "https://m.vk.com/chatjoin?param=test" -v
```

## Description

This command probes a web endpoint for reflected input by sending a GET request with a benign parameter value, using verbose output to inspect the response for unsanitized reflection, which is a precursor to XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with parameter (e.g., ?param=test) | Yes |
| `-v` | Verbose mode to show headers and response details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://m.vk.com/chatjoin?param=test" -v
```

### Advanced Usage

```bash
curl -X GET "https://m.vk.com/chatjoin?param=reflected&other=val" -v -H "User-Agent: Mobile"
```

## Expected Output

Verbose logs including request headers, response status (e.g., 200 OK), and body showing 'test' reflected raw in HTML/JS, without encoding like &amp;lt;.

## Related

- [[Related Procedure: Exploit-Reflected-XSS-in-Mobile-Chat-Join]]
