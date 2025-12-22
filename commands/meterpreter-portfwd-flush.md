---
id: 9e42f2e6-35b5-4c80-be34-1c48ad94032b
name: meterpreter-portfwd-flush
type: command
executor: msfconsole
data: portfwd flush
output: null
created_at: '2023-04-06T03:56:22.631786+00:00'
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

# meterpreter-portfwd-flush

## Command

```msfconsole
portfwd flush
```

## Description

Removes all active port forwarding rules in the Meterpreter session for complete cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Flushes all forwards | No |

## Examples

### Basic Usage

```msfconsole
portfwd flush
```

## Expected Output

[*] All port forwards removed

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
