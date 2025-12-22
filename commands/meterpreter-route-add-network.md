---
id: d07d4c05-aba2-49db-95b6-2448808a15c5
name: meterpreter-route-add-network
type: command
executor: msfconsole
data: route add $_NETWORK $_NETMASK $_SESSION_ID
output: null
created_at: '2023-04-06T03:56:22.632099+00:00'
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

# meterpreter-route-add-network

## Command

```msfconsole
route add $_NETWORK $_NETMASK $_SESSION_ID
```

## Description

Manually adds a route for a specific network through a Meterpreter session ID.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NETWORK | Target network, e.g., 192.168.14.0 | Yes |
| $_NETMASK | Subnet mask, e.g., 255.255.255.0 | Yes |
| $_SESSION_ID | Meterpreter session ID | Yes |

## Examples

### Basic Usage

```msfconsole
route add 192.168.14.0 255.255.255.0 3
```

## Expected Output

[*] Route added: 192.168.14.0/255.255.255.0 via session 3

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
