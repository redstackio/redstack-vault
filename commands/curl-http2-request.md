---
data: 'curl --http2 -v [URL]'
tags:
  - http
  - testing
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 680d648e-44c6-45c2-a33e-28584d9efcfb
created_at: '2025-12-13T09:01:26.196Z'
updated_at: '2025-12-13T09:01:26.196Z'
verified: false
validated: true
submitted: true
---
# curl-http2-request

## Command

```bash
curl --http2 -v [URL]
```

## Description

This command uses cURL to send an HTTP request forcing HTTP/2 protocol, with verbose output to inspect protocol negotiation and responses, useful for testing HTTP/2 vulnerabilities like request smuggling.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--http2` | Force HTTP/2 protocol | Yes |
| `-v` | Verbose output | No |
| `[URL]` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl --http2 https://basecamp-target.com/
```

### Advanced Usage

```bash
curl --http2 -v -d 'data' https://basecamp-target.com/
```

## Expected Output

Verbose logs showing HTTP/2 handshake and response headers, indicating successful protocol usage or errors.

## Related

- [[commands/burp-repeater-test]]
- [[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]
