---
id: 0d4d7411-a5be-45d4-b747-ba415cbe183a
type: tool
verified: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - reconnaissance
  - network-scanning
  - firewall-mapping
url: 'http://packetfactory.openwall.com/firewalk/'
validated: true
---

# firewalk

**Status**: Unverified

## Overview

Firewalk is an active reconnaissance network security tool designed to determine which Layer 4 protocols (TCP, UDP, ICMP) a given IP forwarding device, such as a firewall or router, will pass. It is commonly used in penetration testing to map firewall rules and identify allowed traffic patterns without directly interacting with the target host.

## Description

Firewalk operates by sending customized packets with a TTL value set to one greater than the targeted gateway. If the gateway permits the traffic, it forwards the packets to the next hop, where they expire, generating an ICMP_TIME_EXCEEDED response. If the traffic is blocked, the packets are dropped, resulting in no response. To accurately target the gateway, Firewalk first performs a binding phase similar to traceroute, incrementally increasing the TTL to identify the hop count to the gateway. Once bound, it scans specific protocols and ports. Notably, the scan does not require reaching the ultimate destination host; it only needs a downstream target beyond the gateway.

## Features

- Protocol-specific scanning for TCP, UDP, and ICMP
- Automatic hop counting and binding to the target gateway
- Customizable source ports, local IPs, and timeouts
- Analysis of firewall filtering rules based on response patterns
- Support for scanning multiple ports or protocol variations

## Installation

### Requirements

- Linux environment (tested on Ubuntu/Debian derivatives)
- Development libraries: libnet1-dev and libpcap-dev
- GCC compiler for building from source

### Install Commands

```bash
# Install dependencies on Ubuntu/Debian
sudo apt update
sudo apt install libnet1-dev libpcap-dev gcc make

# Download and compile Firewalk (source from archive, as it's an older tool)
wget https://www.cse.scu.edu/~rstandley/firewalk/firewalk-5.0.tgz

tar xzf firewalk-5.0.tgz
cd firewalk-5.0
make
sudo make install
```

Note: Firewalk is not available in standard package repositories for modern distributions and must be compiled from source. Ensure you have root privileges for installation.

## Basic Usage

```bash
firewalk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P <protocol>` | Specify protocol (tcp, udp, icmp) |
| `-p <port>` | Destination port to scan |
| `-S <srcport>` | Source port for packets |
| `-T <timeout>` | Timeout in seconds for responses (default 3) |
| `-L <localip>` | Local source IP address |
| `-h <gateway>` | IP of the target gateway/firewall |
| `<target>` | Downstream target IP (beyond the gateway) |
| `-V` | Verbose output |
| `-i <interface>` | Network interface to use |

## Examples

### Example 1: Basic TCP Scan

Scan TCP port 80 through a gateway to map firewall rules.

```bash
firewalk -P tcp -p 80 -h 192.168.1.1 10.0.0.1
```

### Example 2: UDP Port Scan with Custom Timeout

Perform a UDP scan on port 53 with a 5-second timeout.

```bash
firewalk -P udp -p 53 -T 5 -h 192.168.1.1 10.0.0.1
```

### Example 3: TCP Scan with Source Port and Local IP

Use a specific source port and local IP for the scan.

```bash
firewalk -P tcp -p 443 -S 12345 -L 192.168.1.100 -h 192.168.1.1 10.0.0.1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[System Network Configuration Discovery]] System Network Configuration Discovery

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual ICMP_TIME_EXCEEDED messages from network devices
- Incremental TTL patterns in outbound traffic resembling traceroute but with protocol variations
- High volume of crafted packets to gateways with varying protocols/ports
- Network logs showing scans from reconnaissance tools (signature-based IDS rules for Firewalk packet patterns)
- Monitor for libnet-based packet crafting on internal hosts

## Related Commands

- [[commands/firewalk-tcp-port-scan]]
- [[commands/firewalk-udp-port-scan]]

## References

- Original Firewalk documentation: http://packetfactory.openwall.com/firewalk/
- Source code archive: https://www.cse.scu.edu/~rstandley/firewalk/
- Related reading: Network reconnaissance techniques in "Hacking: The Art of Exploitation"
