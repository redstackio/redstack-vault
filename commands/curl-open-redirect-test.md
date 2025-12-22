---
id: d4e5f6g7-h8i9-0123-defg-456789012345
data: >-
  curl -L -v
  "http://target.com/www/admin/account-switch.php?return_url=http://127.0.0.1:12345/test"
  --cookie "session=your_session_cookie"
tags:
  - web-testing
  - redirect
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:28:20.504Z'
verified: false
validated: true
submitted: true
---
# curl-open-redirect-test

## Command

```bash
curl -L -v "http://target.com/www/admin/account-switch.php?return_url=http://127.0.0.1:12345/test" --cookie "session=your_session_cookie"
```

## Description

This command tests for open redirect vulnerabilities by sending an authenticated request to a crafted URL and following the redirect to verify if arbitrary domains are allowed. Use it in web vulnerability assessments targeting redirect endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow redirects | Yes |
| `-v` | Verbose output to show headers | Yes |
| `--cookie` | Provide session cookie for authentication | Yes |
| URL | Target endpoint with malicious return_url | Yes |

## Examples

### Basic Usage

```bash
curl -L -v "http://target.com/vuln?redirect=http://evil.com" --cookie "session=abc123"
```

### Advanced Usage

```bash
curl -L -v -H "User-Agent: Mozilla/5.0" "http://target.com/admin/account-switch.php?return_url=http://127.0.0.1:12345/test" --cookie-jar cookies.txt
```

## Expected Output

Verbose output showing HTTP 302 status, Location header pointing to the arbitrary URL (e.g., http://127.0.0.1:12345/test), and final GET to the redirected site. Success if redirect occurs without domain checks.

## Related

- [[Related Procedure: Exploit-Open-Redirect-in-Account-Switch]]
