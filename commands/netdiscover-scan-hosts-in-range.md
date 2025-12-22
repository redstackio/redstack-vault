---
id: 8b7de332-c7f5-4a8c-8055-e3a811b1dff6
name: netdiscover-scan-hosts-in-range
type: command
executor: bash
data: netdiscover -i $_INTERFACE -r $_IP_RANGE
output: null
created_at: '2023-04-06T03:56:22.242964+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - network-discovery
  - arp-scan
verified: true
validated: true
---

# netdiscover-scan-hosts-in-range

## Command

```bash
netdiscover -i $_INTERFACE -r $_IP_RANGE
```

## Description

This command uses Netdiscover to perform an active ARP-based scan of a specified IP range on a given network interface, discovering live hosts and their MAC addresses. It is ideal for local network enumeration during reconnaissance phases.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INTERFACE | Specifies the network interface to use (e.g., eth0, wlan0) | Yes |
| -r $_IP_RANGE | Defines the IP range to scan (e.g., 192.168.1.0/24) | Yes |
| -p | Enables passive mode (listens only, no ARP requests) | No |
| -o | Outputs results to a file | No |

## Examples

### Basic Usage

```bash
netdiscover -i eth0 -r 192.168.1.0/24
```

Scan the 192.168.1.0/24 subnet on eth0.

### Advanced Usage

```bash
netdiscover -i eth0 -r 10.0.0.0/16 -p
```

Passive scan of a larger range to avoid detection.

## Expected Output

Real-time display of discovered hosts, ending with a summary table:

```
Currently scanning: Finished!   |   Screen View: Unique Hosts

20 Captured ARP Req/Rep packets, from 4 hosts.   Total size: 876
_____________________________________________________________________________
IP            At MAC Address     Count     Len  MAC Vendor / Hostname
-----------------------------------------------------------------------------
192.168.1.AA    68:AA:AA:AA:AA:AA     15     630  Sagemcom
192.168.1.XX    52:XX:XX:XX:XX:XX      1      60  Unknown vendor
192.168.1.YY    24:YY:YY:YY:YY:YY      1      60  QNAP Systems, Inc.
192.168.1.ZZ    b8:ZZ:ZZ:ZZ:ZZ:ZZ      3     126  HUAWEI TECHNOLOGIES CO.,LTD  
```

Success is indicated by the presence of expected hosts; empty results may mean no live devices or incorrect range/interface.

## Related

- [[procedures/Netdiscover-Network-Discovery]]
- [[tools/Netdiscover]]
