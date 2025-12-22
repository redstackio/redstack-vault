---
id: 56e775b7-1b6b-40b2-99f3-0b5a41d6622a
type: tool
verified: true
created_at: '2019-08-28T21:17:22.719987+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - firmware-analysis
  - binary-analysis
  - reverse-engineering
  - extraction
url: 'https://github.com/ReFirmLabs/binwalk'
validated: true
---

# binwalk

**Status**: Unverified

## Overview

Binwalk is a fast, open-source tool used for analyzing, reverse engineering, and extracting firmware images. It scans binary files to identify embedded filesystems, compressed archives, executable code, and other structures commonly found in firmware. In offensive security operations, binwalk is essential for dissecting device firmware to discover vulnerabilities, hidden payloads, or backdoors in IoT devices, routers, and embedded systems.

## Description

Binwalk leverages the libmagic library for signature-based detection, similar to the Unix 'file' command, but includes an extensive custom signature database tailored for firmware components like Linux kernels, bootloaders, squashfs filesystems, and cryptographic signatures. It supports entropy analysis to detect encrypted or compressed regions and can automatically extract identified components. This makes it invaluable for red team exercises involving supply chain attacks, IoT exploitation, or firmware modification.

## Features

- Signature-based scanning for over 100 file types, including firmware-specific formats.
- Entropy analysis to identify potential encrypted or random data sections.
- Automatic extraction of embedded files and archives.
- Support for custom magic signature files to extend detection capabilities.
- Integration with other tools like sasquatch for advanced filesystem extraction.
- Python API for scripting custom analysis workflows.

## Installation

### Requirements

- Python 3.6+ (binwalk is Python-based).
- libmagic development libraries (for signature detection).
- Optional: sasquatch or other extractors for certain filesystems.

### Install Commands

```bash
# On Kali Linux (pre-installed in many distributions)
sudo apt update && sudo apt install binwalk

# On Ubuntu/Debian
sudo apt update && sudo apt install binwalk

# From source (for latest version)
git clone https://github.com/ReFirmLabs/binwalk.git
cd binwalk
sudo python3 setup.py install

# On macOS with Homebrew
brew install binwalk

# On Windows (via WSL or Cygwin recommended)
# Install via pip: pip install binwalk
```

## Basic Usage

```bash
binwalk --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-B, --base` | Treat the supplied file as a firmware image and search for all signatures within it. |
| `-e, --extract` | Automatically extract files as they are discovered. |
| `-E, --entropy` | Calculate Shannon entropy across the file. |
| `-f, --signature` | Use the specified signature file for matching. |
| `-M, --matryoshka` | Perform multiple extraction passes to find nested archives. |
| `-v, --verbose` | Enable verbose output. |

## Examples

### Example 1: Basic Usage

Scan a firmware image for embedded files:

```bash
binwalk firmware.bin
```

### Example 2: Advanced Usage

Extract all identified components with entropy analysis:

```bash
binwalk -e -E firmware.bin
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Forge Web Credentials]] Forge Web Credentials (for analyzing credential storage in firmware).
- [[Obfuscated Files or Information]] Obfuscated Files or Information (detecting packed/embedded payloads).
- [[Registry Run Keys - Startup Folder]] Boot or Logon Initialization Scripts (analyzing bootloaders).

### Tactics

- [[Discovery]] Discovery (identifying system components in firmware).
- [[Collection]] Collection (extracting data from binaries).

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'binwalk' executions on analysis machines.
- File system changes: Creation of '_filename.extracted' directories with extracted files.
- Network activity if binwalk is used in automated scripts fetching signatures.
- Log entries for libmagic database accesses or Python module imports related to binwalk.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/foremost]] (file carving from disk images).
- [[strings]] (extracting printable strings from binaries).
- [[tools/DD]] (binary slicing for targeted analysis).

## References

- Official GitHub: https://github.com/ReFirmLabs/binwalk
- Documentation: https://github.com/ReFirmLabs/binwalk/wiki
- Related resources: OWASP Firmware Security Testing Guide
