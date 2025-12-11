---
data: 'curl -H ''Cookie: session=leaked_cookie_value'' https://target_endpoint'
tags:
  - http-request
  - session-hijacking
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e28d78de-50d2-43a4-8076-291296e0dbe3
created_at: '2025-12-11T06:10:40.550Z'
updated_at: '2025-12-11T06:10:40.550Z'
verified: false
validated: true
submitted: true
---
# curl-with-session-cookie

## Command

```bash
curl -H 'Cookie: session=leaked_cookie_value' https://target_endpoint
```

## Description

This command uses cURL to send an HTTP request with a specified session cookie header, allowing impersonation of a user session on web platforms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Cookie: session=leaked_cookie_value'` | Sets the Cookie header with the leaked session value | Yes |
| `https://target_endpoint` | The URL to request | Yes |

## Examples

### Basic Usage

```bash
curl -H 'Cookie: session=eyJ...' https://hackerone.com/dashboard
```

### Advanced Usage

```bash
curl -H 'Cookie: session=eyJ...' -v https://hackerone.com/inbox
```

## Expected Output

HTTP response from the target endpoint, potentially including authenticated content if the cookie is valid.

## Related

- [[procedures/Impersonate-User-with-Stolen-Session-Cookie]]
- [[tools/cURL]]
