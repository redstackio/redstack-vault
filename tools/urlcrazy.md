---
id: 14060d30-07b2-4041-b366-0cf53d4ed197
type: tool
verified: true
created_at: '2019-08-28T21:17:17.895075+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - reconnaissance
  - typosquatting
  - domain-hijacking
url: 'https://github.com/urbanadventurer/urlcrazy'
validated: true
---

# urlcrazy

**Status**: Unverified

## Overview

urlcrazy is a command-line tool for generating and testing domain name typos and variations. It helps security professionals identify potential typosquatting, URL hijacking, phishing sites, and corporate espionage risks by simulating common user errors in typing domain names.

## Description

urlcrazy automates the creation of domain variants based on 15 mutation types, including common misspellings (over 8000 known errors), bit flipping (simulating cosmic ray errors), and keyboard layout swaps (qwerty, azerty, qwertz, dvorak). It validates variants for syntactic correctness, resolves them to check if they are registered, and estimates their popularity using metrics like Alexa rankings. This tool is particularly useful in red teaming for reconnaissance phases, assessing brand protection, or hunting for phishing domains.

## Features

- Generates 15 types of domain variants (e.g., homographs, omissions, repetitions, vowel swaps)
- Incorporates over 8000 common misspellings from various sources
- Supports bit flipping mutations to simulate hardware errors
- Handles multiple keyboard layouts for international typing variations
- Validates domain syntax before resolution
- Performs DNS resolution to check if variants are in use
- Estimates domain popularity and potential traffic hijack risk
- Outputs results in categorized, scannable format for easy analysis

## Installation

### Requirements

- Ruby 1.9 or later
- Bundler (Ruby gem manager)
- Internet access for DNS resolutions

### Install Commands

```bash
# Clone the repository
git clone https://github.com/urbanadventurer/urlcrazy.git
cd urlcrazy

# Install dependencies
bundle install

# Make executable (if needed)
chmod +x urlcrazy.rb

# For Kali/Ubuntu: Install Ruby if not present
sudo apt update
sudo apt install ruby ruby-dev bundler
```

Alternatively, for a system-wide install:

```bash
# Add to PATH or use ruby urlcrazy.rb directly
```

## Basic Usage

```bash
urlcrazy --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -g | Generate variants only, skip resolution checks |
| -r | Resolve and check availability of variants |
| -l LAYOUT | Specify keyboard layout (e.g., qwerty, azerty) |
| -o FILE | Output results to a file |
| -v | Verbose mode for detailed output |

## Examples

### Example 1: Basic Usage

Generate and check variants for a domain:

```bash
urlcrazy example.com
```

### Example 2: Advanced Usage

Generate variants for a specific layout and output to file:

```bash
urlcrazy -l qwertz -o variants.txt example.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1583.001]] Domains
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic: High volume of DNS queries for similar domain names from a single source
- Process monitoring: Ruby processes executing urlcrazy.rb or high CPU from variant generation
- Log analysis: Unusual patterns in DNS resolver logs showing sequential similar queries
- File system: Presence of urlcrazy repository or output files with domain lists

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dnstwist]]
- [[tools/knockpy]]

## References

- Official GitHub: https://github.com/urbanadventurer/urlcrazy
- Ruby documentation for dependencies
