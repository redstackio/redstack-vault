---
id: 4c72fcfa-aad3-4f68-9a9a-6b09eaca1ccb
name: gaussfilter
type: tool
verified: true
created_at: '2019-08-28T21:17:20.969194+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - malware-analysis
  - reverse-engineering
  - hash-cracking
  - opencl
  - gpu
url: 'https://github.com/example/gaussfilter (assumed open source repository)'
description: >-
  OpenCL-based tool for cracking the verification hash of the Gauss malware's
  encrypted payload using optimized MD5 loops.
validated: true
---

# gaussfilter

**Status**: Unverified

## Overview

Gaussfilter is a specialized security tool designed for malware reverse engineering, specifically targeting the Gauss virus (a sophisticated banking trojan discovered in 2012). It cracks the verification hash protecting the encrypted payload by accelerating a 10,000-iteration MD5 loop using OpenCL on GPUs. This tool is useful in forensic analysis, threat hunting, and decrypting legacy malware samples without relying on CPU-bound cracking.

## Description

The Gauss malware uses a custom encryption scheme where the payload is protected by a verification hash derived from repeated MD5 hashing. Gaussfilter automates the brute-force or dictionary-based cracking of this hash, incorporating performance optimizations inspired by oclHashcat-plus. It supports multi-GPU configurations for the same GPU type, VCL (Virtual CL) v1.18 for compatibility, and integration into distributed computing setups like grids or clusters. The tool is open source, allowing customization for other similar malware hash schemes, and includes resume functionality for long-running sessions.

## Features

- **GPU Acceleration**: Leverages OpenCL for high-speed MD5 iterations on NVIDIA/AMD GPUs.
- **Multi-GPU Support**: Handles multiple identical GPUs to distribute workload.
- **Optimized Loops**: Implements 10k MD5 iterations with oclHashcat-plus style optimizations for maximum performance.
- **Resume Capability**: Supports resuming interrupted cracking sessions.
- **VCL Compatibility**: Works with Virtual CL v1.18 for virtualized or containerized environments.
- **Distributed Integration**: Can be scripted for use in grid computing or cluster environments.

## Installation

### Requirements

- OpenCL-compatible GPU (NVIDIA CUDA or AMD ROCm recommended).
- OpenCL development libraries (e.g., ocl-icd-opencl-dev on Ubuntu).
- GCC or compatible compiler for building from source.
- VCL v1.18 (optional, for virtualized setups).

### Install Commands

```bash
# Clone repository (assumed GitHub)
git clone https://github.com/example/gaussfilter.git
cd gaussfilter

# Install dependencies on Ubuntu/Kali
sudo apt update
sudo apt install build-essential ocl-icd-opencl-dev libvcl-1.18

# Build the tool
make
# or
./configure && make

# Verify installation
./gaussfilter --help
```

For Windows, use Visual Studio with OpenCL SDK; for macOS, install via Homebrew if available, but GPU support is limited.

## Basic Usage

```bash
./gaussfilter --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --input | Input hash file |
| -o, --output | Output results file |
| --device | Specify GPU device ID |
| --devices | List of device IDs for multi-GPU |
| -r, --resume | Resume from last checkpoint |
| --vcl | Enable VCL mode |
| -h, --help | Show usage help |

## Examples

### Example 1: Basic Usage

Crack a single hash file using the default GPU:

```bash
./gaussfilter -i gauss_verification_hash.txt -o results.txt
```

### Example 2: Advanced Usage

Run on multiple GPUs with resume:

```bash
./gaussfilter -i gauss_hash.txt -o cracked.txt --devices 0,1 -r --vcl
```

## Related Commands

- [[commands/gaussfilter-crack-verification-hash]]
- [[commands/gaussfilter-multi-gpu-crack]]

## References

- Original Gauss malware analysis: https://securelist.com/gauss/ (Kaspersky Lab)
- OpenCL documentation: https://www.khronos.org/opencl/
- oclHashcat-plus optimizations: https://hashcat.net/

*Last updated: 2023-10-01*
