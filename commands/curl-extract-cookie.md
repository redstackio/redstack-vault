---
data: 'curl -v https://hackerone.com/reports/example 2>&1 | grep -i cookie'
tags:
  - http
  - extraction
  - grep
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:34.529Z'
id: 291c4216-e47a-4889-a6f7-d4b0d84f638c
verified: false
validated: true
submitted: true
---
# curl-extract-cookie

## Command

```bash
curl -v https://hackerone.com/reports/example 2>&1 | grep -i cookie
```

## Description

This command fetches a report page and uses grep to search for cookie-related strings in the verbose output or response body, aiding in identifying leaked cookies in comments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers | Yes |
| `https://hackerone.com/reports/example` | Target report URL | Yes |
| `2>&1 | grep -i cookie` | Redirects stderr and filters for 'cookie' | Yes |

## Examples

### Basic Usage

```bash
curl -s https://hackerone.com/reports/745324 | grep -i 'Cookie:'
```

### Advanced Usage

```bash
curl -v https://hackerone.com/reports/745324 2>&1 | grep -E 'Cookie: __session='
```

## Expected Output

Lines matching cookie patterns, e.g., 'Cookie: __session=abc123...' from comments or headers.

## Related

- [[Related Procedure: Observe-Leaked-Session-Cookie]]
