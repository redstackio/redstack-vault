---
id: uuid7
url: 'https://github.com/google/highwayhash'
tags:
  - secure-hash
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:49.022Z'
validated: true
submitted: true
---
# HighwayHash

**Status**: Unverified

## Overview

HighwayHash is a secure, fast keyed hash function from Google, recommended to mitigate hash-collision DoS in parsers like Snudown.

## Description

Designed for cryptographic security against collision attacks, it's used in offensive security to test or replace weak hashes, ensuring constant-time operations even under adversarial inputs.

## Features

- 64-bit and 128-bit outputs
- Keyed for security
- High performance on modern CPUs

## Installation

### Requirements

- C++ compiler
- CMake

### Install Commands

```bash
# Clone and build
git clone https://github.com/google/highwayhash.git
cd highwayhash
make
```

## Basic Usage

```bash
# Example compilation and run
clang++ -O3 -c highwayhash.h -o test
./test key input
```

### Common Options

| Option | Description |
|--------|-------------|
| Key input | 128-bit key for hashing |

## Examples

### Example 1: Basic Usage

```bash
# Hash a string with key
echo "test" | ./highwayhash 0xkeybytes
```

### Example 2: Advanced Usage

Integrate into C code for table hashing:

```bash
// Pseudo: use HighwayHash64(key, str) % table_size
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of highwayhash binaries
- Changes to hash functions in code

## Related Procedures


## Related Tools

- [[tools/SipHash]]

## References

- GitHub: https://github.com/google/highwayhash
