---
id: tool-uuid-2
url: 'https://hashcat.net/hashcat/'
tags:
  - cracking
  - credential-access
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.965Z'
validated: true
submitted: true
---
# GPU-Hash-Cracking-Tool

**Status**: Unverified

## Overview

GPU-accelerated tool like Hashcat for offline cracking of password hashes extracted from VPN files, targeting admin credentials.

## Description

Utilizes GPU for high-speed brute-force or dictionary attacks on hashes (e.g., MD5, SHA). In this context, cracks admin hashes from Pulse Secure configs to enable post-auth access.

## Features

- Feature 1: Supports multiple hash types
- Feature 2: GPU optimization for speed
- Feature 3: Mask attacks and rules

## Installation

### Requirements

- NVIDIA/AMD GPU with drivers
- CUDA or OpenCL

### Install Commands

```bash
# For Hashcat
wget https://hashcat.net/files/hashcat-6.2.6.7z
7z x hashcat-6.2.6.7z
```

## Basic Usage

```bash
./hashcat -m 0 -a 0 hash.txt wordlist.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m` | Hash mode (e.g., 0 for MD5) |
| `-a` | Attack mode (0=dictionary) |
| `--force` | Ignore warnings |

## Examples

### Example 1: Basic Usage

```bash
./hashcat -m 0 admin_hash.txt rockyou.txt
```

### Example 2: Advanced Usage

```bash
./hashcat -m 0 -a 3 admin_hash.txt ?a?a?a?a?a?a
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High GPU utilization on attacker machines
- No direct network indicators (offline)

## Related Procedures


## Related Tools

- [[tools/download-py]]

## References

- Hashcat documentation: https://hashcat.net/wiki/
