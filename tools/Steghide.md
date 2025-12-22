---
type: tool
description: >-
  Steganography tool for embedding data into images and audio files with
  encryption.
url: 'http://steghide.sourceforge.net/'
verified: true
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - Obfuscation
  - Steganography
commands:
  - '[[commands/steghide-embed-file-in-image]]'
validated: true
---

# Steghide

**Status**: ✓ Verified

## Overview

Steghide is a steganography tool that enables users to hide data within various image and audio file formats without altering the file's perceptible appearance. It is commonly used in offensive security for covert data exfiltration, embedding payloads, or obfuscating sensitive information during red team operations.

## Description

Steghide conceals an embedded file (payload) inside a cover file (e.g., JPEG, BMP, WAV, AU) using steganographic techniques that preserve color frequencies, making detection resistant to basic statistical analysis. By default, it employs AES (Rijndael-128) encryption, but supports other algorithms like rijndael-192, rijndael-256, and more. The tool prompts for a passphrase to secure the hidden data, ensuring the output file remains visually identical to the original cover.

## Features

- Supports embedding and extraction in JPEG, BMP, WAV, and AU formats
- Encryption with multiple algorithms (AES default)
- Passphrase protection for hidden data
- No alteration to file size or visual quality
- Command-line interface for automation

## Installation

### Requirements

- GCC compiler and development libraries (for building from source)

### Install Commands

```bash
# On Debian/Ubuntu/Kali
sudo apt update
sudo apt install steghide

# On macOS (using Homebrew)
brew install steghide

# On Windows (via Cygwin or build from source)
# Download source from official site and compile with MinGW
```

## Basic Usage

```bash
steghide --help
```

View available options and supported formats.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Display help message |
| -v, --version | Show version information |
| -e, --encrypt | Specify encryption algorithm (e.g., rijndael-128) |
| -p, --passphrase | Provide passphrase non-interactively |

## Examples

### Example 1: Basic Usage

Embed a file into an image:

```bash
steghide embed -ef secret.txt -cf image.jpg
```

Enter passphrase when prompted.

### Example 2: Advanced Usage

Extract hidden data from a file:

```bash
steghide extract -sf image.jpg
```

Enter the passphrase to retrieve the embedded file.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information

### Tactics

- [[Defense Evasion]] Defense Evasion

## Detection

- Monitor for unusual file modifications in media directories
- Analyze file entropy or statistical anomalies in images/audio
- Detect command-line executions of steghide in process logs
- Network exfiltration patterns for seemingly benign media files

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/OpenStego]]
- [[tools/Stegsolve]]

## References

- Official website: http://steghide.sourceforge.net/
- SourceForge repository: https://sourceforge.net/projects/steghide/
