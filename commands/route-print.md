---
type: command
executor: cmd
data: route print
output: null
platforms:
  - Windows
tags:
  - network-enumeration
  - discovery
verified: true
validated: true
---

# route-print

## Command

```cmd
route print
```

## Description

Prints the IPv4 routing table, showing destinations, gateways, and interfaces. Essential for understanding network paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| print | Displays the route table | Yes |

## Examples

### Basic Usage

```cmd
route print
```

## Expected Output

```
IPv4 Route Table
===========================================================================
Active Routes:
 Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0      192.168.1.1    192.168.1.100     25
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
```

## Related

- [[procedures/windows-network-enumeration-for-privilege-escalation]]
