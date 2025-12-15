---
id: cmd-curl-test-open-redirect
data: >-
  curl -L
  "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://evil.com"
  -v
tags:
  - web-testing
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.659Z'
verified: false
validated: true
submitted: true
---
# curl-test-open-redirect

## Command

```bash
curl -L "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://evil.com" -v
```

## Description

This command tests for an open redirect vulnerability by sending a GET request to the target endpoint with a malicious redirect parameter and following the location header to confirm redirection to an external site.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-v` | Verbose output to show headers | Yes |
| `?next=http://evil.com` | Malicious redirect URL in query | Yes |

## Examples

### Basic Usage

```bash
curl -L "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://evil.com" -v
```

### Advanced Usage

```bash
curl -L -H "User-Agent: Mozilla/5.0" "https://www.rockstargames.com/GTAOnline/restricted-content/agegate/form?next=http://evil.com/test" -v
```

## Expected Output

Verbose output showing HTTP/1.1 302 Found and Location: http://evil.com in the response headers, confirming the redirect.

## Related

- [[Related Procedure|procedures/Exploit-Open-Redirect-in-Age-Gate]]
