---
id: 4ac07efe-5aa9-41d5-ad89-cf714ccd43f3
name: edb
type: tool
verified: true
created_at: '2019-08-28T21:17:25.553171+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - debugger
  - reverse-engineering
  - exploit-development
url: 'https://github.com/eteran/edb-debugger'
validated: true
---

# edb

**Status**: Unverified

## Overview

edb is a cross-platform debugger for x86 and x86-64 architectures, serving as a Linux equivalent to the Windows-based OllyDbg. It provides an intuitive GUI for binary analysis, debugging, and reverse engineering tasks commonly used in offensive security operations such as malware analysis, exploit development, and vulnerability research.

## Description

edb offers a plugin-based architecture allowing extensibility through debugging cores, with support for multiple APIs. Key capabilities include step-by-step execution (step-into, step-over, run, break), conditional breakpoints, basic instruction analysis, memory region viewing and dumping, effective address inspection, and tabbed data dump views for quick switching between memory regions. It also supports importing and generating symbol maps, making it suitable for dynamic analysis of executables during red team engagements or custom payload development.

## Features

- **Intuitive GUI Interface**: User-friendly layout similar to OllyDbg for efficient debugging sessions.
- **Standard Debugging Operations**: Supports step-into, step-over, run, and break functionalities.
- **Conditional Breakpoints**: Set breakpoints based on conditions for targeted analysis.
- **Plugin-Based Core**: Modular design allows replacement of debugging backends (e.g., ptrace, GDB integration).
- **Instruction and Memory Analysis**: Disassemble code, inspect registers, and dump memory regions.
- **Symbol Map Support**: Import/export symbols for stripped binaries.
- **Tabbed Memory Views**: Multiple simultaneous views of memory for complex analysis.

## Installation

### Requirements

- Linux distribution with x86/x86-64 support (e.g., Ubuntu, Kali Linux).
- Dependencies: Qt5 libraries, Python 3 for plugins, GDB (optional for integration).

### Install Commands

```bash
# On Ubuntu/Debian/Kali
sudo apt update
sudo apt install edb-debugger

# Or build from source
sudo apt install qt5-default libqt5xmlpatterns5-dev libboost-all-dev
git clone https://github.com/eteran/edb-debugger.git
cd edb-debugger
qmake
make
sudo make install
```

## Basic Usage

```bash
edb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `-v, --version` | Display version information |
| `--create-plugin-cache` | Generate plugin cache for faster loading |
| `--clear-plugins` | Clear loaded plugins |
| `--gdb-path PATH` | Specify path to GDB binary for integration |
| `--project PATH` | Load a saved project file |

## Examples

### Example 1: Basic Usage

Launch edb to debug a binary file:

```bash
edb /path/to/target_binary
```

This opens the GUI with the binary loaded for analysis.

### Example 2: Advanced Usage

Clear plugins and launch with GDB integration:

```bash
edb --clear-plugins --gdb-path /usr/bin/gdb /path/to/target_binary
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1587.001]] Develop Capabilities: Malware
- [[SAML Tokens]] Forge Web Credentials: Software

### Tactics

- [[Reconnaissance]] Resource Development

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'edb' executable running on analysis machines.
- Network logs showing no outbound connections (GUI-based, local tool).
- File system artifacts: edb project files (.edb) or plugin caches in user directories.
- Host-based forensics: Memory dumps or process lists during debugging sessions.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Ghidra]]
- [[tools/IDA-Pro]]
- [[tools/GDB]]

## References

- Official GitHub: https://github.com/eteran/edb-debugger
- Documentation: Included in source or via `edb --help`
