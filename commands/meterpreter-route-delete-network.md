---
id: b1da95f2-bf74-43d8-81c7-9d86851e4138
name: meterpreter-route-delete-network
type: command
executor: msfconsole
data: route delete $_NETWORK $_NETMASK $_SESSION_ID
output: null
created_at: '2023-04-06T03:56:22.632122+00:00'
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

# meterpreter-route-delete-network

## Command

```msfconsole
route delete $_NETWORK $_NETMASK $_SESSION_ID
```

## Description

Removes a specific route from the Meterpreter routing table.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_NETWORK | Network to delete | Yes |
| $_NETMASK | Subnet mask | Yes |
| $_SESSION_ID | Session ID | Yes |

## Examples

### Basic Usage

```msfconsole
route delete 192.168.14.0 255.255.255.0 3
```

## Expected Output

[*] Route deleted: 192.168.14.0/255.255.255.0 via session 3

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
