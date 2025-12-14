---
id: cmd-curl-head
data: >-
  curl -I
  'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
tags:
  - http
  - probe
type: command
output: |-
  HTTP/1.1 500 Internal Server Error
  Content-Type: text/html; charset=UTF-8
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.553Z'
verified: false
validated: true
submitted: true
---
# curl-head-request

## Command

```bash
curl -I 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
```

## Description

This command sends an HTTP HEAD request to probe the uploaded .htaccess file, triggering server-side processing that may result in an error exposing paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I` | Performs HEAD request only (headers) | Yes |
| URL | Target file endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -I 'https://target.com/path/to/file.htaccess'
```

### Advanced Usage

```bash
curl -I 'https://target.com/path/to/file.htaccess' --verbose --fail
```

## Expected Output

Headers with possible 500 error; body (if any) may include stack trace with paths in verbose mode.

## Related

- [[Related Procedure|procedures/Trigger-Path-Disclosure-Exception]]
