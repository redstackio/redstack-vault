---
id: tool-hashcat
url: 'https://hashcat.net/hashcat/'
tags:
  - cracking
  - brute-force
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:42.721Z'
validated: true
submitted: true
---
# Hashcat

**Status**: Unverified

## Overview

Hashcat is an advanced password recovery tool used for offline cracking of hashes, ideal for exploiting weak entropy in generated passwords like those in Rocket.Chat's E2EE implementation.

## Description

Hashcat supports over 300 hash types, including PBKDF2 used in mobile app encryption, with GPU acceleration for high-speed brute-force, dictionary, and mask attacks. In offensive security, it's used to test password strength and recover credentials from extracted data, particularly effective against biased generation reducing search space.

## Features

- Feature 1: Multi-GPU support for parallel cracking
- Feature 2: Custom masks and rules for optimized attacks on known biases
- Feature 3: Benchmarking to estimate crack time

## Installation

### Requirements

- NVIDIA/AMD GPU with CUDA/ROCm drivers
- Compatible OS (Linux preferred for performance)

### Install Commands

```bash
# On Ubuntu/Debian
git clone https://github.com/hashcat/hashcat.git
cd hashcat
make
sudo make install
```

## Basic Usage

```bash
hashcat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m` | Specify hash mode |
| `-a` | Attack mode (0=dict, 3=mask) |
| `-w` | Workload profile (3=high) |

## Examples

### Example 1: Basic Usage

```bash
hashcat -m 0 example.md5 wordlist.txt
```

### Example 2: Advanced Usage

```bash
hashcat -m 1000 -a 3 hash.txt mask.hcmask -O
```

(Uses pre-defined mask file for efficiency.)

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High GPU utilization during cracking sessions
- Process monitoring for hashcat.exe on endpoints
- Network logs if rules/wordlists are downloaded

## Related Procedures

- [[procedures/Brute-Force-E2EE-Password]]

## Related Tools

- [[John the Ripper]]
- [[Hydra]]

## References

- Official documentation: https://hashcat.net/wiki/
- Related resources: OWASP Password Storage Cheat Sheet
