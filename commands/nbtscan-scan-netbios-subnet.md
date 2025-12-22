---
type: command
executor: bash
data: nbtscan $_TARGET_SUBNET/$_CIDR
platforms:
  - Linux
  - Windows
tags:
  - enumeration
  - network
  - netbios
verified: true
validated: true
---

# nbtscan-scan-netbios-subnet

## Command

```bash
nbtscan $_TARGET_SUBNET/$_CIDR
```

## Description

This command scans a specified subnet for systems running NetBIOS, querying each address in the range for NetBIOS status information. It reveals responding hosts' IP addresses, NetBIOS computer names, logged-in users, and MAC addresses, useful for network enumeration during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_SUBNET | The base IP address of the subnet to scan (e.g., 10.10.10.0) | Yes |
| $_CIDR | The CIDR notation for the subnet mask (e.g., 24 for /24) | Yes |

## Examples

### Basic Usage

Scan the 10.10.10.0/24 subnet:

```bash
nbtscan 10.10.10.0/24
```

### Advanced Usage

Scan a smaller range like /28:

```bash
nbtscan 192.168.1.0/28
```

## Expected Output

```
Doing NBT name scan for addresses from 10.10.10.0/24

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
10.10.10.0       Sendto failed: Permission denied
10.10.10.10      BOB-PC    <server>  <unknown>        00:0c:29:72:eb:b4
10.10.10.230     ALICE-PC  <server>  <unknown>        00:1a:20:66:ca:c2
10.10.10.235     WIN95-PC            ADMINISTRATOR    00:0c:29:5d:0c:2f
10.10.10.255     Sendto failed: Permission denied
```

The output lists responding hosts with their NetBIOS details; failures indicate non-responsive or permission-denied addresses.

## Related

- [[Related Procedure: Enumerate-NetBIOS-Hosts]]
- [[tools/nbtscan]]
