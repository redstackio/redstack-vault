---
type: command
executor: bash
data: >-
  xfreerdp /v:$_TARGET_IP /u:$_USERNAME /p:$_PASSWORD /d:$_DOMAIN +clipboard
  /cert-ignore /size:$_RESOLUTION /smart-sizing
tags:
  - rdp
  - freerdp
  - pth
platforms:
  - Linux
verified: true
validated: true
---

# freerdp-connect-with-credentials

## Command

```bash
xfreerdp /v:$_TARGET_IP /u:$_USERNAME /p:$_PASSWORD /d:$_DOMAIN +clipboard /cert-ignore /size:$_RESOLUTION /smart-sizing
```

## Description

Uses FreeRDP to connect to a Windows RDP server with credentials, enabling clipboard and ignoring certs. Supports pass-the-hash with /pth for advanced auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /v:$_TARGET_IP | Target IP/hostname | Yes |
| /u:$_USERNAME | Username | Yes |
| /p:$_PASSWORD | Password (or omit for prompt) | No |
| /d:$_DOMAIN | Domain | No |
| /pth:$_HASH | NTLM hash for pass-the-hash | No (for PTH) |
| +clipboard | Enable clipboard sharing | No |
| /cert-ignore | Skip cert validation | No |
| /size:$_RESOLUTION | Screen resolution (e.g., 1366x768) | No |
| /smart-sizing | Enable dynamic scaling | No |

## Examples

### Basic Usage

```bash
xfreerdp /v:10.10.10.10 /u:admin /p:pass123 +clipboard /cert-ignore /size:1366x768 /smart-sizing
```

### Pass-the-Hash Usage

```bash
xfreerdp /v:10.10.10.10 /u:admin /d:corp /pth:88a405e17c0aa5debbc9b5679753939d /cert-ignore
```

## Expected Output

[freerdp] loading channel rdpdr
[freerdp] loading channel cliprdr
Connected successfully
[RDP session opens]

## Related

- [[procedures/RDP-Remote-Code-Execution]]
- [[tools/FreeRDP]]
