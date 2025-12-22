---
id: 7464fa1b-15c3-49d6-844d-6782a5df4def
type: tool
verified: true
created_at: '2019-08-28T21:17:19.325739Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - dos
  - sip
  - flood
  - network
url: 'https://tools.kali.org/networking/inviteflood'
validated: true
---

# inviteflood

**Status**: Unverified

## Overview

inviteflood is a specialized tool for conducting denial-of-service (DoS) attacks on SIP (Session Initiation Protocol) and SDP (Session Description Protocol) endpoints by flooding them with INVITE messages over UDP/IP. It is commonly used in penetration testing to assess the resilience of VoIP infrastructure against flooding attacks. The tool generates and sends rapid bursts of INVITE packets to overwhelm target servers, simulating real-world attack scenarios.

## Description

Developed for Linux environments, inviteflood targets SIP-based communication systems, which are prevalent in VoIP telephony. By flooding the target with INVITE messages—requests that initiate sessions—it can exhaust resources like CPU, memory, or bandwidth on the receiving end. Tested originally on Red Hat Fedora Core 4, it compiles and runs on modern Linux distributions. This tool is part of the Kali Linux distribution and is intended for ethical hacking and security research, not malicious use.

## Features

- UDP-based INVITE message flooding for SIP/SDP protocols
- Configurable packet count, target IP/port, and network interface
- Lightweight and efficient for high-volume packet generation
- Cross-compatible with various Linux kernels and distributions

## Installation

### Requirements

- Linux system (tested on Red Hat Fedora Core 4 and later distributions like Ubuntu/Kali)
- GCC compiler for building from source
- Root privileges for raw socket access (if needed for high-rate flooding)

### Install Commands

On Kali Linux (pre-packaged):

```bash
sudo apt update
sudo apt install inviteflood
```

On Ubuntu/Debian (from source):

```bash
sudo apt update
sudo apt install build-essential
wget https://example-repo/inviteflood.tar.gz  # Replace with actual source URL
tar -xzf inviteflood.tar.gz
cd inviteflood
make
sudo make install
```

On other Linux distributions, compile from the official repository.

## Basic Usage

```bash
inviteflood --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --dest | Target IP address |
| -p, --port | Target port (default: 5060) |
| -c, --count | Number of packets to send |
| -i, --interface | Sending interface |
| -h, --help | Display help |

## Examples

### Example 1: Basic Usage

Flood a target SIP server with 10,000 INVITE messages:

```bash
inviteflood -d 192.168.1.100 -p 5060 -c 10000
```

### Example 2: Advanced Usage

Specify interface for a controlled test:

```bash
inviteflood -d 10.0.0.50 -p 5060 -c 50000 -i eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Flood

### Tactics

- [[Impact]] Impact

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual UDP traffic spikes to port 5060 from a single source
- High volume of malformed SIP INVITE packets in network logs (e.g., via Wireshark or Suricata)
- Resource exhaustion on SIP servers (CPU/memory spikes correlated with traffic)
- Process monitoring for 'inviteflood' binary execution

## Related Procedures

- [[procedures/SIP-DoS-Flooding]]

## Related Tools

- [[tools/sipvicious]]
- [[tools/scapy]]

## References

- Official Kali Documentation: https://tools.kali.org/networking/inviteflood
- GitHub Repository: https://github.com/kali-tools/inviteflood (if available)
- SIP Protocol RFC: https://tools.ietf.org/html/rfc3261
