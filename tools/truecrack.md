---
id: 035afa38-1d8d-401f-bed2-7404e736792c
type: tool
verified: true
created_at: '2019-08-28T21:17:28.434338+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - credential-access
  - truecrypt
  - encryption-cracking
  - cuda
url: 'https://github.com/ttrue/TrueCrack'
validated: true
---

# truecrack

**Status**: Unverified

## Overview

TrueCrack is a specialized brute-force password cracker designed for TrueCrypt encrypted volumes. It leverages Nvidia CUDA for GPU acceleration on Linux systems, making it efficient for cracking complex passwords protecting disk encryption. Commonly used in penetration testing to recover access to encrypted data after obtaining the volume file or device.

## Description

TrueCrack targets TrueCrypt (and compatible VeraCrypt) volumes by performing brute-force attacks on the volume headers. It supports PBKDF2 key derivation with RIPEMD160, SHA512, and Whirlpool functions, and XTS mode with AES, Serpent, and Twofish ciphers. Attacks can be dictionary-based or generate passwords from a custom alphabet within length constraints. It handles both file-hosted containers and partition-hosted volumes, including hidden volumes and backup headers. The tool runs on both GPU (Nvidia CUDA) and CPU, with GPU providing significant speedups for intensive cracking tasks.

## Features

- Feature 1: Dictionary attacks using wordlists for common passwords.
- Feature 2: Custom alphabet brute-force for exhaustive generation up to specified lengths.
- Feature 3: Support for multiple encryption modes (AES, Serpent, Twofish) and key derivations (RIPEMD160, SHA512, Whirlpool).
- Feature 4: GPU acceleration via Nvidia CUDA for faster cracking.
- Feature 5: Handling of hidden volumes and backup headers to bypass protections.
- Feature 6: Cross-compatibility with VeraCrypt volumes.

## Installation

### Requirements

- Linux OS (tested on Ubuntu/Debian derivatives).
- Nvidia GPU with CUDA toolkit (version 6.0+ for GPU support).
- GCC compiler and make utilities.
- Optional: CPU-only mode if no GPU available.

### Install Commands

```bash
# Clone the repository
git clone https://github.com/ttrue/TrueCrack.git
cd TrueCrack

# For GPU support (Nvidia CUDA)
make gpu

# For CPU-only support
make cpu

# Install to /usr/local (optional)
sudo make install
```

On Kali Linux, it may be available via apt, but compiling from source is recommended for latest features:

```bash
sudo apt update
sudo apt install git build-essential nvidia-cuda-toolkit
# Then follow clone and make steps above
```

## Basic Usage

```bash
truecrack --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message and usage |
| -v, --version | Show TrueCrack version |
| -s | Specify volume file or device |
| -m | Set encryption mode (AES/Twofish/Serpent) |
| -k | Set key derivation (RIPEMD160/SHA512/Whirlpool) |
| -w | Dictionary wordlist path |
| -a | Custom alphabet for brute-force |
| -l/-L | Min/max password length |
| -b | Use backup header |

## Examples

### Example 1: Basic Usage (Dictionary Attack)

```bash
truecrack -s encrypted_volume.tc -m AES -k RIPEMD160 -w /path/to/wordlist.txt
```

This attempts passwords from the wordlist against an AES-encrypted volume using RIPEMD160 derivation.

### Example 2: Advanced Usage (Alphabet Brute-Force)

```bash
truecrack -s /dev/sdb1 -m Twofish -k Whirlpool -a "abcdefghijklmnopqrstuvwxyz0123456789" -l 6 -L 8 -b
```

Generates and tests 6-8 character passwords from alphanumeric set on a partition-hosted volume, using backup header if needed.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Unsecured Credentials]] Unsecured Credentials

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high GPU utilization (nvidia-smi shows truecrack process) during unexpected times.
- Detection method 2: File system access logs showing reads on encrypted volume files (.tc, .hc).
- Detection method 3: Network inactivity combined with CPU/GPU spikes on endpoints with access to encrypted data.
- Detection method 4: Presence of TrueCrack binaries or source in temporary directories (/tmp, /var/tmp).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/john-the-ripper]]
- [[tools/Hashcat]]

## References

- Official GitHub: https://github.com/ttrue/TrueCrack
- TrueCrypt Documentation: https://www.truecrypt.org/docs/
