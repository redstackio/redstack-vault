---
id: c127a8c7-b624-4d92-af9e-1fe5f5121a60
name: meterpreter-route-flush
type: command
executor: msfconsole
data: route flush
output: null
created_at: '2023-04-06T03:56:22.632175+00:00'
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

# meterpreter-route-flush

## Command

```msfconsole
route flush
```

## Description

Flushes all routes from the Meterpreter routing table for cleanup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Removes all routes | No |

## Examples

### Basic Usage

```msfconsole
route flush
```

## Expected Output

[*] All routes flushed

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
