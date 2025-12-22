---
id: 6662db65-6346-4b31-9fb2-b4ab3ba8f66e
type: tool
verified: true
created_at: '2019-08-28T21:17:32.018608+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - memory-forensics
  - dfir
  - volatility
  - incident-response
url: 'https://github.com/volatilityfoundation/volatility'
commands:
  - '[[commands/volatility-imageinfo]]'
  - '[[commands/volatility-pslist]]'
  - '[[commands/volatility-pstree]]'
  - '[[commands/volatility-dlllist]]'
validated: true
---

# Volatility

**Status**: Unverified

## Overview

Volatility is an open-source memory forensics framework written in Python. It extracts digital artifacts from volatile memory (RAM) dumps, providing visibility into the runtime state of systems independent of the live environment. Commonly used in digital forensics and incident response (DFIR) for analyzing malware, rootkits, and system compromises.

## Description

The Volatility Framework supports memory dumps from major 32- and 64-bit Windows versions (XP through Windows 8/8.1/Server 2012), Linux kernels (2.6.x to 4.x), macOS (10.5 to 10.9), and Android. It handles formats like raw dumps, crash dumps, hibernation files, and VM snapshots. Plugins enable analysis of processes, network connections, registry, files, and more, aiding in threat hunting and forensic investigations.

## Features

- Feature 1: Profile-based analysis for OS-specific structures
- Feature 2: 100+ plugins for artifacts like processes, modules, handles, and hooks
- Feature 3: Cross-platform support for Windows, Linux, macOS memory samples
- Feature 4: Extensible Python architecture for custom plugins

## Installation

### Requirements

- Python 2.7 (for Volatility 2.x)
- Git for cloning the repository
- Supported platforms: Linux (Kali/Ubuntu recommended), Windows, macOS

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install -y python2.7 git

git clone https://github.com/volatilityfoundation/volatility.git
cd volatility

# No further installation needed; run with python vol.py
```

For Volatility 3 (modern version):

```bash
pip install volatility3
```

## Basic Usage

```python
python vol.py --info
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help for plugins |
| --info | List available profiles and plugins |
| -f, --file | Specify memory dump file |
| --profile | Select OS profile for analysis |
| -v | Verbose output |

## Examples

### Example 1: Basic Usage

```python
python vol.py -f memory.dmp imageinfo
```

### Example 2: Advanced Usage

```python
python vol.py -f memory.dmp --profile=Win7SP1x64 pslist | grep suspicious
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Process Discovery]] Process Discovery (via pslist/pstree)
- [[Software Discovery]] Software Discovery (via modules/dlllist)
- [[Network Sniffing]] Network Sniffing (via netscan)

### Tactics

- [[Discovery]] Discovery
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for python vol.py executions in forensics tools on analyst machines
- Detection method 2: Unusual file access to memory dumps (.dmp, .raw) by Python processes
- Detection method 3: Network downloads of volatility.git repository

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Reckoner]]
- [[tools/Autopsy]]

## References

- Official GitHub: https://github.com/volatilityfoundation/volatility
- Documentation: https://volatility3.readthedocs.io/
- Volatility 2 Wiki: https://github.com/volatilityfoundation/volatility/wiki
