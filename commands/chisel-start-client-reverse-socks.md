---
id: 2ad689c6-f6ee-46c0-b5a8-08610e9745ba
name: chisel-start-client-reverse-socks
type: command
executor: bash
data: './chisel client --tls-skip-verify https://$_VPS_IP:$_SERVER_PORT R:socks'
output: null
created_at: '2023-04-06T03:56:22.550102+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - chisel
  - client
  - reverse
  - socks
verified: true
validated: true
---

# chisel-start-client-reverse-socks

## Command

```bash
./chisel client --tls-skip-verify https://$_VPS_IP:$_SERVER_PORT R:socks
```

## Description

Connects the Chisel client to a server and creates a reverse SOCKS5 tunnel (R:socks) for inbound proxying from the server side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --tls-skip-verify | Skip TLS certificate verification | No (for self-signed) |
| https://$_VPS_IP:$_SERVER_PORT | Server URL (e.g., https://192.168.1.100:8443) | Yes |
| R:socks | Reverse tunnel for SOCKS5 | Yes |

## Examples

### Basic Usage

```bash
./chisel client --tls-skip-verify https://192.168.1.100:8443 R:socks
```

### Advanced Usage

```bash
./chisel client --tls-skip-verify https://$_VPS_IP:8443 R:1080:socks --auth user:pass
```

## Expected Output

"2023/xx/xx xx:xx:xx client: Connected (Latency: xxxms)" followed by tunnel logs. Success: No disconnects; server shows new SOCKS listener.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Chisel]]
