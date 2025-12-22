---
id: 99ce93d1-3b94-4878-8817-f3e0114b1769
name: Composite-Moniker
type: tool
verified: true
created_at: '2019-08-28T21:17:24.433277+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - exploitation
  - rce
  - cve-2017-8570
  - office
url: 'https://github.com/rapid7/metasploit-framework/pull/8450'
validated: true
---

# Composite-Moniker

**Status**: Unverified

## Overview

Composite Moniker is a proof-of-concept (PoC) exploit tool for CVE-2017-8570, a remote code execution vulnerability in Microsoft Office. It generates malicious RTF documents that leverage improper handling of composite monikers in OLE objects to execute arbitrary code when opened in vulnerable versions of Microsoft Word or other Office applications. This tool is useful in red team engagements for demonstrating client-side attacks via phishing or file delivery vectors.

## Description

CVE-2017-8570 affects Microsoft Office 2007, 2010, 2013, and 2016 by allowing attackers to embed malicious OLE objects in RTF files. The composite moniker technique bypasses certain security features, leading to RCE without user interaction beyond opening the file. The tool automates the creation of such files, embedding custom payloads like shellcode or commands. It is typically implemented as a Python script and requires no compilation.

## Features

- Feature 1: Generates RTF files with embedded composite moniker payloads for CVE-2017-8570 exploitation.
- Feature 2: Supports custom payload injection, including shellcode or executable commands.
- Feature 3: Compatible with Metasploit integration for payload generation and delivery.

## Installation

### Requirements

- Python 2.7 or 3.x
- Required libraries: None (standalone script)
- Target: Vulnerable Microsoft Office installations (pre-2016 patches)

### Install Commands

```bash
# Clone the PoC repository (example from public sources)
git clone https://github.com/rapid7/metasploit-framework.git
cd metasploit-framework
# Or download standalone PoC script
wget https://example-poc-site/composite_moniker.py
```

For Kali Linux:

```bash
# Metasploit is pre-installed on Kali
msfupdate
```

## Basic Usage

```bash
tool-name --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -o, --output | Specify output RTF file |
| -p, --payload | Custom payload to embed |

## Examples

### Example 1: Basic Usage

```python
python composite_moniker.py --output exploit.rtf
```

Generates a default malicious RTF file.

### Example 2: Advanced Usage

```python
python composite_moniker.py --output exploit.rtf --payload "calc.exe"
```

Embeds a command to launch calculator as the payload.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Phishing]] Phishing

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for RTF files with embedded OLE objects using tools like olevba or rtfdump.
- Detection method 2: Office telemetry logs showing unexpected moniker parsing errors or code execution from documents.
- Detection method 3: Antivirus signatures for known PoC patterns in generated RTF files.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit]]
- [[tools/Office-Exploit-Tools]]

## References

- Official CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-8570
- Microsoft Security Bulletin: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2017-8570
- PoC Source: Various GitHub repositories and Metasploit modules
