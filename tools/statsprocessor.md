---
id: 87a54bb6-2fb0-41a4-a8e8-8dae331df145
type: tool
verified: true
description: >-
  High-performance word generator using per-position Markov chains for password
  candidate generation.
url: 'https://github.com/hashcat/hashcat-utils'
created_at: '2019-08-28T21:17:19.242868+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
tags:
  - wordlist-generation
  - password-cracking
  - markov-chain
commands:
  - '[[commands/statsprocessor-generate-basic-wordlist]]'
  - '[[commands/statsprocessor-generate-specified-count]]'
validated: true
---

# statsprocessor

**Status**: Unverified

## Overview

Statsprocessor is a standalone binary tool designed for high-performance generation of password candidates using per-position Markov chain attacks. It's part of the hashcat ecosystem and excels at creating realistic wordlists from statistical models derived from known passwords, making it ideal for offline password cracking in red team operations and security research.

## Description

The tool processes .chrstats or .stats files (typically output from hashcat's maskprocessor) to generate candidates based on positional probabilities of characters. This allows for efficient, targeted brute-force attacks that mimic real password patterns without exhaustive enumeration. Common use cases include augmenting dictionary attacks, testing password policies, and training machine learning models for credential stuffing defenses.

## Features

- **High Performance**: Generates millions of candidates per second on modern hardware.
- **Per-Position Markov**: Builds chains based on character transitions at each password position for realistic outputs.
- **Standalone Binary**: No dependencies beyond basic libc; compiles easily.
- **Flexible Output**: Supports stdout piping or direct file writing.
- **Integration Ready**: Works seamlessly with hashcat, John the Ripper, and custom cracking pipelines.

## Installation

### Requirements

- GCC or Clang compiler
- Make utility
- Git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/hashcat/hashcat-utils.git
cd hashcat-utils/src

# Compile the binary
make statsprocessor

# Make executable and move to PATH (optional)
chmod +x statsprocessor
sudo mv statsprocessor /usr/local/bin/
```

For precompiled binaries, check releases on the GitHub repository.

## Basic Usage

```bash
./statsprocessor --help
```

This displays available options and syntax.

### Common Options

| Option | Description |
|--------|-------------|
| (No flags needed for basic use) | Processes stats file directly |
| (Pipe output) | Use with `| head -n N` for limiting |

## Examples

### Example 1: Basic Usage

Generate candidates from a stats file to stdout:

```bash
./statsprocessor passwords.chrstats
```

### Example 2: Advanced Usage

Generate 1 million candidates to a file:

```bash
[[commands/statsprocessor-generate-specified-count]]
./statsprocessor passwords.chrstats 1000000 candidates.txt
```

Use the basic generation and pipe:

```bash
[[commands/statsprocessor-generate-basic-wordlist]]
./statsprocessor passwords.chrstats | head -n 100000 > small_list.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Password Cracking]] Password Cracking
- [[Password Guessing]] Password Guessing

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of compiled binary named 'statsprocessor' in temporary directories.
- Large temporary wordlist files with patterned password candidates.
- High CPU usage during generation on compromised systems.
- File system artifacts like .chrstats files from hashcat tools.

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
- [[tools/maskprocessor]]

## References

- Official GitHub: https://github.com/hashcat/hashcat-utils
- Hashcat Documentation: https://hashcat.net/wiki/
