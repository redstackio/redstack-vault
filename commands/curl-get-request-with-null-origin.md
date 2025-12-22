---
id: c882587e-8fd0-413b-8b11-685c972fd769
name: curl-get-request-with-null-origin
type: command
executor: bash
data: 'curl -H "Origin: null" -H "Cookie: $_COOKIE" -X GET "$_TARGET_URL/$_ENDPOINT"'
output: null
created_at: '2023-04-06T03:55:55.758478+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
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

# curl-get-request-with-null-origin

## Command

```bash
curl -H "Origin: null" -H "Cookie: $_COOKIE" -X GET "$_TARGET_URL/$_ENDPOINT"
```

## Description

Sends a GET request to a target web endpoint with the Origin header set to null, simulating a cross-origin request from a null context to test for CORS misconfigurations. This is used to trigger reflection of the Origin in the Access-Control-Allow-Origin header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target domain (e.g., https://victim.example.com) | Yes |
| $_ENDPOINT | Path to the vulnerable endpoint (e.g., /api/user) | Yes |
| $_COOKIE | Session or authentication cookie value (e.g., sessionid=abc123) | No (if unauthenticated) |
| -H | Adds custom headers | Built-in |
| -X GET | Specifies the HTTP method | Built-in |

## Examples

### Basic Usage

```bash
curl -H "Origin: null" -X GET "https://victim.example.com/api/profile"
```

### Advanced Usage (with Cookie)

```bash
curl -H "Origin: null" -H "Cookie: sessionid=abc123" -X GET "https://victim.example.com/endpoint"
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: application/json
Access-Control-Allow-Origin: null

{"user": {"email": "victim@example.com", "api_key": "sensitive_key"}}

The response includes the endpoint data and potentially reflected CORS headers indicating vulnerability.

## Related

- [[procedures/CORS-Misconfiguration-Exploitation-Null-Origin]]
- [[commands/curl-check-cors-response-headers]]
