---
type: command
executor: cmd
data: ipconfig /all
output: null
platforms:
  - Windows
tags:
  - network-enumeration
  - discovery
verified: true
validated: true
---

# ipconfig-all

## Command

```cmd
ipconfig /all
```

## Description

Displays full TCP/IP configuration for all network interfaces, including IP addresses, subnet masks, default gateways, DNS servers, and MAC addresses. Use during initial enumeration to map the local system's network setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /all | Shows detailed info for all adapters | Yes |

## Examples

### Basic Usage

```cmd
ipconfig /all
```

## Expected Output

```
Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : contoso.com
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection
   Physical Address. . . . . . . . . : 00-15-5D-00-12-34
   DHCP Enabled. . . . . . . . . . . : Yes
   Autoconfiguration Enabled . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.100(Preferred)
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 192.168.1.10
```

## Related

- [[procedures/windows-network-enumeration-for-privilege-escalation]]
