---
type: command
executor: bash
data: 'curl -s -I https://$_TARGET_URL | grep -i content-security-policy'
tags:
  - web
  - recon
platforms:
  - linux
  - macos
verified: true
validated: true
---

# curl-fetch-csp-header

## Command

```bash
curl -s -I https://$_TARGET_URL | grep -i content-security-policy
```

## Description

This command fetches the HTTP headers from a target URL and extracts the Content-Security-Policy (CSP) header to inspect its directives, such as whether 'unsafe-inline' is permitted. Use it during reconnaissance to identify CSP misconfigurations exploitable for script injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The full URL of the target web page (e.g., https://example.com) | Yes |
| -s | Silent mode to suppress progress meter | Built-in |
| -I | Fetch headers only (HEAD request) | Built-in |
| grep -i content-security-policy | Case-insensitive filter for CSP header | Built-in |

## Examples

### Basic Usage

```bash
curl -s -I https://example.com | grep -i content-security-policy
```

### Advanced Usage

```bash
curl -s -I -H "User-Agent: Mozilla/5.0" https://example.com | grep -i content-security-policy
```

## Expected Output

Content-Security-Policy: default-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' https://trusted.com

This shows the policy directives. Look for 'unsafe-inline' to confirm vulnerability to inline script injection.

## Related

- [[procedures/CSP-Bypass-via-Unsafe-Inline-Script-Injection]]
