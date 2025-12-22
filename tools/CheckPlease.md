---
id: dfdd1ecd-cc16-4dcd-9bfe-890f598561aa
name: CheckPlease
type: tool
verified: true
created_at: '2019-08-28T21:17:35.212531+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - evasion
  - sandbox
  - redteam
  - payload-generation
url: 'https://github.com/zerosum0x00/CheckPlease'
validated: true
---

# CheckPlease

**Status**: Unverified

## Overview

CheckPlease is an open-source framework for generating sandbox evasion modules and payloads in multiple programming languages, including PowerShell, Python, Go, Ruby, C, C#, Perl, and Rust. It is designed for red team operations and malware development to detect and bypass virtualized analysis environments by checking for common sandbox indicators such as timing anomalies, VM artifacts, and hardware fingerprints.

## Description

CheckPlease provides modular evasion techniques that can be integrated into larger payloads or used standalone. It supports cross-platform generation, making it versatile for targeting Windows, Linux, and macOS environments. Common use cases include embedding evasion checks in initial payload stages to avoid detonation in automated sandboxes during penetration testing or adversary emulation.

## Features

- Feature 1: Multi-language support for generating evasion code (PowerShell, Python, Go, etc.)
- Feature 2: Various detection techniques including VM registry/process checks, timing-based evasion, and file artifact scanning
- Feature 3: Customizable output with placeholders for integrating actual malicious code
- Feature 4: Command-line interface for easy payload generation and module listing

## Installation

### Requirements

- PowerShell 5.0+ for Windows (or Python 3.x for cross-platform scripting)
- Git for cloning the repository
- Supported languages' runtimes (e.g., Python, Go compiler)

### Install Commands

```bash
# Clone the repository (Kali/Ubuntu)
git clone https://github.com/zerosum0x00/CheckPlease.git
cd CheckPlease

# For PowerShell usage on Windows
Import-Module .\CheckPlease.psm1

# For Python-based generation
pip install -r requirements.txt  # If applicable for extensions
```

## Basic Usage

```powershell
Get-Help New-CheckPleasePayload
```

### Common Options

| Option | Description |
|--------|-------------|
| -Language | Specify output language (e.g., PowerShell, Python) |
| -Technique | Choose evasion method (e.g., VMArtifactCheck) |
| -OutputPath | File path for generated payload |
| -Help | Show usage information |

## Examples

### Example 1: Basic Usage

```powershell
New-CheckPleasePayload -Language PowerShell -Technique VMArtifactCheck -OutputPath evasion.ps1
```

### Example 2: Advanced Usage

```python
python checkplease.py --language Go --technique TimingDelay --output evasion.go
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Virtualization-Sandbox Evasion]] Virtualization/Sandbox Evasion
- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Presence of generated scripts with characteristic CheckPlease comments or patterns (e.g., VM process checks)
- Detection method 2: Anomalous PowerShell/Python executions querying VM artifacts (e.g., via Sysmon logging)
- Detection method 3: Network fetches from GitHub repository during installation

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerShell Empire]]
- [[tools/Covenant]]

## References

- Official GitHub: https://github.com/zerosum0x00/CheckPlease
- Related resources: MITRE ATT&CK T1497 documentation
