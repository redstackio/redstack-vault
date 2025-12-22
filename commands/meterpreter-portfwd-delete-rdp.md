---
id: ed8d3277-fbaa-4d52-9c6f-78c7a73ed81b
name: meterpreter-portfwd-delete-rdp
type: command
executor: msfconsole
data: portfwd delete -l 3389 -p 3389 -r $_TARGET_HOST
output: null
created_at: '2023-04-06T03:56:22.631702+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - cleanup
  - meterpreter
verified: true
validated: true
---

# meterpreter-portfwd-delete-rdp

## Command

```msfconsole
portfwd delete -l 3389 -p 3389 -r $_TARGET_HOST
```

## Description

Removes a specific RDP port forward rule from the Meterpreter session to clean up after use.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -l 3389 | Local port of the forward | Yes |
| -p 3389 | Remote port of the forward | Yes |
| -r $_TARGET_HOST | Remote host of the forward | Yes |

## Examples

### Basic Usage

```msfconsole
portfwd delete -l 3389 -p 3389 -r 192.168.1.100
```

## Expected Output

[*] Removed port forward 3389 => 3389:192.168.1.100 (TCP)

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
