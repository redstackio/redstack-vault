---
id: 2c24f794-5df3-472c-a45f-7e684a0e02e6
type: tool
verified: true
created_at: '2019-08-28T21:17:23.408410+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - defense-evasion
  - code-signing
  - pe-manipulation
url: 'https://github.com/secrary/SigThief'
validated: true
---

# SigThief

**Status**: Unverified

## Overview

SigThief is a Python-based tool designed for stealing digital signatures from signed Portable Executable (PE) files and applying them to unsigned binaries. It is commonly used in red team operations to subvert code signing checks, allowing malicious executables to appear as legitimate signed software and potentially bypass antivirus or endpoint detection solutions that rely on signature validation.

## Description

The tool operates in two main phases: extraction and application. In extraction, it parses a signed PE file to isolate the digital certificate and signature data. In application, it embeds this stolen signature into an unsigned PE, modifying the file's structure to mimic a properly signed binary. This technique exploits trust in code signing to evade defenses, though it may not fool advanced validation like timestamp checks or certificate revocation lists. SigThief is particularly useful against Windows environments where signed executables are whitelisted or trusted by default.

## Features

- Feature 1: Extracts complete digital signatures including certificates and PKCS#7 structures from signed PE files.
- Feature 2: Applies stolen signatures to unsigned PE binaries without requiring compilation or external signing tools.
- Feature 3: Supports common PE formats used in Windows executables (.exe, .dll).
- Feature 4: Lightweight Python implementation with minimal dependencies.

## Installation

### Requirements

- Python 3.6+
- pip for dependency installation
- Access to signed and unsigned PE files for testing

### Install Commands

```bash
# Clone the repository
git clone https://github.com/secrary/SigThief.git
cd SigThief

# Install dependencies
pip3 install -r requirements.txt
```

On Kali Linux or Ubuntu, ensure Python3 and git are installed:
```bash
sudo apt update && sudo apt install python3 python3-pip git
```

## Basic Usage

```bash
python3 sigthief.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -o | Specify output file for extracted/applied signature |
| -i | Input signature file for application |

## Examples

### Example 1: Basic Usage - Extract Signature

Extract a signature from a legitimate signed executable:
```bash
python3 sigthief.py signed_app.exe -o stolen.sig
```

### Example 2: Advanced Usage - Apply Signature

Apply the stolen signature to an unsigned payload:
```bash
python3 sigthief.py malware.exe -i stolen.sig -o signed_malware.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Code Signing]] Code Signing

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for Python processes accessing PE file structures (e.g., via Sysmon Event ID 1 with ImageLoaded for python.exe and file modifications).
- Detection method 2: Check for mismatched signatures in executables using tools like sigcheck or SigVerif, where certificate details don't align with the binary's hash.
- Detection method 3: Behavioral analytics for unsigned binaries suddenly appearing signed, or anomalies in certificate timestamps/issuers.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Pe-Sieve]]
- [[tools/Donut]]

## References

- Official GitHub Repository: https://github.com/secrary/SigThief
- Related resources: MITRE ATT&CK Technique T1553.002 documentation
