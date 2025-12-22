---
id: ec216abb-ae50-4b97-b863-612be9b9be1c
name: hex2raw
type: tool
verified: true
created_at: '2019-08-28T21:17:30.292851+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - packet-crafting
  - network-injection
  - sniffing
url: 'https://github.com/securityoffense/HexInject'
validated: true
---

# hex2raw

**Status**: Unverified

## Overview

hex2raw is a utility from the HexInject suite, designed for converting hexadecimal representations of network packets into raw binary format. It is primarily used in network security testing for crafting custom packets that can be injected into the network, facilitating tasks like fuzzing, spoofing, and traffic manipulation. Common use cases include red team operations involving packet injection for evasion or simulation of attacks.

## Description

HexInject provides a command-line framework for raw network access, including sniffing and injection capabilities. hex2raw specifically handles the conversion of hex dumps (from tools like Wireshark or manual crafting) to binary packets suitable for injection. It works seamlessly with other CLI tools, enabling shell scripts for automated packet generation, interception, and modification. This makes it valuable for transparent network traffic analysis and manipulation in offensive security scenarios.

## Features

- Feature 1: Direct hex string to raw binary conversion for quick prototyping.
- Feature 2: File-based input support for batch processing hex dumps.
- Feature 3: Integration with inject and sniff tools in the HexInject suite for end-to-end packet workflows.
- Feature 4: Lightweight and scriptable, requiring no GUI.

## Installation

### Requirements

- Linux kernel with raw socket support (most distributions).
- GCC compiler for building from source.
- Root privileges for packet injection (though hex2raw itself does not require root for conversion).

### Install Commands

HexInject (including hex2raw) is not pre-installed on most distros; build from source:

```bash
# Clone the repository
git clone https://github.com/securityoffense/HexInject.git
cd HexInject

# Compile
make

# Install (optional, or just use binaries in place)
sudo make install
```

On Kali Linux, it may be available via community packages, but compiling is recommended for the latest version.

## Basic Usage

```bash
hex2raw --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage. |
| -o, --output | Specify output file for raw binary (default: stdout). |

## Examples

### Example 1: Basic Usage

Convert a hex string to raw and save to file:

```bash
hex2raw "4500003c..." -o packet.raw
```

### Example 2: Advanced Usage

Process a file of hex packets and pipe to injector:

```bash
hex2raw hex_dump.txt -o - | sudo inject -i eth0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (for analyzing captured hex dumps).
- [[SSH]] Traffic Duplication (for crafting and injecting duplicate packets).

### Tactics

- [[Impact]] Impact (via traffic disruption).
- [[Initial Access]] Initial Access (via crafted packets exploiting services).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual raw socket creations or hex-to-binary file conversions in process logs.
- Detection method 2: Network IDS alerts on injected packets with malformed or spoofed headers.
- Detection method 3: File system scans for .raw files or HexInject binaries in temporary directories.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[inject]] (companion tool for packet injection).
- [[sniff]] (for capturing hex dumps to feed into hex2raw).
- [[tools/Wireshark]] (for generating hex inputs).

## References

- Official GitHub: https://github.com/securityoffense/HexInject
- Man page: Available after installation via `man hex2raw`.
