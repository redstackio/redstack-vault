---
id: 6bc7a8d5-8b84-40b2-b0b0-8a868afc57ed
name: responder-analyze-incoming-requests
type: command
executor: bash
data: responder -I eth0 -A
output: null
created_at: '2023-04-06T03:56:22.270819+00:00'
updated_at: '2023-04-10T20:25:10.736475+00:00'
platforms:
  - Linux
tags:
  - network-discovery
  - responder
  - analyze
verified: true
validated: true
---

# responder-analyze-incoming-requests

## Command

```bash
responder -I $_INTERFACE -A
```

## Description

This command runs Responder in analysis mode to passively monitor and log incoming LLMNR, NBT-NS, and BROWSER requests without sending any spoofed responses. Use it for reconnaissance to understand name resolution activity on the network before launching active attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -I $_INTERFACE | Network interface to listen on (e.g., eth0, wlan0) | Yes |
| -A | Analysis mode: Log requests without responding | Yes |

## Examples

### Basic Usage

```bash
responder -I eth0 -A
```

### Advanced Usage

Run on a specific interface for extended monitoring:

```bash
responder -I wlan0 -A
```

## Expected Output

Console logs of incoming requests, such as:

```
[*] [LLMNR]  192.168.1.100 requested 'nonexistent' > [SID: None], [AUTH: None]
[*] [NBT-NS] 192.168.1.101 requested 'hostname' > [SID: None], [AUTH: None]
```
No responses are sent; output shows query sources and targets for mapping network behavior.

## Related

- [[procedures/LLMNR-NBT-NS-Poisoning-with-Responder]]
- [[commands/responder-enable-poisoning-and-wpad]]
