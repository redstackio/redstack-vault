---
id: f9364494-8f30-435f-9e4b-310972c6d5bb
type: tool
verified: true
created_at: '2019-08-28T21:17:30.664522+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - malware-analysis
  - detection
  - pattern-matching
url: 'https://yara.readthedocs.io/'
commands:
  - '[[commands/yara-compile-rules]]'
  - '[[commands/yara-basic-scan]]'
  - '[[commands/yara-scan-processes]]'
validated: true
---

# Yara

**Status**: Unverified

## Overview

YARA is a tool for identifying and classifying malware samples by creating descriptions (rules) based on textual or binary patterns found in the samples. It is widely used in malware research, incident response, and security operations to detect known malware families or custom indicators of compromise (IoCs). In offensive security contexts, YARA can be used to scan for evasion techniques, verify payload signatures, or analyze captured binaries during post-exploitation.

## Description

YARA rules consist of strings (text or hex patterns) and a boolean expression that defines the matching logic. The tool supports scanning individual files, directories, or running processes. Rules can be compiled for faster execution. YARA is particularly useful for creating lightweight, signature-based detection without relying on full antivirus engines. It integrates well with other tools like Volatility for memory analysis or scripts for automated hunting.

## Features

- **Rule Definition**: Create custom rules with strings, modules (e.g., PE, ELF), and conditions for complex matching.
- **Scanning Modes**: Support for file, directory, and process scanning with recursive options.
- **Compilation**: Compile rules to binary format for performance gains.
- **Output Formats**: JSON, CSV, or plain text for match reporting.
- **Cross-Platform**: Works on Linux, Windows, and macOS with bindings for Python, etc.

## Installation

### Requirements

- Build tools (gcc, make) for compilation from source.
- Python 3+ if using bindings.

### Install Commands

```bash
# Kali Linux (pre-installed in most cases)
sudo apt update && sudo apt install yara

# Ubuntu/Debian
sudo apt update && sudo apt install yara

# macOS (via Homebrew)
brew install yara

# Windows (via Chocolatey)
choco install yara

# From Source (all platforms)
git clone https://github.com/VirusTotal/yara.git
cd yara
./bootstrap.sh
./configure
make
sudo make install
```

## Basic Usage

```bash
yara --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-r` | Recursive scan of directories |
| `-w` | Scan whole files (disable fast mode) |
| `-p <n>` | Scan top n processes |
| `-o <format>` | Output format (json, csv) |
| `-s` | Print matching strings |

## Examples

### Example 1: Basic Usage

Scan a single file with a rule:

```bash
yara rules.yar suspicious.exe
```

### Example 2: Advanced Usage

Compile rules and scan a directory recursively:

```bash
yarac rules.yar compiled.yac
yara -r compiled.yac /path/to/samples/
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Security Software Discovery]] Security Software Discovery (scanning for AV signatures or malware patterns)
- [[Software Discovery]] Software Discovery (analyzing binaries for indicators)

### Tactics

- [[Discovery]] Discovery
- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'yara' or 'yarac' executions.
- File system scans for .yara or .yac files in unusual locations.
- Network activity if YARA rules fetch external modules or data.
- Integration logs in SIEM if used with automated tools like TheHive or MISP.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/volatility]] (memory forensics integration)
- [[tools/Radare2]] (binary analysis companion)

## References

- Official documentation: https://yara.readthedocs.io/
- GitHub Repository: https://github.com/VirusTotal/yara
