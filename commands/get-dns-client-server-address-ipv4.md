---
type: command
executor: powershell
data: Get-DnsClientServerAddress -AddressFamily IPv4 | ft
output: null
platforms:
  - Windows
tags:
  - network-enumeration
  - discovery
verified: true
validated: true
---

# get-dns-client-server-address-ipv4

## Command

```powershell
Get-DnsClientServerAddress -AddressFamily IPv4 | ft
```

## Description

Lists DNS server addresses configured for IPv4 interfaces. Helps identify internal DNS infrastructure for potential targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -AddressFamily | Specifies IPv4 | Yes |
| ft | Formats output as table | Yes |

## Examples

### Basic Usage

```powershell
Get-DnsClientServerAddress -AddressFamily IPv4 | ft
```

## Expected Output

```
InterfaceAlias ServerAddresses
-------------- --------------
Ethernet       {192.168.1.10, 8.8.8.8}
Wi-Fi          {10.0.0.10}
```

## Related

- [[procedures/windows-network-enumeration-for-privilege-escalation]]
