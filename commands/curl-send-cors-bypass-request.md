---
type: command
executor: bash
data: 'curl -v -X GET -H "Origin: $_MALICIOUS_ORIGIN" $_TARGET_URL'
output: null
created_at: '2023-04-06T03:55:55Z'
updated_at: '2023-04-10T20:21:20Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - cors
  - exploitation
verified: true
validated: true
---

# curl-send-cors-bypass-request

## Command

```bash
curl -v -X GET -H "Origin: $_MALICIOUS_ORIGIN" $_TARGET_URL
```

## Description

This command sends an HTTP GET request to a target endpoint with a custom Origin header to test or exploit CORS misconfigurations, such as regex bypasses where unescaped dots allow wildcard matching. Use it to verify if the server reflects the Origin in Access-Control-Allow-Origin, enabling cross-origin data access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MALICIOUS_ORIGIN | The crafted Origin header value (e.g., https://apiiexample.com for regex bypass) | Yes |
| $_TARGET_URL | The full URL of the vulnerable endpoint (e.g., https://api.example.com/endpoint) | Yes |
| -v | Verbose mode to display request/response headers | No |
| -X GET | Specifies the HTTP method (use OPTIONS for preflight testing) | No |

## Examples

### Basic Usage

```bash
curl -v -X GET -H "Origin: https://apiiexample.com" https://api.example.com/endpoint
```

### With Credentials (Authenticated Bypass)

```bash
curl -v -X GET -H "Origin: https://apiiexample.com" -H "Cookie: session=abc123" https://api.example.com/endpoint
```

## Expected Output

*   Trying 93.184.216.34:443...
* Connected to api.example.com (93.184.216.34) port 443
> GET /endpoint HTTP/1.1
> Host: api.example.com
> Origin: https://apiiexample.com
<
< HTTP/1.1 200 OK
< Access-Control-Allow-Origin: https://apiiexample.com
< Access-Control-Allow-Credentials: true
<
{"private API key": "sensitive-data"}

The response includes the echoed Origin in ACAO header and the sensitive payload, indicating successful bypass.

## Related

- [[procedures/Exploit-CORS-Misconfiguration-Regex-Bypass]]
