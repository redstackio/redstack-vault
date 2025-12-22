---
type: command
executor: bash
data: './cloudflared tunnel --url $_PROTOCOL://$_HOST:$_PORT'
tags:
  - tunnel
  - expose
  - cloudflared
platforms:
  - Linux
verified: true
validated: true
---

# cloudflared-tunnel-expose-service

## Command

```bash
./cloudflared tunnel --url $_PROTOCOL://$_HOST:$_PORT
```

## Description

Creates a temporary Cloudflare Tunnel that exposes the specified local service to a public URL. Useful for pivoting to internal services from external attacker machines without opening firewall ports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --url | Specifies the local service URL (protocol://host:port) | Yes |
| $_PROTOCOL | Protocol (e.g., http, https) | Yes |
| $_HOST | Hostname or IP (e.g., localhost, 127.0.0.1) | Yes |
| $_PORT | Port number (e.g., 8080) | Yes |

## Examples

### Basic Usage

Expose a local HTTP server on port 8080:

```bash
./cloudflared tunnel --url http://localhost:8080
```

### Advanced Usage

Expose an HTTPS service:

```bash
./cloudflared tunnel --url https://internal-server:8443
```

## Expected Output

2023/xx/xx HH:MM:SS INFO Tunnel server connected
2023/xx/xx HH:MM:SS INFO Your quick Tunnel has been created! Visit it at: https://random.trycloudflare.com

The tunnel URL is the public endpoint; test accessibility externally.

## Related

- [[procedures/Cloudflare-Tunnel-Pivoting-for-Lateral-Movement]]
- [[tools/cloudflared]]
