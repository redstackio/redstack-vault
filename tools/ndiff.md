---
id: 102f319f-733b-4b7a-8894-023a99fb061e
type: tool
verified: true
created_at: '2019-08-28T21:17:40.391220+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reconnaissance
  - comparison
  - nmap
url: 'https://nmap.org/ndiff/'
validated: true
---

# ndiff

**Status**: Unverified

## Overview

Ndiff is a utility included in the Nmap suite for comparing the results of two Nmap scans. It highlights differences in hosts, ports, services, and other scan data, making it essential for tracking network changes, monitoring security posture, or analyzing scan evolution over time. Commonly used in penetration testing to identify new vulnerabilities or configuration drifts.

## Description

Ndiff processes Nmap's XML output files and generates human-readable or machine-parseable reports of differences. It supports normal, XML, and grepable output formats. Key capabilities include detecting added/removed hosts, port state changes (open to closed), service version updates, and OS fingerprint alterations. Ndiff is lightweight, fast, and integrates seamlessly with automated scanning workflows. It runs on all platforms supported by Nmap and requires no additional dependencies beyond the Nmap installation.

## Features

- **Difference Highlighting**: Uses + for additions, - for removals, and detailed explanations for changes.
- **Multiple Output Formats**: Normal text (-oN), XML (-oX), or grepable (-oG) for integration with other tools.
- **Verbose Mode**: Provides in-depth analysis of why differences occurred.
- **Flexible Input**: Handles large XML files from comprehensive Nmap scans efficiently.
- **Scriptable**: Easily automated in scripts for periodic network monitoring.

## Installation

### Requirements

- Nmap version 6.40 or later (Ndiff is bundled with Nmap).
- Perl (for some advanced features, though core functionality is in C).

### Install Commands

```bash
# On Kali Linux (pre-installed with Nmap)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install nmap

# On macOS with Homebrew
brew install nmap

# On Windows
# Download from https://nmap.org/download.html and install the MSI package
# Ndiff is included in the installer

# Verify installation
ndiff --version
```

## Basic Usage

```bash
ndiff --help
```

Displays help with all options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and exit |
| -v | Verbose output with detailed change explanations |
| -oN <file> | Output differences in normal format to file |
| -oX <file> | Output in XML format for further processing |
| --all | Show all hosts, even those unchanged |

## Examples

### Example 1: Basic Usage

```bash
ndiff scan1.xml scan2.xml
```

Compares two scans and prints differences to stdout.

### Example 2: Advanced Usage

```bash
ndiff -v -oN changes.txt initial-scan.xml follow-up-scan.xml
```

Runs a verbose comparison and saves results to changes.txt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of ndiff executable or process (ndiff.exe on Windows).
- File system artifacts: Temporary XML diff files or logs referencing ndiff.
- Network logs showing repeated Nmap scans followed by comparison activity.
- Command-line auditing: Searches for 'ndiff' in process execution logs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (parent tool for generating scan inputs)
- [[Zenmap]] (GUI for Nmap, can export to XML for Ndiff)

## References

- Official Nmap Documentation: https://nmap.org/book/ndiff.html
- Nmap Project: https://nmap.org
