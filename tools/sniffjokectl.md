---
id: bd14654b-8337-4a34-b902-31855ae2a63b
type: tool
verified: true
created_at: '2019-08-28T21:17:37.629522+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
description: >-
  Control interface for SniffJoke, a Linux tool that injects fake packets into
  TCP connections to evade passive network sniffing and intrusion detection
  systems.
url: 'https://github.com/evilsocket/sniffjoke'
platforms:
  - Linux
tags:
  - evasion
  - tcp-manipulation
  - network-defense-evasion
  - ids-evasion
commands:
  - '[[commands/sniffjokectl-start-daemon]]'
  - '[[commands/sniffjokectl-status-check]]'
  - '[[commands/sniffjokectl-stop-daemon]]'
validated: true
---

# sniffjokectl

**Status**: Unverified

## Overview

sniffjokectl is the command-line control tool for SniffJoke, a utility designed to protect TCP connections from passive wiretapping by injecting deceptive packets, delaying transmissions, and modifying traffic. It is commonly used in offensive security operations to evade detection by network intrusion detection systems (IDS) or packet sniffers during red team engagements or when maintaining operational security over compromised networks.

## Description

SniffJoke operates as a transparent proxy for TCP connections on Linux systems. When activated, it intercepts outbound TCP traffic, applies evasion techniques such as packet fragmentation, injection of fake segments, and timing manipulations to render captured traffic unreadable or misleading to passive monitoring tools. sniffjokectl provides the interface to manage the SniffJoke daemon, including starting, stopping, and querying its status. This tool is particularly useful in scenarios where attackers need to maintain command-and-control (C2) channels or exfiltrate data without triggering alerts from signature-based defenses.

## Features

- **Daemon Management**: Start, stop, and monitor the SniffJoke service.
- **Evasion Profiles**: Support for predefined strategies to confuse sniffers (e.g., fake packet injection, TCP sequence disruption).
- **Transparent Operation**: Works without modifying application code, handling connections at the kernel level via iptables integration.
- **Status Reporting**: Real-time feedback on active connections and evasion effectiveness.
- **Customizable Rules**: Ability to define specific hosts or ports for evasion application.

## Installation

### Requirements

- Linux kernel with iptables support.
- Root privileges for daemon operations.
- Dependencies: libevent, libnetfilter-queue (install via package manager).

### Install Commands

For Ubuntu/Debian/Kali:

```bash
sudo apt update
sudo apt install build-essential libevent-dev libnetfilter-queue-dev libpcap-dev
wget https://github.com/evilsocket/sniffjoke/archive/master.zip
unzip master.zip
cd sniffjoke-master
make
sudo make install
```

The tool installs the `sniffjoke` daemon and `sniffjokectl` binary to `/usr/local/bin/`.

## Basic Usage

```bash
sniffjokectl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Display help message and usage. |
| `-v, --version` | Show SniffJoke version. |
| `--daemon` | Run in daemon mode (for sniffjoke binary). |

## Examples

### Example 1: Basic Usage

Start the SniffJoke daemon:

```bash
sudo sniffjoke --daemon
```

Check status using sniffjokectl:

```bash
sniffjokectl status
```

### Example 2: Advanced Usage

Stop the daemon:

```bash
sniffjokectl stop
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools (to impair IDS/sniffers)
- [[Protocol Tunneling]] Protocol Hijacking (TCP manipulation)

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- **Process Monitoring**: Look for `sniffjoke` processes or `sniffjokectl` executions via `ps aux` or Sysdig.
- **Network Anomalies**: Unusual TCP retransmissions, out-of-order packets, or delayed ACKs in traffic captures (Wireshark filters: `tcp.analysis.retransmission`).
- **Iptables Rules**: Check for NFQUEUE rules redirecting TCP traffic: `sudo iptables -t mangle -L -v -n`.
- **File Artifacts**: Presence of `/usr/local/bin/sniffjoke` or logs in `/var/log/sniffjoke/`.
- **Behavioral**: Increased latency in TCP connections from the host without corresponding network issues.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/iptables]] (for rule management)
- [[tools/tcpdump]] (for traffic analysis)

## References

- Official GitHub Repository: https://github.com/evilsocket/sniffjoke
- Documentation: Included in source or man pages after installation (`man sniffjoke`)
