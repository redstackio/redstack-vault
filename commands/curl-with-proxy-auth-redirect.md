---
data: 'curl -H "Proxy-Authorization: Basic xxx==" http://server1:8000 -L'
tags:
  - curl
  - redirect
  - header
type: command
output: null
executor: bash
platforms:
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.551Z'
id: 30e79149-3c62-4c27-a922-dcc12510de67
verified: false
validated: true
submitted: true
---
# curl-with-proxy-auth-redirect

## Command

```bash
curl -H "Proxy-Authorization: Basic xxx==" http://server1:8000 -L
```

## Description

Sends an HTTP GET request with a custom Proxy-Authorization header using Basic auth, targeting a redirect endpoint, and follows the redirect with -L to demonstrate header leakage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Adds custom header (Proxy-Authorization: Basic xxx==) | Yes |
| `-L` | Automatically follows HTTP redirects | Yes |
| `http://server1:8000` | Initial target URL | Yes |

## Examples

### Basic Usage

```bash
curl -H "Proxy-Authorization: Basic dXNlcjpwYXNz" http://server1:8000 -L
```

### Advanced Usage

```bash
curl -H "Proxy-Authorization: Basic xxx==" http://server1:8000 -L -v  # Verbose for debug
```

## Expected Output

Follows redirect to new host; if vulnerable, header is forwarded. Verbose shows: '< HTTP/1.1 302 Found\n< Location: http://server2:8081/' and subsequent request.

## Related

- [[commands/nc-listen-port]]
- [[procedures/Trigger-Proxy-Header-Leakage-with-curl]]
