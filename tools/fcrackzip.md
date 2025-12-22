---
id: tool-uuid-5
url: 'http://oldhome.schmorp.de/marc/fcrackzip.html'
tags:
  - cracking
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:48.574Z'
validated: true
submitted: true
---
# Fcrackzip

**Status**: Unverified

## Overview

Fcrackzip brute-forces passwords on ZIP archives using dictionary attacks.

## Description

Optimizes ZIP cracking with unzip verification.

## Features

- Dictionary mode
- Unzip check

## Installation

### Requirements

- Build tools

### Install Commands

```bash
# Ubuntu
apt install fcrackzip
```

## Basic Usage

```bash
fcrackzip -D -p list.zip file.zip
```

### Common Options

| Option | Description |
|--------|-------------|
| -u | Unzip |
| -D | Dict |
| -p | Passlist |

## Examples

### Example 1: Basic Usage

```bash
fcrackzip -u file.zip
```

### Example 2: Advanced Usage

```bash
fcrackzip -D -p list file.zip
```

## MITRE ATT&CK Mapping

### Techniques

- [[Password Guessing]] Password Guessing

### Tactics

- [[Lateral Movement]] Lateral Movement

## Detection

- ZIP access attempts

## Related Procedures

- [[procedures/Brute-Force-Credentials-and-Manipulate-Base64-Cookie]]

## Related Tools

- [[tools/John-the-Ripper]]

## References

- Source forge
