---
id: tool-uuid-2
url: 'https://hashcat.net/hashcat/'
name: Hashcat
tags:
  - cracking
  - password
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.050Z'
validated: true
submitted: true
---
# Hashcat

**Status**: Unverified

## Overview

Hashcat is an advanced password recovery utility supporting over 300 hash types, used for offline cracking of captured credentials like NTLMv2 hashes from SMB auth.

## Description

In security testing, Hashcat accelerates cracking with GPU support, essential for processing NTLMv2 hashes obtained via SSRF and SMB listeners to recover domain passwords.

## Features

- Feature 1: Multi-GPU acceleration
- Feature 2: Support for NTLMv1/v2, Kerberos, etc.
- Feature 3: Rule-based and hybrid attacks

## Installation

### Requirements

- OpenCL or CUDA drivers for GPU
- Compatible OS

### Install Commands

```bash
# On Kali Linux
apt install hashcat
```

## Basic Usage

```bash
hashcat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m` | Hash mode |
| `-a` | Attack mode |
| `-O` | Optimized kernels |

## Examples

### Example 1: Basic Usage

```bash
hashcat -m 5600 hashes.txt wordlist.txt
```

### Example 2: Advanced Usage

```bash
hashcat -m 5600 -a 0 hashes.txt rockyou.txt -r rules/best64.rule
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- High GPU utilization during cracking
- Process monitoring for hashcat.exe
- File access to hash dumps and wordlists

## Related Procedures

- [[procedures/Analyze-Captured-NTLMv2-Hashes]]

## Related Tools

- [[John the Ripper]]

## References

- Official site: https://hashcat.net/hashcat/
- Wiki: https://hashcat.net/wiki/
