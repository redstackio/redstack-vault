---
id: cmd-1066410-005
data: 'curl -L ''https://lnk.clario.co/abc123'' -v'
tags:
  - test
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.471Z'
verified: false
validated: true
submitted: true
---
# test-redirect

## Command

```bash
curl -L 'https://lnk.clario.co/abc123' -v
```

## Description

Tests a short link by following redirects to verify open redirect behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `'https://...'` | Short link URL | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -L 'https://lnk.clario.co/abc123' -v
```

### Advanced Usage

```bash
curl -L -o /dev/null 'https://lnk.clario.co/abc123' -w '%{url_effective}'
```

## Expected Output

Verbose logs showing 302 redirect to the target malicious URL.

## Related

- [[commands/create-firebase-short-link]]
- [[procedures/Demonstrate-Open-Redirect-PoC]]
