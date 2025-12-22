---
id: dcc86a4b-b976-4547-b25f-576f5abbf475
name: meterpreter-autoroute-add-subnet
type: command
executor: msfconsole
data: run autoroute -s $_SUBNET
output: null
created_at: '2023-04-06T03:56:22.631830+00:00'
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

# meterpreter-autoroute-add-subnet

## Command

```msfconsole
run autoroute -s $_SUBNET
```

## Description

Runs the autoroute post module to add a route for a specified subnet through the active Meterpreter session, enabling pivoting to that network.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s $_SUBNET | Subnet to route, e.g., 192.168.15.0/24 | Yes |

## Examples

### Basic Usage

```msfconsole
run autoroute -s 192.168.15.0/24
```

## Expected Output

[*] Adding route for network 192.168.15.0/255.255.255.0
[*] Route added successfully

## Related

- [[procedures/Meterpreter-Network-Pivoting-via-Port-Forwarding-and-Routing]]
