---
id: 79d9753f-ed9a-4f08-a968-3351b5e71888
name: oclgausscrack
type: tool
verified: true
created_at: '2019-08-28T21:17:26.530495+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - cracking
  - malware-analysis
  - opencl
  - gpu
  - hashcat
url: 'https://github.com/epfl-cds/oclgausscrack'
validated: true
---

# oclgausscrack

**Status**: Unverified

## Overview

oclgausscrack is a specialized open-source tool for cracking the verification hash of the encrypted payload in the Gauss malware, a advanced persistent threat targeting financial institutions. It uses OpenCL to accelerate the computationally intensive process of performing 10,000 MD5 hash iterations per password candidate, making it suitable for GPU-accelerated cracking in malware reverse engineering and forensic analysis.

## Description

Developed to decrypt the Gauss virus payload, oclgausscrack employs optimizations inspired by oclHashcat-plus for high performance. It supports multi-GPU setups (of identical hardware types) and is compatible with VCL (Virtual CL) version 1.18 for virtualized environments. The tool is designed for integration into distributed computing frameworks and includes resume functionality for long-running cracking sessions. Use it in scenarios involving historical malware analysis or similar hash-breaking tasks requiring repeated MD5 computations.

## Features

- OpenCL-based GPU acceleration for 10k MD5 iteration loops
- Performance optimizations derived from oclHashcat-plus
- Support for multi-GPU configurations (same GPU type only)
- Compatibility with VCL 1.18 for virtual OpenCL
- Open-source codebase for customization and auditing
- Resume support for interrupted sessions
- Integration capabilities for distributed cracking environments

## Installation

### Requirements

- OpenCL-compatible GPU (NVIDIA/AMD) with drivers installed
- GCC compiler and Make for building
- OpenCL development headers (e.g., ocl-icd-opencl-dev on Ubuntu)
- Optional: VCL 1.18 for virtualized CL support

### Install Commands

```bash
# On Ubuntu/Debian (Kali similar)
sudo apt update
sudo apt install git build-essential ocl-icd-opencl-dev

# Clone the repository
git clone https://github.com/epfl-cds/oclgausscrack.git
cd oclgausscrack

# Build the tool
make

# For NVIDIA GPUs, ensure CUDA/OpenCL drivers are installed
# Test with: clinfo (to verify OpenCL platforms)
```

For other platforms like Windows, use Visual Studio with OpenCL SDK, but Linux is recommended for security testing.

## Basic Usage

```bash
oclgausscrack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and exit |
| -v, --version | Show version information |
| --resume | Resume from a previous session (uses .resume file) |

## Examples

### Example 1: Basic Usage

```bash
oclgausscrack -h gauss_verification_hash.hex -w /usr/share/wordlists/rockyou.txt
```

This runs the cracker against a hash file using the rockyou wordlist, outputting progress to stdout.

### Example 2: Advanced Usage

```bash
oclgausscrack -h input_hash.hex -w custom_dict.txt -o cracked.txt --resume
```

Resumes a session if interrupted, saving the result to cracked.txt.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for hash cracking in credential access scenarios)
- [[Network Sniffing]] Network Sniffing (in broader malware analysis contexts)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- GPU utilization spikes with OpenCL processes (monitor clinfo or GPU tools like nvidia-smi)
- File artifacts: .resume files or temporary hash/wordlist accesses in /tmp
- Process monitoring: Look for oclgausscrack binary executions in forensic timelines
- Network: If integrated with distributed systems, unusual outbound connections to cracking clusters

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]

## References

- Original repository: https://github.com/epfl-cds/oclgausscrack
- Gauss Malware analysis: Kaspersky Lab reports on Duqu/Flame family
- OpenCL documentation: Khronos Group
