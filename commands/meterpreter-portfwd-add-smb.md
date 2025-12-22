---
id: 170c7951-ce28-4be5-86a1-320591113c02-c
name: meterpreter-portfwd-add-smb
type: command
executor: msfconsole
data: portfwd add -L 0.0.0.0 -l 445 -r $_REMOTE_HOST -p 445
output: null
created_at: '2023-04-06T03:56:22.631643+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - smb
  - meterpreter
verified: true
validated: true
---

# meterpreter-portfwd-add-smb

## Command

```msfconsole
portfwd add -L 0.0.0.0 -l 445 -r $_REMOTE_HOST -p 445
```

## Description

Adds a port forward for SMB traffic (port 445) binding to all local interfaces, proxying to a remote host via the pivot for file share access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -L 0.0.0.0 | Bind to all local interfaces | Yes |
| -l 445 | Local port to listen on | Yes |
| -r $_REMOTE_HOST | Remote host IP | Yes |
| -p 445 | Remote port | Yes |

## Examples

### Basic Usage

```msfconsole
portfwd add -L 0.0.0.0 -l 445 -r 192.168.57.102 -p 445
```

## Expected Output

[*] Added port forward 0.0.0.0:445 => 445:192.168.57.102 (TCP)

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
