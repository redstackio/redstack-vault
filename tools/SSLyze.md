---
url: 'https://github.com/iSECPartners/sslyze'
tags:
  - ssl-analysis
  - recon
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:11.022Z'
id: 685c2781-2c95-4dbf-b2de-e9d0000be1da
validated: true
submitted: true
---
# sslyze

**Status**: Unverified

**Status**: Unverified

## Overview

Python tool for analyzing SSL/TLS configs, ciphers, certs, and vulns like Heartbleed.

## Description

Scans SMTP with STARTTLS on apps.owncloud.com:587, confirming anonymous ciphers and self-signed certs.

## Features

- Feature 1: Cipher suite listing
- Feature 2: Cert validation
- Feature 3: Protocol downgrade tests

## Installation

### Requirements

- Python 3+

### Install Commands

```bash
pip install sslyze
```

## Basic Usage

```bash
sslyze --help
```

### Common Options

| Option | Description |
|--------|-------------|
| --regular | Standard scan |
| --starttls | Protocol (smtp) |

## Examples

### Example 1: Basic Usage

```bash
sslyze --regular target:443
```

### Example 2: Advanced Usage

```bash
sslyze --regular target:587 --starttls=smtp
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Multiple TLS connection attempts
- Python process with sslyze args

## Related Procedures

- [[procedures/Analyze-SMTP-Cipher-Suites-with-Sslyze]]

## Related Tools

- [[tools/testssl-sh]]

## References

- GitHub: https://github.com/iSECPartners/sslyze
- Docs: https://sslyze.readthedocs.io
