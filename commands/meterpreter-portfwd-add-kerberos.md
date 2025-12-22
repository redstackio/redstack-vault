---
id: 170c7951-ce28-4be5-86a1-320591113c02-b
name: meterpreter-portfwd-add-kerberos
type: command
executor: msfconsole
data: portfwd add -l 88 -p 88 -r 127.0.0.1
output: null
created_at: '2023-04-06T03:56:22.631643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - kerberos
  - meterpreter
verified: true
validated: true
---

# meterpreter-portfwd-add-kerberos

## Command

```msfconsole
portfwd add -l 88 -p 88 -r 127.0.0.1
```

## Description

Adds a port forward for Kerberos traffic (port 88) looping back to the compromised host itself, useful for local authentication pivoting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 88 | Local port to listen on | Yes |
| -p 88 | Remote port to forward to | Yes |
| -r 127.0.0.1 | Loopback to pivot host | Yes |

## Examples

### Basic Usage

```msfconsole
portfwd add -l 88 -p 88 -r 127.0.0.1
```

## Expected Output

[*] Added port forward 88 => 88:127.0.0.1 (TCP)

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
