---
url: 'https://github.com/unoconv/unoconv'
tags:
  - conversion
  - libreoffice
  - vulnerable
type: tool
platforms:
  - Linux
  - Cloud (AWS)
description: >-
  Command-line tool for converting between document formats using LibreOffice,
  vulnerable to crafted file exploits leading to LFI.
id: c8f798c7-14b1-4660-a2bc-70ceda9f84b8
created_at: '2025-12-14T03:46:14.524Z'
updated_at: '2025-12-14T03:46:14.524Z'
verified: false
validated: true
submitted: true
---
# unoconv

**Status**: Unverified

## Overview

unoconv is a command-line utility that leverages LibreOffice to convert documents between formats like DOCX to PDF. In offensive security, it is notable for vulnerabilities when processing malicious inputs, as seen in CVE-2019-17400, enabling LFI in integrated systems like Slack's preview generation.

## Description

It acts as a wrapper around LibreOffice's UNO API for batch conversions, commonly used in server environments. The tool's lack of robust input validation allows exploits via specially crafted Office files to access local resources during conversion, exposing credentials in cloud setups.

## Features

- Feature 1: Supports multiple input/output formats
- Feature 2: Headless operation for automation
- Feature 3: Listener mode for network-based conversions

## Installation

### Requirements

- LibreOffice installed
- Python 2/3 environment

### Install Commands

```bash
# Install via pip (legacy Python 2)
pip install unoconv
# Or from source
git clone https://github.com/unoconv/unoconv.git
cd unoconv
sudo python setup.py install
```

## Basic Usage

```bash
unoconv -f pdf input.docx
```

### Common Options

| Option | Description |
|--------|-------------|
| `-f, --format` | Output format (e.g., pdf, png) |
| `-d, --debug` | Enable debug output |
| `-l, --listen` | Start listener mode |

## Examples

### Example 1: Basic Usage

```bash
unoconv -f png malicious.docx
```

### Example 2: Advanced Usage

```bash
unoconv -f thumbnail -d input.xlsx
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1203.001]]
- [[File and Directory Discovery]]

### Tactics

- [[Execution]]
- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for unoconv invocations with Office inputs
- Anomaly detection in conversion logs for LFI attempts
- File integrity checks on processed documents

## Related Procedures


## Related Tools

- [[tools/LibreOffice]]

## References

- Official documentation: https://github.com/unoconv/unoconv
- Related CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-17400
