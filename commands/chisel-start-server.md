---
id: fc86c51d-3d23-4679-9fd5-02dc16ed84f0
name: chisel-start-server
type: command
executor: bash
data: >-
  ./chisel server --tls-key ./$_TLS_KEY --tls-cert ./$_TLS_CERT -p $_SERVER_PORT
  --reverse
output: null
created_at: '2023-04-06T03:56:22.550038+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - chisel
  - tunnel
  - reverse
verified: true
validated: true
---

# chisel-start-server

## Command

```bash
./chisel server --tls-key ./$_TLS_KEY --tls-cert ./$_TLS_CERT -p $_SERVER_PORT --reverse
```

## Description

Starts the Chisel server in reverse mode, allowing clients to create inbound tunnels for SOCKS5 proxying, secured with TLS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --tls-key ./$_TLS_KEY | Path to TLS private key file | Yes |
| --tls-cert ./$_TLS_CERT | Path to TLS certificate file | Yes |
| -p $_SERVER_PORT | Port to listen on (default 8080) | No |
| --reverse | Enable reverse tunneling mode | Yes |

## Examples

### Basic Usage

```bash
./chisel server --tls-key ./key.pem --tls-cert ./cert.pem -p 8443 --reverse
```

### Advanced Usage

```bash
./chisel server --tls-key ./key.pem --tls-cert ./cert.pem -p 8443 --reverse --auth user:pass
```

## Expected Output

"2023/xx/xx xx:xx:xx server: Listening on 0.0.0.0:8443" on success. Errors for missing files or bound ports.

## Related

- [[procedures/Proxify-Go-Application-with-Graftcp]]
- [[tools/Chisel]]
