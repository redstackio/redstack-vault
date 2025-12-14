---
data: curl -I $1
tags:
  - web
  - verification
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:31.250Z'
id: 75809fba-2695-4a57-87ff-da8f10e3e1f4
verified: false
validated: true
submitted: true
---
# curl-http-check

## Command

```bash
curl -I $1
```

## Description

Fetches HTTP headers to check server response, status, and content indicators for unclaimed sites.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $1 | URL (e.g., https://dev.rbk.money) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://dev.rbk.money
```

### Advanced Usage

```bash
curl -I -L https://dev.rbk.money
```

## Expected Output

Headers like "HTTP/1.1 404 Not Found" or GitHub-specific Server: GitHub.com.

## Related

- [[Related Procedure]]
