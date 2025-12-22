---
type: command
executor: beacon
data: socks 1080
tags:
  - cobalt-strike
  - proxy
platforms:
  - Windows
verified: true
validated: true
---

# beacon-start-socks-proxy

## Command

```beacon
socks 1080
```

## Description

This Cobalt Strike beacon command starts a SOCKS4a proxy server on the compromised host, allowing external tools to pivot through the beacon for internal network access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 1080 | Local port to bind the SOCKS proxy | Yes |

## Examples

### Basic Usage

```beacon
socks 1080
```

### Advanced Usage

```beacon
socks -p 1080
```
(Use -p to specify port explicitly.)

## Expected Output

"SOCKS server started (0.0.0.0:1080)" in the beacon console.

## Related

- [[procedures/NTLM-Relay-Attack-via-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
