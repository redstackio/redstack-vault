---
data: >-
  curl -X GET https://manage.booth.pm/design/edit -H "Cookie:
  session=your_session_cookie" -v
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.255Z'
id: 4b7ae8b5-b501-4755-a105-c97e2f97bc19
verified: false
validated: true
submitted: true
---
# curl-upload-access

## Command

```bash
curl -X GET https://manage.booth.pm/design/edit -H "Cookie: session=your_session_cookie" -v
```

## Description

This command accesses the design edit page to verify the upload function is available, using verbose output to inspect the response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `-H "Cookie: ..."` | Provides authentication session | Yes |
| `-v` | Verbose mode for headers and status | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://manage.booth.pm/design/edit -H "Cookie: session=abc123" -v
```

### Advanced Usage

```bash
curl -X GET https://manage.booth.pm/design/edit -H "Cookie: session=abc123" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

HTTP/1.1 200 OK followed by HTML content containing the upload form; look for <input type="file"> elements.

## Related

- [[Related Procedure]]
