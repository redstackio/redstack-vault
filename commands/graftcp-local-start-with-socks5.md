---
id: e9fbe1b2-e10f-495f-8d9c-8f32dce4f5b1
name: graftcp-local-start-with-socks5
type: command
executor: bash
data: >-
  graftcp-local -listen :$_LISTEN_PORT -logfile $_LOG_FILE -loglevel $_LOG_LEVEL
  -socks5 127.0.0.1:1080
output: null
created_at: '2023-04-06T03:56:22.550173+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - graftcp
  - proxy
  - socks5
verified: true
validated: true
---

# graftcp-local-start-with-socks5

## Command

```bash
graftcp-local -listen :$_LISTEN_PORT -logfile $_LOG_FILE -loglevel $_LOG_LEVEL -socks5 127.0.0.1:1080
```

## Description

Launches the Graftcp local proxy listener, routing intercepted Go application traffic through the specified SOCKS5 endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -listen :$_LISTEN_PORT | Address:port to listen on (default :2233) | No |
| -logfile $_LOG_FILE | Path to log file (default /tmp/graftcp.log) | No |
| -loglevel $_LOG_LEVEL | Log verbosity (1-6, default 1) | No |
| -socks5 127.0.0.1:1080 | SOCKS5 proxy address | Yes |

## Examples

### Basic Usage

```bash
graftcp-local -listen :2233 -logfile /tmp/graftcp.log -loglevel 3 -socks5 127.0.0.1:1080
```

### Advanced Usage

```bash
graftcp-local -listen :2233 -socks5 127.0.0.1:1080 -socks5_username $_USER -socks5_password $_PASS
```

## Expected Output

"[INFO] Listening on :2233" with proxy connection logs. Errors: "Failed to connect to SOCKS5" if proxy down.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Graftcp]]
