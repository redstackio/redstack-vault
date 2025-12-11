---
data: 'curl -v -H "Authorization: Bearer token" https://target-app.com/resource'
tags:
  - http
  - authentication
  - replay
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f23096f9-3fca-494b-8a50-8aee2d24169c
created_at: '2025-12-11T03:47:47.661Z'
updated_at: '2025-12-11T03:47:47.661Z'
verified: false
validated: true
submitted: true
---
# curl-replay-auth-token

## Command

```bash
curl -v -H "Authorization: Bearer token" https://target-app.com/resource
```

## Description

Uses curl to replay an authentication token (e.g., old or expired) in a request header to test for broken authentication mechanisms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| `-H "Authorization: Bearer token"` | Auth header with token | Yes |
| `https://target-app.com/resource` | Target protected URL | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Authorization: Bearer old-token" https://target-app.com/protected
```

### Advanced Usage

```bash
curl -v -H "Authorization: Bearer old-token" -d "data=payload" https://target-app.com/api
```

## Expected Output

HTTP 200 if replay succeeds, indicating broken token invalidation.

## Related

- [[commands/curl-access-actuator-endpoint]]
- [[procedures/Exploit-Exposed-Endpoints-and-Broken-Authentication-for-Information-Leakage]]
