---
id: 89dc25e7-2307-42bc-a467-64cc1995080c
type: tool
verified: true
created_at: '2019-08-28T21:17:28.539604+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - vpn
  - ike
  - mitm
  - cisco
  - credential-access
url: 'https://github.com/nullsecuritynet/tools/tree/master/ip/fiked'
validated: true
---

# fiked

**Status**: Unverified

## Overview

fiked (FakeIKEd) is a specialized tool for performing semi-man-in-the-middle (MitM) attacks against insecure Cisco VPN setups using PSK+XAUTH based IPsec authentication. It acts as a fake IKE daemon, impersonating a VPN gateway's IKE responder to capture XAUTH login credentials without fully implementing the client side of a complete MitM.

## Description

fiked supports just enough of the IKE standards and Cisco-specific extensions to trick VPN clients into revealing their credentials during authentication. This makes it useful in penetration testing scenarios where attackers position themselves to intercept IKE negotiations, such as on compromised networks or via ARP spoofing. It is particularly effective against legacy or misconfigured Cisco VPN concentrators that rely on weak pre-shared key (PSK) and extended authentication (XAUTH) mechanisms. Once credentials are captured, they can be used for further lateral movement or direct access to the VPN.

## Features

- Impersonates IKE responder to capture XAUTH usernames and passwords
- Supports Cisco VPN PSK+XAUTH authentication protocols
- Lightweight daemon mode for persistent listening
- Logs captured credentials to file for easy extraction
- Minimal implementation focused on credential theft without full IPsec tunnel support

## Installation

### Requirements

- Linux system with kernel support for raw sockets (e.g., Ubuntu, Kali)
- GCC compiler and make utilities
- libpcap-dev for packet capture (if extended sniffing is needed)

### Install Commands

```bash
# Download and extract the source
wget https://github.com/nullsecuritynet/tools/archive/master.zip
unzip master.zip
cd tools-master/ip/fiked

# Compile
make

# Install to /usr/local/bin (optional)
sudo make install
```

On Kali Linux, it may be available via apt or pre-compiled in security tool repositories.

## Basic Usage

```bash
fiked -i eth0
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Specify the network interface to listen on (e.g., eth0) |
| `-d` | Run in daemon mode (background) |
| `-p <pidfile>` | Specify PID file for daemon |
| `-l <logfile>` | Log captured credentials to a file |
| `-h` | Show help message |

## Examples

### Example 1: Basic Usage

Listen on the default interface to capture IKE packets:

```bash
sudo fiked -i eth0
```

This will start the fake IKE daemon, responding to incoming IKE initiation packets from VPN clients and logging any XAUTH credentials.

### Example 2: Advanced Usage

Run in daemon mode with logging:

```bash
sudo fiked -i eth0 -d -l /tmp/fiked_creds.log -p /var/run/fiked.pid
```

Monitor the log file for captured usernames and passwords.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Modify Authentication Process]] Modify Authentication Process

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual IKE daemon processes (e.g., fiked binary running on non-VPN servers)
- Network traffic anomalies: Fake IKE responses (ISAKMP packets) from unauthorized IPs
- Log analysis for XAUTH credential dumps in unexpected locations
- Process monitoring for raw socket usage on network interfaces

## Related Commands

- [[commands/fiked-listen-interface]]
- [[commands/fiked-daemon-log]]

## References

- Official repository: https://github.com/nullsecuritynet/tools/tree/master/ip/fiked
- IKE protocol documentation: RFC 2409
- Cisco XAUTH extensions: Cisco IPsec documentation
