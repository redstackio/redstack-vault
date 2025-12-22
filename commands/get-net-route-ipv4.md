---
type: command
executor: powershell
data: >-
  Get-NetRoute -AddressFamily IPv4 | ft
  DestinationPrefix,NextHop,RouteMetric,ifIndex
output: null
platforms:
  - Windows
tags:
  - network-enumeration
  - discovery
verified: true
validated: true
---

# get-net-route-ipv4

## Command

```powershell
Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
```

## Description

Retrieves and formats the IPv4 routing table in PowerShell, highlighting prefixes, next hops, metrics, and interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -AddressFamily | Limits to IPv4 | Yes |
| DestinationPrefix | Route destination | Built-in |
| NextHop | Gateway IP | Built-in |
| RouteMetric | Cost of route | Built-in |
| ifIndex | Interface index | Built-in |
| ft | Table format | Yes |

## Examples

### Basic Usage

```powershell
Get-NetRoute -AddressFamily IPv4 | ft DestinationPrefix,NextHop,RouteMetric,ifIndex
```

## Expected Output

```
DestinationPrefix NextHop       RouteMetric ifIndex
----------------- -------       ------------ -------
0.0.0.0/0         192.168.1.1  25          12
127.0.0.0/8       OnLink       331         1
192.168.1.0/24    OnLink       281         12
```

## Related

- [[procedures/windows-network-enumeration-for-privilege-escalation]]
