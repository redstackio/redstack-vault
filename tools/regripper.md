---
id: 837d921c-c0de-41cb-9d85-bfd0d03f3470
type: tool
verified: true
created_at: '2019-08-28T21:17:39.481617+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - forensics
  - registry
  - analysis
  - incident-response
url: 'https://github.com/keydet89/RegRipper3.0'
commands:
  - '[[commands/rip-parse-all-plugins]]'
  - '[[commands/rip-parse-system-profile]]'
  - '[[commands/rip-run-single-plugin]]'
validated: true
---

# regripper

**Status**: Unverified

## Overview

RegRipper is an open-source Perl-based tool designed for extracting, parsing, and analyzing data from Windows Registry hives. It is primarily used in digital forensics, incident response, and security assessments to uncover system artifacts, user activity, malware persistence, and configuration details. The tool operates via a command-line interface (CLI) called 'rip' or a graphical user interface (GUI), making it accessible for both automated scripting and interactive analysis.

## Description

RegRipper functions as an engine that executes modular plugins—individual Perl scripts that target specific registry keys, values, and data structures. These plugins can enumerate subkeys, extract timestamps, and correlate information relevant to investigations, such as recent file access, network connections, or installed software. The CLI version ('rip') allows for batch processing and integration into scripts, while the GUI provides a user-friendly interface for selecting hives, profiles (collections of plugins), and output files. Plugins promote knowledge sharing among analysts by encapsulating reusable parsing logic, enabling rapid analysis of common forensic artifacts without manual registry navigation.

## Features

- **Modular Plugin System**: Over 400 plugins for parsing various hives (SYSTEM, SOFTWARE, NTUSER.DAT, etc.), covering topics like services, USB history, and event logs.
- **CLI and GUI Support**: Command-line for automation; GUI for interactive selection of hives and profiles.
- **Profile Management**: Predefined profiles (e.g., 'all', 'system') group related plugins for efficient targeted analysis.
- **Output Formatting**: Results are structured for easy reading, with timestamps and data in plain text; supports logging in GUI mode.
- **Extensibility**: Users can create custom plugins to parse novel artifacts or retain organizational knowledge.

## Installation

### Requirements

- Perl 5.10 or later (ActivePerl on Windows, standard Perl on Linux).
- Access to Windows Registry hive files (extracted from disk images or memory dumps using tools like FTK Imager).

### Install Commands

```bash
# Clone the repository (Linux/macOS/Windows with Git)
git clone https://github.com/keydet89/RegRipper3.0.git
cd RegRipper3.0

# On Kali Linux or Ubuntu (Perl is pre-installed)
# No additional packages needed; run directly with perl

# On Windows
# Download ZIP from GitHub, extract, and ensure Perl is in PATH
# Or use: perl rip.pl --help
```

For portable use, download the latest release ZIP from the GitHub repository and extract to a working directory.

## Basic Usage

```bash
perl rip.pl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -r <file> | Specify the registry hive file to parse |
| -p <profile> | Use a specific profile (e.g., 'all', 'system', 'software') |
| -g | Launch the GUI version |
| -d <dir> | Output directory for results |
| --help | Display help and available plugins |

## Examples

### Example 1: Basic Usage

Parse the SYSTEM hive with all plugins and redirect output:

```bash
perl rip.pl -r SYSTEM -p all > system_analysis.txt
```

### Example 2: Advanced Usage

Run a single plugin on a user hive:

```bash
perl rip.pl -r NTUSER.DAT recentdocs
```

Launch GUI for interactive parsing:

```bash
perl rr.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Query Registry]] Query Registry (for extracting persistence, discovery, and defense evasion indicators from registry artifacts)
- [[Credential Dumping]] OS Credential Dumping (plugins can parse credential-related keys like SAM or LSA)

### Tactics

- [[Discovery]] Discovery (uncovering system and user information)
- [[Persistence]] Persistence (identifying registry-based persistence mechanisms)

## Detection

- Monitor for Perl script execution (e.g., process creation of perl.exe or rip.pl) on forensic workstations.
- Network indicators: Downloads from GitHub repository or unusual file extractions in analysis environments.
- File system: Presence of RegRipper directories, .pl files, or output .txt files with parsed registry data.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/volatility]] (memory forensics complementing registry analysis)
- [[tools/Autopsy]] (full digital forensics suite integrating registry parsing)

## References

- Official GitHub: https://github.com/keydet89/RegRipper3.0
- Harlan Carvey's Blog: https://www.windows-ir.com/
- SANS Forensics Resources: https://www.sans.org/tools/regripper/
