---
id: uuid8
url: 'https://github.com/veorq/SipHash'
tags:
  - secure-hash
type: tool
verified: false
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:49.008Z'
validated: true
submitted: true
---
# SipHash

**Status**: Unverified

## Overview

SipHash is a secure keyed hash function designed to prevent hash-flooding DoS attacks, suggested as a replacement for weak hashes like SDBM in Snudown.

## Description

It provides collision resistance for hash tables in security testing and production, used offensively to validate mitigations against complexity attacks.

## Features

- 64-bit output
- PRF (pseudorandom function)
- Efficient for short inputs

## Installation

### Requirements

- C compiler

### Install Commands

```bash
# Clone and build
git clone https://github.com/veorq/SipHash.git
cd SipHash
make
```

## Basic Usage

```bash
./siphash key input
```

### Common Options

| Option | Description |
|--------|-------------|
| key | 128-bit key |
| input | Data to hash |

## Examples

### Example 1: Basic Usage

```bash
./siphash 0xdeadbeef input_string
```

### Example 2: Advanced Usage

In code:

```bash
// Use siphash24(key, str) for table indexing
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Disable or Modify Tools]] Impair Defenses: Disable or Modify Tools

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

Indicators and methods for detecting this tool's usage:

- SipHash library inclusions
- Hash function updates

## Related Procedures


## Related Tools

- [[tools/HighwayHash]]

## References

- GitHub: https://github.com/veorq/SipHash
