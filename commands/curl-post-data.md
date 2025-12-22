---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: 'curl -X POST -d ''data=input'' http://target.com/endpoint'
tags:
  - http
  - post
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.271Z'
verified: false
validated: true
submitted: true
---
# curl-post-data

## Command

```bash
curl -X POST -d 'data=input' http://target.com/endpoint
```

## Description

Sends a POST request with form data to a target URL, ideal for submitting malicious inputs to web applications to trigger vulnerabilities like PHP crashes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d 'data=input'` | Data to send in the request body | Yes |
| `http://target.com/endpoint` | Target URL | Yes |
| `-H 'Header: value'` | Custom headers | No |

## Examples

### Basic Usage

```bash
curl -X POST -d 'array=large_malformed_data' http://target.com/vuln.php
```

### Advanced Usage

```bash
curl -X POST -d 'input={"arr":["a" repeated 1000000 times]}' -H 'Content-Type: application/json' http://target.com/api.php
```

## Expected Output

Successful request: HTTP response body. Vulnerable trigger: 500 error or connection timeout due to crash.

## Related

- [[Related Procedure|procedures/Trigger-PHP-implode-Crash]]
