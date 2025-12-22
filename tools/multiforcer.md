---
id: 04a4af9f-5ea4-42b7-b3b9-a01881d6acaa
name: multiforcer
type: tool
verified: true
created_at: '2019-08-28T21:17:41.712916+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - hash-cracking
  - rainbow-tables
  - gpu-acceleration
  - credential-access
url: 'https://github.com/ryancdotorg/multiforcer'
commands:
  - '[[commands/multiforcer-brute-force-ntlm-hash]]'
  - '[[commands/multiforcer-generate-rainbow-table-md5]]'
validated: true
---

# multiforcer

**Status**: Unverified

## Overview

Multiforcer is a GPU-accelerated tool for generating rainbow tables and brute-forcing hashes. It supports multiple hash types including MD5, SHA1, LM, NTLM, and others, leveraging CUDA and OpenCL for high-performance cracking in offensive security operations like password recovery from credential dumps.

## Description

Multiforcer implements rainbow tables from scratch and provides brute-force capabilities optimized for graphics cards. It is particularly useful in red team engagements for offline analysis of captured hashes, enabling rapid password guessing without CPU limitations. Common use cases include cracking NTLM hashes from Windows environments or generating custom rainbow tables for specific charsets.

## Features

- GPU acceleration via CUDA and OpenCL for faster cracking
- Support for hash types: MD5, SHA1, SHA256, LM, NTLM, and more
- Rainbow table generation and lookup for efficient cracking
- Custom charset definitions for targeted brute-force attacks
- Distributed table generation for large-scale operations
- Output formatting compatible with tools like Hashcat

## Installation

### Requirements

- NVIDIA GPU with CUDA toolkit (for CUDA mode) or AMD/Intel GPU with OpenCL
- GCC compiler and Make
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ryancdotorg/multiforcer.git
cd multiforcer

# Compile with CUDA support (requires CUDA installed)
make cuda

# Or compile with OpenCL support
make opencl

# For CPU fallback (slower)
make
```

On Kali Linux, it may require additional dependencies:

```bash
apt update && apt install build-essential cuda-toolkit-opencl-1-2-headless
```

## Basic Usage

```bash
multiforcer --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version information |
| --force | Overwrite output files |
| -t $_THREADS | Number of threads to use |

## Examples

### Example 1: Basic Usage

Brute-force a hash file:

```bash
multiforcer -f hashes.txt -o cracked.txt -c charset.def
```

### Example 2: Advanced Usage

Generate a rainbow table:

```bash
multiforcer --rainbow -f table.rt -c alphanum.def --hash-type ntlm --table-index 0 --chain-length 1000 --chain-num 1000000
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- GPU utilization spikes during cracking sessions
- Process monitoring for 'multiforcer' executable
- Network traffic if tables are transferred (though typically offline)
- File system artifacts like .rt rainbow tables or charset files

## Related Procedures

- [[procedures/Crack-NTLM-Hashes-Offline]]
- [[procedures/Generate-and-Use-Rainbow-Tables]]

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Official GitHub: https://github.com/ryancdotorg/multiforcer
- CUDA Documentation: https://developer.nvidia.com/cuda-toolkit
