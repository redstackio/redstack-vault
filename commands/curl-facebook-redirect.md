---
data: >-
  curl -L
  "https://www.facebook.com/v18.0/dialog/oauth?client_id=UBER_APP_ID&redirect_uri=https://auth.uber.com/login?next_url=https://login.uber.com/logout&scope=public_profile,email&response_type=token"
  -H "Referer: https://attacker.com" -v
tags:
  - redirect
  - curl
  - oauth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.118Z'
id: f605f5e9-4d98-4f32-b6b1-776366f8fb6a
verified: false
validated: true
submitted: true
---
# curl-facebook-redirect

## Command

```bash
curl -L "https://www.facebook.com/v18.0/dialog/oauth?client_id=UBER_APP_ID&redirect_uri=https://auth.uber.com/login?next_url=https://login.uber.com/logout&scope=public_profile,email&response_type=token" -H "Referer: https://attacker.com" -v
```

## Description

Follows the OAuth redirect from Facebook to Uber's auth endpoint, simulating victim post-authorization flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `redirect_uri` | Chained URI | Yes |
| `-H Referer` | Set origin header | No |
| `-v` | Verbose | No |

## Examples

### Basic Usage

```bash
curl -L "https://www.facebook.com/v18.0/dialog/oauth?..." -v
```

### Advanced Usage

```bash
curl -L "https://www.facebook.com/v18.0/dialog/oauth?..." -H "Cookie: fbm=1" -v
```

## Expected Output

Chain of 302 redirects ending at auth.uber.com with preserved parameters.

## Related

- [[Related Procedure: Chain-Redirect-to-Uber-Auth-Endpoint]]
