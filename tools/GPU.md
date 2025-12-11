---
url: null
tags:
  - hash-cracking
  - brute-force
type: tool
platforms:
  - Linux
  - Windows
description: >-
  Graphics Processing Unit used for accelerating password hash cracking
  operations.
id: f0f3a5f3-20ba-4c30-96c4-bcc08f246706
created_at: '2025-12-11T06:10:40.254Z'
updated_at: '2025-12-11T06:10:40.254Z'
verified: false
validated: true
submitted: true
---
# GPU

**Status**: Unverified

## Overview

GPUs are hardware accelerators used in security testing for high-speed computation tasks like cracking password hashes, leveraging parallel processing.

## Description

In offensive security, GPUs are paired with software like hashcat to crack hashes efficiently, far faster than CPU-based methods.

## Features

- Parallel processing for brute-force attacks
- Support for various hash types
- Integration with cracking frameworks

## Installation

### Requirements

- Compatible GPU hardware (e.g., NVIDIA)
- Drivers and CUDA/OpenCL

### Install Commands

```bash
# Install hashcat for GPU usage
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

## Examples

### Example 1: Basic Usage

```bash
hashcat -m 0 -a 0 hash.txt wordlist.txt
```

### Example 2: Advanced Usage

```bash
hashcat -m 1000 -a 3 hash.txt ?a?a?a?a?a?a --force
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- High GPU utilization in logs
- Presence of cracking software

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[hashcat]]
- [[john]]

## References

- Hashcat documentation
