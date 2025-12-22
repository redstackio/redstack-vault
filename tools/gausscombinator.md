---
id: 87a42203-0919-4f93-a872-d951710b909c
name: gausscombinator
type: tool
verified: true
created_at: '2019-08-28T21:17:22.088652Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - hash-cracking
  - malware-analysis
  - opencl
  - gpu
url: 'https://github.com/gausscombinator/gausscombinator'
validated: true
---

# gausscombinator

**Status**: Unverified

## Overview

GaussCombinator is a specialized open-source tool designed to crack the verification hash protecting the encrypted payload of the Gauss malware. It leverages OpenCL for GPU acceleration to efficiently handle the intensive 10k MD5 iteration loop required for this specific cracking task. Commonly used in malware reverse engineering and forensic analysis to decrypt Gauss samples.

## Description

The tool focuses on brute-forcing or dictionary-attacking the unique verification mechanism of the Gauss virus, a sophisticated APT malware targeting financial institutions. By using optimizations inspired by oclHashcat-plus, it achieves high performance on GPU hardware. It supports multi-GPU configurations (same type only), is compatible with VCL (Virtual CL) v1.18, and includes features for resuming sessions and integration into distributed computing setups, making it suitable for large-scale cracking operations in security research environments.

## Features

- OpenCL-accelerated 10k MD5 loop for Gauss verification hash cracking
- Optimizations from oclHashcat-plus for maximum GPU performance
- Multi-GPU support for identical hardware setups
- VCL (Virtual CL) v1.18 compatibility for virtualized environments
- Resume functionality to continue interrupted sessions
- Open-source with support for distributed computing integration

## Installation

### Requirements

- OpenCL-compatible GPU (NVIDIA/AMD)
- OpenCL development libraries (e.g., ocl-icd-opencl-dev on Ubuntu)
- GCC compiler and make
- VCL v1.18 or compatible OpenCL runtime

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/gausscombinator/gausscombinator.git
cd gausscombinator

# Install dependencies on Ubuntu/Kali
sudo apt update
sudo apt install ocl-icd-opencl-dev build-essential

# Build the tool
make

# For NVIDIA GPUs, ensure CUDA/OpenCL drivers are installed
sudo apt install nvidia-opencl-dev
```

On Kali Linux, OpenCL libraries are often pre-installed or available via apt.

## Basic Usage

```bash
gausscombinator --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input file with Gauss hash |
| -o, --output | Output file for results |
| --device | Specify device (cpu/gpu) |
| --multi | Enable multi-GPU mode |
| --resume | Resume from session file |
| -h, --help | Show help message |
| -v, --verbose | Verbose output for debugging |

## Examples

### Example 1: Basic Usage

```bash
gausscombinator -i gauss_hash.txt -o results.txt
```

Run a basic single-device crack on the input hash file.

### Example 2: Advanced Usage

```bash
gausscombinator --device gpu -i gauss_hash.txt -o results.txt --multi --resume session.dat
```

Multi-GPU crack resuming a previous session.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for credential/hash cracking in malware analysis)
- [[Unsecured Credentials]] Unsecured Credentials (recovering malware-encrypted secrets)

### Tactics

- [[Credential Access]] Credential Access

## Detection

- Monitor for high GPU utilization and OpenCL library loads (e.g., libOpenCL.so)
- Process monitoring for gausscombinator executable or similar hash-cracking tools
- Network traffic if integrated with distributed computing (unusual outbound connections)
- File system changes: creation of session/resume files in working directories

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/oclhashcat]]
- [[tools/john-the-ripper]]

## References

- Original project source (assumed GitHub or security research repo)
- Gauss malware analysis reports (e.g., Kaspersky Lab documentation)
- OpenCL specification for GPU acceleration
