---
id: 667507ae-8018-46db-a6f4-41a0a953edc4
type: tool
verified: true
created_at: '2019-08-28T21:17:38.700357+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - redteam
  - evasion
  - hta
  - encryption
  - payload-generation
url: 'https://github.com/sensepost/demiguise'
validated: true
---

# demiguise

**Status**: Unverified

## Overview

Demiguise is a Python-based tool designed for red team operations to generate encrypted HTML Applications (HTA) files. It bundles executable payloads into obfuscated HTA formats, helping to evade antivirus detection and facilitate payload delivery in phishing or drive-by download scenarios.

## Description

Demiguise specializes in creating self-decrypting HTA bundles that can embed Windows executables, scripts, or other payloads. By encrypting the content and optionally signing with certificates, it allows red teams to deliver malicious HTA files that appear benign. Commonly used in initial access vectors like spear-phishing attachments or compromised websites, the tool supports custom encryption keys and certificate-based signing to enhance stealth.

## Features

- Feature 1: Payload bundling into encrypted HTA files for AV evasion
- Feature 2: Support for custom encryption keys and certificate signing
- Feature 3: Generation of standalone HTA executables that decrypt and run payloads on Windows targets
- Feature 4: Integration with common red team workflows for payload obfuscation

## Installation

### Requirements

- Python 2.7 or 3.x
- Git for cloning the repository
- OpenSSL for certificate handling (optional)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/sensepost/demiguise.git
cd demiguise

# Install dependencies (if any, typically none beyond Python)
pip install -r requirements.txt  # Usually not needed

# Make executable (on Linux/macOS for development)
chmod +x demiguise.py
```

On Windows, simply run the Python script directly.

## Basic Usage

```bash
tool-name --help
```

Run `python demiguise.py -h` to see all options.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -f | Specify input payload file |
| -o | Specify output HTA file |
| -e | Custom encryption key |
| --cert | Path to signing certificate |
| --pass | Certificate password |

## Examples

### Example 1: Basic Usage

```python
python demiguise.py -f payload.exe -o bundle.hta -e mykey
```

This creates an encrypted HTA from payload.exe.

### Example 2: Advanced Usage

```python
python demiguise.py -f payload.exe -o signed.hta --cert cert.pfx --pass mypass -e strongkey
```

Generates a signed, encrypted HTA for better evasion.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[Regsvr32]] Signed Binary Proxy Execution: HTA

### Tactics

- [[Initial Access]] Initial Access
- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for HTA file creation with embedded executables via file analysis tools like Volatility or Wireshark for unusual network callbacks
- Detection method 2: Endpoint detection rules for PowerShell/HTA execution patterns, encrypted payloads decrypting to EXEs
- Detection method 3: Signature-based AV for known Demiguise-generated artifacts or behavioral alerts on HTA downloads

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/metasploit]]
- [[tools/Empire]]

## References

- Official GitHub: https://github.com/sensepost/demiguise
- SensePost Blog: https://sensepost.com/blog/2017/demiguise-hta-bundling-tool/
- MITRE ATT&CK: https://attack.mitre.org/techniques/T1218/010/
