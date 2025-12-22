---
id: 30c4e5a5-12ab-49c6-b399-f2993513e305
name: curl-get-request-with-origin-header
type: command
executor: bash
data: >-
  curl -X GET -H "Origin: https://evil.com" -H "Cookie: sessionid=abc123"
  "https://victim.example.com/endpoint" -v
output: null
created_at: '2023-04-06T03:55:54.548875+00:00'
updated_at: '2023-04-06T03:55:54.554680+00:00'
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

# curl-get-request-with-origin-header

## Command

```bash
curl -X GET -H "Origin: https://evil.com" -H "Cookie: sessionid=abc123" "https://victim.example.com/endpoint" -v
```

## Description

This command sends an HTTP GET request to a target endpoint with a custom Origin header to test for CORS misconfiguration via Origin Reflection. It includes an authentication cookie to simulate a victim's session. Use this during web vulnerability assessment to check if the server echoes the Origin in Access-Control-Allow-Origin, enabling cross-origin data access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `-H "Origin: https://evil.com"` | Sets the Origin header to an attacker-controlled domain | Yes |
| `-H "Cookie: sessionid=abc123"` | Includes the session cookie for authentication (replace with actual value) | Yes |
| `https://victim.example.com/endpoint` | The target URL of the sensitive endpoint | Yes |
| `-v` | Verbose mode to display request/response headers | No |

## Examples

### Basic Usage

```bash
curl -X GET -H "Origin: https://evil.com" -H "Cookie: sessionid=abc123" "https://victim.example.com/endpoint" -v
```

### Advanced Usage (with User-Agent)

```bash
curl -X GET -H "Origin: https://evil.com" -H "Cookie: sessionid=abc123" -H "User-Agent: Mozilla/5.0" "https://victim.example.com/endpoint" -v
```

## Expected Output

A verbose output showing the request headers, followed by the response:

< HTTP/1.1 200 OK
< Access-Control-Allow-Origin: https://evil.com
< Access-Control-Allow-Credentials: true
< Content-Type: application/json
<
{"api_key": "sk-12345"}

Success is indicated if Access-Control-Allow-Origin matches the sent Origin and the body contains sensitive data.

## Related

- [[procedures/CORS-Misconfiguration-Exploitation-Origin-Reflection]]
