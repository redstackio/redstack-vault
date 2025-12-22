---
id: 9c23f775-7058-443d-b942-c8d6ccb6ec61
type: tool
verified: true
created_at: '2019-08-28T21:17:43.147413+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - forensics
  - digital-evidence
  - gui
  - chain-of-custody
url: 'https://github.com/dfir-framework/dff'
validated: true
---

# dff-gui

**Status**: Unverified

## Overview

DFF-GUI is the graphical user interface component of the Digital Forensics Framework (DFF), an open-source tool designed for computer forensics investigations. It enables both professionals and non-experts to collect, preserve, and analyze digital evidence from various sources without compromising the integrity of the data. Commonly used in incident response, evidence acquisition, and forensic triage during security assessments or investigations.

## Description

Built on a modular API, DFF-GUI provides a user-friendly interface for accessing local and remote devices, processing standard forensic file formats, and performing OS-specific analysis on Windows and Linux systems. It supports features like write-blocking for chain of custody preservation, carving for deleted artifacts, and timeline-based searches, making it suitable for red team evidence handling or blue team investigations in offensive security contexts.

## Features

- **Preserve Digital Chain of Custody**: Built-in write blocker and cryptographic hash calculation to ensure evidence integrity.
- **Access to Local and Remote Devices**: Supports disk drives, removable media, and remote file systems.
- **Read Standard Digital Forensics File Formats**: Compatible with Raw, EnCase EWF, AFF 3, and VmWare VMDK formats.
- **Windows and Linux OS Forensics**: Analysis of registry, mailboxes, NTFS, EXT2/3/4, and FAT file systems.
- **Quick Triage and Search**: Regular expressions, dictionaries, content search, tags, and timeline views for metadata and data discovery.
- **Recover Hidden and Deleted Artifacts**: Carving from unallocated spaces, recovery of deleted files/folders.
- **Volatile Memory Forensics**: Extraction of processes, local files, binaries, and network connections from memory dumps.

## Installation

### Requirements

- Python 2.7 or 3.x (depending on version)
- Qt libraries for GUI (PyQt4 or PySide)
- Dependencies: libewf, afflib, sleuthkit (for advanced features)

### Install Commands

For Ubuntu/Kali Linux (build from source, as it's not in standard repos):

```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip libqt4-dev libewf-dev libafflib-dev sleuthkit

# Clone and install DFF
git clone https://github.com/dfir-framework/dff.git
cd dff
python3 setup.py install

# For GUI specifically, ensure PyQt is installed
pip3 install PyQt5
```

For Windows: Download pre-built binaries from the official GitHub releases or use a package manager like Chocolatey if available.

For macOS: Use Homebrew to install dependencies, then build from source similar to Linux.

## Basic Usage

```bash
dff-gui
```

This launches the GUI. Use the interface to create a new case, load evidence files, and select analysis modules.

### Common Options

| Option | Description |
|--------|-------------|
| --load <file> | Automatically load an evidence file on startup |
| --workspace <path> | Specify a workspace directory for the analysis session |
| -h, --help | Show help message and available flags |

## Examples

### Example 1: Basic Usage

```bash
dff-gui
```

Opens the GUI; select "New Case" and load a disk image via File > Open Evidence.

### Example 2: Advanced Usage

```bash
dff-gui --load /evidence/disk.dd --workspace /cases/my_investigation
```

Launches with the disk image loaded and sets the workspace for organized analysis.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Network Sniffing]] Network Sniffing (for network connection analysis in memory forensics)
- [[Data from Local System]] Data from Local System (for file system and artifact recovery)

### Tactics

- [[Discovery]] Discovery (evidence collection and triage)
- [[Command and Control]] Command and Control (remote device access analysis)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring: Look for dff-gui.exe or python processes with DFF modules loaded.
- File system changes: Creation of .dff workspace files or hash logs in temporary directories.
- Network activity: Connections to remote file systems if enabled.
- Registry/Artifact: Installation logs or recent executions in event logs.

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
- [[tools/sleuthkit]] (command-line companion for file system analysis)

## References

- Official GitHub: https://github.com/dfir-framework/dff
- Documentation: https://wiki.digitalforensicframework.org/
- Related resources: SANS Forensics resources on open-source tools
