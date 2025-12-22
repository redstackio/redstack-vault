---
id: 7931e55f-7cb9-4533-9586-74b190172a75
name: sniffjoke
type: tool
verified: true
created_at: '2019-08-28T21:17:41.036236+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - evasion
  - network-obfuscation
  - ids-evasion
url: 'https://github.com/evilsocket/sniffjoke'
validated: true
---

# sniffjoke

**Status**: Unverified

## Overview

SniffJoke is a Linux-based tool designed to protect TCP connections from passive wiretapping by injecting fake packets, delaying transmissions, and modifying traffic. It is commonly used in offensive security operations to evade intrusion detection systems (IDS) and network sniffers during reconnaissance or command-and-control communications.

## Description

SniffJoke operates by transparently proxying TCP connections and applying evasion techniques such as packet fragmentation, sequence number manipulation, and insertion of bogus data. This makes it difficult for passive monitoring tools to reconstruct or interpret the real traffic. It is particularly useful in red team engagements where maintaining stealthy network communications is critical. The tool requires root privileges and works on a per-interface basis.

## Features

- Feature 1: Transparent TCP connection handling without application modifications
- Feature 2: Configurable packet injection and delay rules for custom evasion strategies
- Feature 3: Support for multiple network interfaces and protocol-specific obfuscation
- Feature 4: Integration with iptables for traffic redirection

## Installation

### Requirements

- Linux kernel with iptables support
- Root access for installation and execution
- Build tools (gcc, make) for compilation from source

### Install Commands

```bash
# On Ubuntu/Debian (if available in repos, otherwise from source)
sudo apt update
sudo apt install sniffjoke

# From source (recommended for latest version)
git clone https://github.com/evilsocket/sniffjoke.git
cd sniffjoke
./autogen.sh
./configure
make
sudo make install
```

## Basic Usage

```bash
sniffjoke --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --iface` | Specify network interface (e.g., eth0) |
| `-f, --file` | Load configuration from file |
| `-v, --version` | Display version information |
| `-d, --daemon` | Run in background mode |

## Examples

### Example 1: Basic Usage

Start SniffJoke on the default interface:

```bash
sudo sniffjoke -i eth0
```

### Example 2: Advanced Usage

Start with a custom configuration for specific ports:

```bash
sudo sniffjoke -i wlan0 -f /etc/sniffjoke.rules
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify System Firewall]] Disable or Modify Tools (network monitoring evasion)
- [[Software Packing]] Software Packing (traffic obfuscation)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual TCP sequence anomalies or delayed packets in network traffic
- Detection method 2: Presence of SniffJoke processes (ps aux | grep sniffjoke) or iptables rules redirecting traffic
- Detection method 3: Increased packet fragmentation on monitored interfaces

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official GitHub Repository: https://github.com/evilsocket/sniffjoke
- Documentation: https://github.com/evilsocket/sniffjoke/blob/master/README.md

## Related Commands

- [[commands/sniffjoke-version-check]]
- [[commands/sniffjoke-start-basic]]
- [[commands/sniffjoke-start-with-config]]
