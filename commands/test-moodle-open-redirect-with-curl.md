---
data: >-
  curl -i -L
  "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com"
tags:
  - web
  - redirect
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 43b399ab-fbd3-46d0-8c52-24041b21b7df
created_at: '2025-12-13T23:52:39.014Z'
updated_at: '2025-12-13T23:52:39.014Z'
verified: false
validated: true
submitted: true
---
# test-moodle-open-redirect-with-curl

## Command

```bash
curl -i -L "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com"
```

## Description

This command tests for an open redirect vulnerability in the Moodle LTI endpoint by sending a GET request with an external redirect_uri and following the redirect to check the Location header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers | Yes |
| `-L` | Follow redirects | Yes |
| `redirect_uri` | External URL to test (e.g., https://example.com) | Yes |

## Examples

### Basic Usage

```bash
curl -i -L "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://example.com"
```

### Advanced Usage

```bash
curl -i -L -v "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=https://attacker.com/phish" 2>&1 | grep Location
```

(Verbose mode to log details and grep for Location header.)

## Expected Output

HTTP/1.1 302 Found\nLocation: https://example.com\n... (indicating successful unvalidated redirect).

## Related

- [[Related Procedure]]
