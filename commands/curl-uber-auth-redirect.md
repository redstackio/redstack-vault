---
data: >-
  curl -L "https://auth.uber.com/login?next_url=https://login.uber.com/logout"
  -H "Referer: https://www.facebook.com" -v
tags:
  - redirect
  - curl
  - internal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:39.098Z'
id: 421b0275-6bf8-49a6-8531-d13f0c3a2729
verified: false
validated: true
submitted: true
---
# curl-uber-auth-redirect

## Command

```bash
curl -L "https://auth.uber.com/login?next_url=https://login.uber.com/logout" -H "Referer: https://www.facebook.com" -v
```

## Description

Triggers the redirect from Uber's auth endpoint to the logout endpoint via next_url parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `next_url` | Target internal URL | Yes |
| `-L` | Location follow | Yes |
| `-H Referer` | Simulate origin | No |

## Examples

### Basic Usage

```bash
curl -L "https://auth.uber.com/login?next_url=https://login.uber.com/logout" -v
```

### Advanced Usage

```bash
curl -L "https://auth.uber.com/login?next_url=...&access_token=FAKE" -v
```

## Expected Output

302 redirect to the next_url with any query params.

## Related

- [[Related Procedure: Redirect-to-Uber-Logout-Endpoint]]
