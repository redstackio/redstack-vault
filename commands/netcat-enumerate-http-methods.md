---
id: 9a3a4e94-ae7f-411d-89f7-91e596f5594d
name: netcat-enumerate-http-methods
type: command
executor: bash
data: |-
  nc $_TARGET_HOST $_TARGET_PORT
  OPTIONS / HTTP/1.1
  Host: $_TARGET_HOST
output: |-
  HTTP/1.1 200 OK
  Date: Sun, 19 July 2020 06:46:30 GMT
  Server: Apache-Coyote/1.1
  Allow: GET, HEAD, POST, OPTIONS, TRACE
  Content-Length: 0
  Connection: close
  Content-Type: text/html
created_at: '2020-07-19T06:50:16.822559+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Web
tags:
  - Enumeration
  - Web
verified: true
validated: true
---

# netcat-enumerate-http-methods

## Command

```bash
nc $_TARGET_HOST $_TARGET_PORT
OPTIONS / HTTP/1.1
Host: $_TARGET_HOST
```

## Description

This command uses Netcat to create a TCP connection to the target web server and manually sends an HTTP OPTIONS request to enumerate supported methods. It reveals the Allow header, helping identify insecure methods like DELETE or TRACE for potential exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | Target hostname or IP address (e.g., demo.testfire.net) | Yes |
| $_TARGET_PORT | Target port (default 80 for HTTP, 443 for HTTPS) | Yes |
| OPTIONS / HTTP/1.1 | HTTP request to query allowed methods | Yes |
| Host: $_TARGET_HOST | Specifies the virtual host for the request | Yes |

## Examples

### Basic Usage

```bash
nc demo.testfire.net 80
OPTIONS / HTTP/1.1
Host: demo.testfire.net
```

### Advanced Usage

For HTTPS, pipe through openssl: ```bash
printf "OPTIONS / HTTP/1.1\r\nHost: example.com\r\n\r\n" | openssl s_client -connect example.com:443
```

## Expected Output

```
HTTP/1.1 200 OK
Date: Sun, 19 July 2020 06:46:30 GMT
Server: Apache-Coyote/1.1
Allow: GET, HEAD, POST, OPTIONS, TRACE
Content-Length: 0
Connection: close
Content-Type: text/html
```

Look for the 'Allow' line to list supported methods.

## Related

- [[procedures/Enumerate-HTTP-Methods]]
- [[tools/Netcat]]
