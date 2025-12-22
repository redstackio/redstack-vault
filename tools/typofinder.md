---
id: 50dd7236-0e8f-4936-b47c-9e01b8e6d955
name: typofinder
type: tool
verified: true
created_at: '2019-08-28T21:17:23.539571+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - reconnaissance
  - typosquatting
  - domain-typos
url: 'https://github.com/example/typofinder'
validated: true
---

# typofinder

## Overview

Typofinder is a command-line tool designed for discovering potential typosquatting domains by generating common typographical variations (typos) of a given domain name. It resolves these typos to IP addresses and identifies the country of origin for each IP, helping security researchers detect malicious domains that mimic legitimate ones for phishing or brand protection purposes.

Category: Reconnaissance

## Installation

### Requirements

- Python 3.6+
- Required libraries: dnspython, geoip2 (for country lookup)

### Install Commands

On Kali/Ubuntu:

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/typofinder.git
cd typofinder

# Install dependencies
pip3 install -r requirements.txt

# Or install directly if available via pip
pip3 install typofinder
```

On macOS:

```bash
brew install python3
pip3 install typofinder
```

Supported Platforms: Linux, macOS (Windows via WSL).

## Basic Usage

```bash
typofinder --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -d, --domain | Specify the target domain |
| -o, --output | Save results to a file |
| -v, --verbose | Enable verbose output for debugging |
| -c, --country-only | Output only country information |

## Examples

### Example 1: Basic Usage

Scan for typos of example.com and display results:

```bash
[[commands/typofinder-basic-typo-scan]]
```

### Example 2: Advanced Usage

Scan and save to file:

```bash
[[commands/typofinder-scan-with-output]]
```

## Related Commands

- [[commands/typofinder-basic-typo-scan]]
- [[commands/typofinder-scan-with-output]]

## References

- Official repository: https://github.com/example/typofinder
- Related to typosquatting detection techniques in MITRE ATT&CK [[T1583.001]]
