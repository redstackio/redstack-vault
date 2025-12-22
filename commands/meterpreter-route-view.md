---
id: 4507597a-5cf0-4ebc-9d9c-30bae99098fa
name: meterpreter-route-view
type: command
executor: msfconsole
data: route
output: null
created_at: '2023-04-06T03:56:22.632055+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - pivoting
  - routing
  - meterpreter
verified: true
validated: true
---

# meterpreter-route-view

## Command

```msfconsole
route
```

## Description

Displays the current routing table and available networks from the Meterpreter session's perspective.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Shows routes and interfaces | No |

## Examples

### Basic Usage

```msfconsole
route
```

## Expected Output

[*] Routes
[*]   0.0.0.0/0 via 192.168.1.1
[*]   10.0.0.0/24 via session 1

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
