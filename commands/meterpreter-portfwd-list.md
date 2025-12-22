---
id: 41693039-776d-4121-9445-deb4c56a51f5
name: meterpreter-portfwd-list
type: command
executor: msfconsole
data: portfwd list
output: null
created_at: '2023-04-06T03:56:22.631581+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - meterpreter
verified: true
validated: true
---

# meterpreter-portfwd-list

## Command

```msfconsole
portfwd list
```

## Description

Lists all active port forwarding rules configured in the current Meterpreter session, showing local and remote ports, hosts, and protocols.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; lists all forwards | No |

## Examples

### Basic Usage

```msfconsole
portfwd list
```

## Expected Output

[*] Local port forwards:
[*]   3389 => 3389:192.168.1.100 (TCP)
[*]   445 => 445:10.0.0.50 (TCP)

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
