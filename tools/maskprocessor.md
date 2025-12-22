---
id: c2058346-c3b3-47db-86d1-c07e9d76d2b6
type: tool
verified: true
description: >-
  High-performance word generator for mask-based password cracking and
  brute-force attacks.
url: 'https://github.com/hashcat/maskprocessor'
tags:
  - password-cracking
  - wordlist-generation
  - brute-force
platforms:
  - Linux
  - Windows
  - macOS
commands:
  - '[[commands/maskprocessor-generate-basic-mask]]'
  - '[[commands/maskprocessor-generate-custom-charset]]'
created_at: '2019-08-28T21:17:22.406223+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
validated: true
---

# maskprocessor

**Status**: Unverified

## Overview

Maskprocessor is a high-performance word generator designed for generating password candidates based on customizable masks. It is particularly useful in offensive security operations for creating targeted wordlists for cracking hashed passwords, such as in scenarios involving credential dumping or offline attacks. The tool supports per-position charset configuration, making it efficient for complex mask patterns without the overhead of scripting.

## Description

Maskprocessor operates as a standalone binary that processes mask patterns to produce wordlists at high speeds. It is part of the hashcat ecosystem but can be used independently. Common use cases include generating permutations for known password structures (e.g., 8 characters with mixed case and digits) during post-exploitation credential attacks or preparing inputs for tools like hashcat. It excels in scenarios requiring massive generation without memory constraints, supporting incremental modes for large-scale brute-forcing.

## Features

- **Per-Position Charsets**: Define custom character sets for each position in the mask (e.g., lowercase for first chars, digits for last).
- **High Performance**: Optimized for speed, capable of generating billions of candidates per second on modern hardware.
- **Incremental Generation**: Supports keyspace exploration for resuming or distributing generation tasks.
- **Output Flexibility**: Direct to stdout, files, or pipes for integration with other tools.
- **Cross-Platform**: Compiled binaries available for Linux, Windows, and macOS.

## Installation

### Requirements

- GCC or compatible compiler (for building from source).
- Git (to clone the repository).
- Supported platforms: Linux, Windows (with MinGW), macOS.

### Install Commands

```bash
# Clone the repository
git clone https://github.com/hashcat/maskprocessor.git

# Build the binary
cd maskprocessor
make

# The executable 'maskprocessor' will be in the current directory
```

Pre-built binaries are available in the releases section of the GitHub repository for quick deployment without compilation.

## Basic Usage

```bash
./maskprocessor [options] <mask>
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message and exit |
| `--stdout` | Output to stdout instead of file |
| `-o <file>` | Specify output file |
| `--keyspace` | Display keyspace size without generating |
| `-i, --increment` | Enable incremental mode for large generations |
| `--cpu-affinity` | Bind to specific CPU cores for performance |

## Examples

### Example 1: Basic Usage

Generate a simple wordlist of 4 lowercase letters followed by 2 digits and save to a file.

```bash
./maskprocessor ?l?l?l?l?d?d -o passwords.txt
```

### Example 2: Advanced Usage

Generate passwords using a custom charset for the first position (uppercase only) and incremental mode.

```bash
./maskprocessor -1 ?u ?1?l?l?d?d?d --increment -o custom_passwords.txt
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

- Process monitoring for 'maskprocessor' binary execution, often with high CPU usage.
- File system scans for large generated wordlist files (e.g., patterns like passwords.txt with mask-generated content).
- Network logs if output is piped to remote cracking tools; local disk I/O spikes during generation.

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

- Official GitHub: https://github.com/hashcat/maskprocessor
- Hashcat Documentation: https://hashcat.net/wiki/
