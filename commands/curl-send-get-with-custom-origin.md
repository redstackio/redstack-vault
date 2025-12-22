---
type: command
executor: bash
data: 'curl -v -H "Origin: $_MALICIOUS_ORIGIN" $_TARGET_URL'
output: null
created_at: '2023-04-06T03:55:55Z'
updated_at: '2023-04-06T03:55:55Z'
platforms:
  - Linux
  - macOS
  - Windows (with curl)
tags:
  - web
  - cors
  - exploitation
verified: true
validated: true
---

# curl-send-get-with-custom-origin

## Command

```bash
curl -v -H "Origin: $_MALICIOUS_ORIGIN" $_TARGET_URL
```

## Description

This command uses curl to send a GET request to a target web endpoint with a custom Origin header, useful for testing and exploiting CORS misconfigurations by simulating cross-origin requests from a malicious domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_ORIGIN | The forged Origin header value (e.g., https://eviltrusted.com) to bypass regex validation | Yes |
| $_TARGET_URL | The full URL of the vulnerable endpoint (e.g., https://api.example.com/endpoint) | Yes |
| -v | Verbose mode to display request/response headers | No (recommended for debugging) |
| -H | Flag to add custom headers | Built-in |

## Examples

### Basic Usage

```bash
curl -v -H "Origin: https://evil.com" https://api.example.com/endpoint
```

### With Silent Output and JSON Parsing

```bash
curl -s -H "Origin: null" https://api.example.com/sensitive | jq .
```

## Expected Output

Verbose output showing the request headers, followed by the response:

* Connected to api.example.com (192.0.2.1) port 443
> GET /endpoint HTTP/1.1
> Host: api.example.com
> Origin: https://evil.com
<
< HTTP/1.1 200 OK
< Access-Control-Allow-Origin: https://evil.com
< Access-Control-Allow-Credentials: true
<
{"api_key": "sk-abc123", "user_data": "sensitive info"}

Success is indicated by the echoed Origin in Access-Control-Allow-Origin and sensitive data in the body.

## Related

- [[procedures/CORS-Misconfiguration-Exploitation-Expanding-Origin-Regex-Issues]]
