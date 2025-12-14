---
id: cmd-curl-open-redirect-test
data: 'curl -X GET "https://app.smule.com/redirect?url=TARGET_URL" -v'
tags:
  - web
  - redirect
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.327Z'
verified: false
validated: true
submitted: true
---
# curl-open-redirect-test

## Command

```bash
curl -X GET "https://app.smule.com/redirect?url=TARGET_URL" -v
```

## Description

This command tests for open redirect vulnerabilities by sending a GET request to a redirect endpoint with a user-supplied URL, using verbose output to inspect headers like Location for successful redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `url=TARGET_URL` | The redirect parameter with target URL (e.g., //evil.com) | Yes |
| `-v` | Verbose mode to show headers | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://app.smule.com/redirect?url=https://example.com" -v
```

### Advanced Usage

```bash
curl -X GET "https://app.smule.com/redirect?url=%2F%2Fphishingsite.com" -v
```

## Expected Output

Verbose output showing HTTP/1.1 302 Found and Location: https://phishingsite.com indicating successful redirect.

## Related

- [[Related Procedure: Bypass-Open-Redirect-for-Phishing]]
