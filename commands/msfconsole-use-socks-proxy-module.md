---
type: command
executor: msfconsole
data: use auxiliary/server/socks_proxy
output: null
platforms:
  - Linux
tags:
  - metasploit
  - proxy
verified: true
validated: true
---

# msfconsole-use-socks-proxy-module

## Command

```msfconsole
use auxiliary/server/socks_proxy
```

## Description

This command loads the SOCKS proxy server module in Metasploit, preparing it to host a proxy tunnel via an active session. Use this as the first step when setting up pivoting through a compromised host.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `auxiliary/server/socks_proxy` | The module path for the SOCKS proxy server | Yes |

## Examples

### Basic Usage

```msfconsole
use auxiliary/server/socks_proxy
```

### With Context

After obtaining a Meterpreter session, load this module to begin proxy configuration.

## Expected Output

[*] auxiliary/server/socks_proxy - SOCKS Proxy Server (SOCKS4a)

       Name: auxiliary/server/socks_proxy
     Version: 1
   License: MSF_LICENSE

(Displays module options like SRVHOST, SRVPORT, etc.)

## Related

- [[procedures/Setup-Meterpreter-SOCKS-Proxy]]
- [[commands/msfconsole-set-srvport]]
