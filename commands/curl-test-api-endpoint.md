---
id: 9e471f4f-473f-4927-8fd5-9ddfd2ef6267
name: curl-test-api-endpoint
type: command
executor: bash
data: 'curl https://api.example.com/endpoint'
output: null
created_at: '2023-04-06T03:55:55.966469+00:00'
updated_at: '2023-04-10T20:21:23.340743+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - testing
verified: true
validated: true
---

# curl-test-api-endpoint

## Command

```bash
curl $_TARGET_URL
```

## Description

This command uses curl to perform a basic GET request to a target API endpoint, testing its availability and response. It is useful for initial reconnaissance of web APIs before attempting CORS exploitation, as it confirms the endpoint returns data without browser restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The full URL of the API endpoint to test (e.g., https://api.example.com/endpoint) | Yes |

## Examples

### Basic Usage

```bash
curl https://api.example.com/endpoint
```

### Advanced Usage

```bash
curl -v https://api.example.com/endpoint -H "Origin: https://evil.com"
```

This adds verbose output and a custom Origin header to simulate a cross-origin request.

## Expected Output

A successful response might look like:
```
{"user_id": 123, "api_key": "sensitive_value", "session_token": "abc123"}
```

If the endpoint is vulnerable, this data can be stolen via CORS abuse in a browser context. Errors indicate the endpoint is down or access is restricted server-side.

## Related

- [[procedures/Exploit-CORS-Misconfiguration-with-JavaScript-POC]]
