---
id: c3a549fc-4cd3-44a1-aff5-263676411352
name: pd-phrasendrescher
type: tool
verified: true
created_at: '2019-08-28T21:17:26.626094+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - macOS
  - FreeBSD
  - NetBSD
  - OpenBSD
tags:
  - password-cracking
  - brute-force
  - dictionary-attack
  - credential-access
url: 'https://github.com/d3vid-hack/phrasendrescher'
commands:
  - '[[commands/pd-dictionary-attack]]'
  - '[[commands/pd-brute-force-incremental]]'
  - '[[commands/pd-list-plugins]]'
validated: true
---

# pd-phrasendrescher

**Status**: Unverified

## Overview

phrasen|drescher (p|d) is a modular, multi-processing passphrase cracking tool designed for offensive security operations. It supports dictionary-based attacks with permutations (such as case variations and l33t speak) and incremental brute-force attacks using custom character maps. The tool is extensible via a simple plugin API, allowing users to develop custom modules for specific cracking scenarios, such as targeting encrypted files, network services, or hash formats.

## Description

p|d excels in cracking passphrases offline or against vulnerable services by leveraging multiple CPU cores for parallel processing. It is particularly useful in red team engagements for recovering credentials from captured hashes, encrypted archives, or weak authentication mechanisms. Plugins handle various input formats (e.g., hashes, encrypted data) and output cracked results. The tool supports a range of permutations to adapt to common user password patterns without exhaustive computation.

## Features

- **Modular Plugin System**: Easy extension for new cracking targets like SSH keys, WiFi passwords, or custom hashes.
- **Multi-Processing**: Utilizes multiple cores to speed up attacks on large wordlists or keyspaces.
- **Dictionary Attacks**: Supports base wordlists with optional mutations (uppercase, lowercase, l33t substitutions, append/prepend rules).
- **Incremental Brute Force**: Custom character sets for targeted guessing, avoiding full keyspace exhaustion.
- **Cross-Platform Compatibility**: Works on Unix-like systems including Linux, macOS, and BSD variants.

## Installation

### Requirements

- GCC compiler and make utilities.
- Perl (for some plugins).
- Sufficient CPU cores for multi-processing benefits.

### Install Commands

```bash
# Clone the repository
git clone https://github.com/d3vid-hack/phrasendrescher.git pd
cd pd

# Compile the tool
make

# For Ubuntu/Debian dependencies
sudo apt update
sudo apt install build-essential git perl

# For macOS (using Homebrew)
brew install gcc make git perl
```

After compilation, the `pd` binary will be available in the current directory. Add it to your PATH for global access: `sudo cp pd /usr/local/bin/`.

## Basic Usage

```bash
./pd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-m, --mode` | Specify cracking mode (dictionary, brute).
| `-p, --plugin` | Select a plugin for the target type (e.g., hash, ssh).
| `-t, --threads` | Number of processing threads (default: CPU cores).
| `-v, --verbose` | Enable detailed output for debugging.
| `-o, --output` | File to save cracked results.

## Examples

### Example 1: Basic Usage

Run a simple dictionary attack on a hash file using the default plugin:

```bash
./pd -m dictionary -f wordlist.txt -u hashes.txt -o cracked.txt
```

### Example 2: Advanced Usage

Perform a brute-force attack with custom character map and multi-threading:

```bash
./pd -m brute -c 'abc123' -l 8 -t 4 -u target.txt -o results.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force
- [[Password Guessing]] Password Guessing
- [[Password Cracking]] Password Cracking

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- High CPU utilization on cracking machines during engagements.
- Presence of large wordlist files or temporary output files in working directories.
- Network traffic if plugins target online services (monitor for repeated authentication attempts).
- Process monitoring for `pd` binary or child processes consuming multiple cores.

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

- Official GitHub Repository: https://github.com/d3vid-hack/phrasendrescher
- Plugin Development Guide: Included in source docs

*Last updated: 2023-05-29T16:48:53.029709+00:00*
