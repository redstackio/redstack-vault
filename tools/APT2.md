---
id: cdae333c-a71e-4378-99fd-85664a17d533
type: tool
verified: true
created_at: '2019-08-28T21:17:26.444901+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - penetration-testing
  - automation
  - scanning
  - exploitation
url: 'https://github.com/mgeeky/APT2'
commands:
  - '[[commands/apt2-run-nmap-scan]]'
  - '[[commands/apt2-import-nessus]]'
  - '[[commands/apt2-import-nexpose]]'
  - '[[commands/apt2-start-interface]]'
validated: true
---

# APT2

**Status**: Unverified

## Overview

APT2 is an Automated Penetration Testing Toolkit designed to streamline security assessments by integrating scanning, enumeration, and exploitation capabilities. It performs NMap scans or imports results from tools like Nexpose, Nessus, or existing NMap XML files, then automatically launches relevant exploit and enumeration modules based on discovered services and a configurable safety level. All results are stored in a local Knowledge Base (KB) for review and analysis within the tool's interface.

Common use cases include initial reconnaissance in red team engagements, automated vulnerability scanning for pentesting, and building a centralized repository of assessment findings.

## Description

APT2 automates the penetration testing workflow by processing scan data to identify potential attack vectors and executing modular exploits/enumerations accordingly. The tool supports a 'Safe Level' configuration to control the aggressiveness of automated actions, preventing unintended impacts on production environments. The Knowledge Base serves as a SQLite-backed repository where module outputs are harvested, allowing users to query and visualize results through the tool's GUI or CLI interface. It is particularly useful for lone pentesters or teams needing to scale manual efforts with automation while maintaining traceability.

## Features

- **Scan Integration**: Native NMap scanning or import from Nexpose, Nessus, and NMap XML.
- **Modular Execution**: Launches exploits and enumerations tailored to discovered services (e.g., SMB, HTTP, RDP).
- **Safety Controls**: Configurable safe levels to limit destructive actions.
- **Knowledge Base**: SQLite database for storing and querying results from all modules.
- **User Interface**: GUI for interactive review and CLI for scripted use.
- **Extensibility**: Python-based modules for custom exploits and enumerations.

## Installation

### Requirements

- Python 2.7 or 3.x (tool is compatible with both, but Python 3 recommended).
- Git for cloning the repository.
- Dependencies: NMap, and optionally Nessus/Nexpose for imports.
- SQLite for the Knowledge Base (included with Python).

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mgeeky/APT2.git
cd APT2

# Install Python dependencies (if any; APT2 is mostly self-contained)
pip install -r requirements.txt  # If requirements.txt exists; otherwise, none needed

# Make executable (if needed)
chmod +x apt2.py
```

On Kali Linux, APT2 may be available via apt, but building from source is recommended for the latest features.

## Basic Usage

```bash
python apt2.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and usage. |
| `--nmap` | Perform an NMap scan on the target. |
| `--nessus` | Import Nessus XML scan results. |
| `--nexpose` | Import Nexpose XML scan results. |
| `--safe-level` | Set safety level (1-5, default 3). |
| `--kb` | Specify Knowledge Base path. |
| `--gui` | Launch the graphical interface. |

## Examples

### Example 1: Basic Usage

Run APT2 with an NMap scan on a target and auto-launch modules:

```bash
python apt2.py --nmap 192.168.1.100 --safe-level 2
```

This scans the target, processes results, and executes low-risk enumerations/exploits, storing output in the KB.

### Example 2: Advanced Usage

Import Nessus results and review in GUI:

```bash
python apt2.py --nessus scan_results.xml --gui
```

This imports the XML, runs modules, and opens the interface for KB browsing. See [[commands/apt2-import-nessus]] for details.

### Example 3: NMap XML Import

```bash
python apt2.py --nmap-xml previous_scan.xml --safe-level 4
```

Processes an existing NMap XML and launches higher-risk modules.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic patterns from NMap scans or module executions (e.g., multiple port probes).
- File system artifacts: Presence of APT2 directory, apt2.py process, or SQLite KB files.
- Process monitoring: Python processes spawning NMap or exploit tools.
- Log analysis: Unusual XML imports or automated enumeration attempts.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for scanning integration)
- [[Nessus]] (for XML imports)
- [[Metasploit]] (similar modular exploitation)

## References

- Official GitHub: https://github.com/mgeeky/APT2
- Documentation: Included in repo README
- Related: Penetration testing automation frameworks like AutoRecon or Pacific
