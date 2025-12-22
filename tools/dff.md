---
id: e4761d2a-4857-448c-aff8-81ee966c79c4
type: tool
verified: true
created_at: '2019-08-28T21:17:38.234838+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - forensics
  - digital-forensics
  - evidence-collection
  - chain-of-custody
url: 'https://github.com/dfir-framework/dff'
validated: true
---

# dff

**Status**: Unverified

## Overview

DFF (Digital Forensics Framework) is a free and open-source computer forensics software built on a dedicated Application Programming Interface (API). It enables both professionals and non-experts to quickly collect, preserve, and reveal digital evidence without compromising systems or data. Primarily used in incident response, investigations, and security analysis to maintain integrity of evidence.

Category: Forensics

## Description

DFF provides a modular framework for digital forensics tasks, supporting access to various file systems, recovery of artifacts, and preservation of chain of custody. It is particularly useful for analyzing disk images, memory dumps, and remote systems in a forensically sound manner. The tool supports both GUI and API-driven workflows, making it versatile for automated scripting or interactive analysis in security operations.

## Features

- **Preserve digital chain of custody**: Includes software write blockers and cryptographic hash calculations to ensure evidence integrity.
- **Access to local and remote devices**: Supports disk drives, removable devices, and remote file systems.
- **Read standard digital forensics file formats**: Compatible with Raw, EnCase EWF, and AFF 3 formats.
- **Virtual machine disk reconstruction**: Handles VmWare (VMDK) files.
- **Windows and Linux OS forensics**: Analyzes registry, mailboxes, NTFS, EXTFS 2/3/4, and FAT 12/16/32 file systems.
- **Quickly triage and search for (meta-)data**: Uses regular expressions, dictionaries, content search, tags, and timelines.
- **Recover hidden and deleted artifacts**: Recovers deleted files/folders, unallocated spaces, and performs carving.
- **Volatile memory forensics**: Extracts processes, local files, binary data, and network connections from memory dumps.

## Installation

### Requirements

- Python 2.7 or 3.x (depending on version)
- Dependencies: PyQt4/PyQt5 for GUI, various forensics libraries (e.g., libewf, libaff)
- Supported on Linux and Windows

### Install Commands

For Ubuntu/Kali Linux (from source, as not typically in default repos):

```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip git build-essential libewf-dev libafflib-dev

# Clone the repository
git clone https://github.com/dfir-framework/dff.git
cd dff

# Install Python dependencies
pip3 install -r requirements.txt

# Build and install
python3 setup.py build
sudo python3 setup.py install
```

For Windows: Download pre-built binaries from the official GitHub releases or use a package manager like Chocolatey if available.

Note: Building from source is recommended for the latest features. Refer to the GitHub README for platform-specific instructions.

## Basic Usage

```bash
dff --help
```

Displays help and available options.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-m, --module` | Specify a module to load (e.g., vfs, hash) |
| `-f, --file` | Path to the evidence file or image to analyze |
| `--gui` | Launch the graphical user interface (default on most platforms) |

## Examples

### Example 1: Basic Usage

```bash
dff
```

Launches the DFF GUI for interactive forensics analysis.

### Example 2: Advanced Usage

```bash
dff -m hash -f /path/to/evidence.img
```

Runs the hash module on a disk image to compute cryptographic hashes for chain of custody.

## MITRE ATT&CK Mapping

This tool is commonly associated with defensive and investigative activities, but in red team contexts, it may support post-exploitation evidence gathering:

### Techniques

- [[Data from Local System]] Data from Local System
- [[Network Sniffing]] Network Sniffing (for network artifact analysis)

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control (for remote evidence collection)

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of 'dff' or 'dff.exe' process in task lists or memory.
- Network connections or file accesses related to evidence mounting (e.g., write-blocker emulation).
- Log entries for hash computations or file system mounts in forensic modes.
- Installation artifacts in /opt/dff or Python site-packages.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/volatility]] (for advanced memory forensics)
- [[tools/autopsy]] (GUI-based forensics suite)

## References

- Official GitHub: https://github.com/dfir-framework/dff
- Documentation: http://wiki.digital-forensics-framework.org/
- Related resources: NIST Guidelines on Digital Evidence Preservation
