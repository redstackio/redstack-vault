---
id: cmd-curl-get
data: >-
  curl
  'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess'
  --verbose
tags:
  - http
  - error-probe
type: command
output: Full HTML error page with stack trace including paths.
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.543Z'
verified: false
validated: true
submitted: true
---
# curl-get-response

## Command

```bash
curl 'https://nextcloud.example.com/remote.php/dav/files/username/test.htaccess' --verbose
```

## Description

This command performs a full GET request to retrieve the response from the .htaccess file access, capturing any error output with disclosed paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--verbose` | Shows detailed request/response info | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl 'https://target.com/file.htaccess' -v
```

### Advanced Usage

```bash
curl 'https://target.com/file.htaccess' -v --output error.html
```

## Expected Output

Verbose output including headers and body with potential PHP fatal error and full paths.

## Related

- [[Related Procedure|procedures/Trigger-Path-Disclosure-Exception]]
