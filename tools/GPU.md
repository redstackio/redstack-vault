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
  Graphics Processing Unit hardware used for parallel computing tasks like
  password hash cracking.
id: d88d3a68-90b9-42d6-82b0-41807b332387
created_at: '2025-12-11T03:47:59.559Z'
updated_at: '2025-12-11T03:47:59.559Z'
verified: false
validated: true
submitted: true
---
# GPU

**Status**: Unverified

## Overview

GPUs are hardware accelerators used in security for high-speed computations, such as cracking password hashes extracted from systems like VPN servers.

## Description

In offensive security, GPUs power tools like Hashcat for brute-forcing hashes, enabling rapid cracking of admin credentials for escalation.

## Features

- Parallel processing for speed
- Compatibility with cracking software
- High throughput for cryptographic tasks

## Installation

### Requirements

- Compatible GPU hardware (e.g., NVIDIA)
- Drivers and CUDA/OpenCL

### Install Commands

```bash
# Install drivers via vendor tools
```

## Basic Usage

```bash
# Used via cracking tools like hashcat --help
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Hardware-specific |

## Examples

### Example 1: Basic Usage

```bash
hashcat -m 0 -a 0 hash.txt wordlist.txt --opencl-device-types 1,2
```

### Example 2: Advanced Usage

```bash
hashcat -m 1000 -a 3 admin_hash.txt ?a?a?a?a?a?a --opencl-device-types 1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credential Dumping]]

### Tactics

- [[Credential Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for high GPU utilization
- Log executions of cracking tools

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Hashcat]] (inferred)

## References

- GPU cracking guides
