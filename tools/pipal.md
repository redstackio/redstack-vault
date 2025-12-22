---
id: b814a7f0-2ec4-4594-8a45-3a7af1d16fed
type: tool
verified: true
created_at: '2019-08-28T21:17:29.353176+00:00'
updated_at: '2023-10-01T12:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - password-analysis
  - cracking
  - ruby
url: 'https://github.com/digininja/pipal'
validated: true
---

# pipal

**Status**: Unverified

## Overview

Pipal is a Ruby-based password analysis tool designed to process large password lists and generate statistical insights into common patterns, base words, keyboard sequences, and other structures. It helps security professionals and penetration testers understand password strength distributions and prioritize cracking efforts by highlighting weaknesses like common words or predictable patterns.

## Description

Pipal reads a plain text file containing passwords (one per line) and performs analysis to identify trends such as:
- Frequency of base words (e.g., 'password', '123456')
- Keyboard walking patterns (e.g., 'qwerty', 'asdf')
- Repetitive characters (e.g., 'aaaaa')
- L33t speak variations (e.g., 'p@ssw0rd')
- Name-based passwords and other common categories

The tool outputs results to the console, making it ideal for quick analysis during red team engagements, password audits, or after dumping credential databases. It does not perform cracking itself but provides data to inform tools like Hashcat or John the Ripper.

## Features

- **Pattern Recognition**: Detects keyboard walks, repetitions, and common substitutions.
- **Statistical Summaries**: Counts total, unique, and categorized passwords.
- **Customizable Analysis**: Processes any text file format with one password per line.
- **Lightweight**: Ruby script with no heavy dependencies beyond standard Ruby libraries.

## Installation

### Requirements

- Ruby 1.9 or later (Ruby 2.x recommended)
- Git for cloning the repository

### Install Commands

On Kali Linux (pre-installed in some versions, but verify):

```bash
# If not pre-installed, clone from GitHub
sudo apt update
sudo apt install ruby git

# Clone the repository
git clone https://github.com/digininja/pipal.git /opt/pipal
cd /opt/pipal
# No further installation needed; run directly with ruby
```

On Ubuntu:

```bash
sudo apt update
sudo apt install ruby-full git

git clone https://github.com/digininja/pipal.git /opt/pipal
```

On macOS (using Homebrew):

```bash
brew install ruby
git clone https://github.com/digininja/pipal.git /opt/pipal
```

Alternative: Install via RubyGems if available (though primarily a Git repo):

```bash
gem install pipal
```

## Basic Usage

```bash
ruby /opt/pipal/pipal.rb /path/to/passwords.txt
```

### Common Options

Pipal has minimal command-line options; it primarily relies on the input file path. For help:

| Option | Description |
|--------|-------------|
| No flags needed | Processes the entire file and outputs to stdout |

To save output:

```bash
ruby /opt/pipal/pipal.rb passwords.txt > pipal_analysis.txt
```

## Examples

### Example 1: Basic Usage

Analyze a standard wordlist like RockYou:

```bash
ruby /opt/pipal/pipal.rb /usr/share/wordlists/rockyou.txt
```

This will display console output with stats on the 14 million+ passwords.

### Example 2: Advanced Usage

Process a custom dump from a breach:

```bash
# Assuming passwords.txt is your file
ruby /opt/pipal/pipal.rb passwords.txt | grep "Base words" -A 10
```

This filters output to focus on base word frequencies.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Brute Force]] Brute Force (for informing cracking strategies)
- [[Unsecured Credentials]] Unsecured Credentials (for analyzing dumped passwords)

### Tactics

- [[Credential Access]] Credential Access

## Detection

Indicators and methods for detecting this tool's usage:

- Ruby process executing pipal.rb with large text files as arguments (e.g., via process monitoring tools like Sysmon or auditd).
- High I/O on password files or temporary analysis outputs.
- Network activity if combined with remote file transfers for dumps.

## Related Procedures

- [[procedures/Analyze-Password-Dump-for-Cracking]]
- [[procedures/Password-Spraying-Preparation]]

## Related Tools

- [[tools/Hashcat]]
- [[tools/john-the-ripper]]
- [[tools/CeWL]]

## References

- Official GitHub: https://github.com/digininja/pipal
- Kali Tools Page: https://www.kali.org/tools/pipal/
- Blog Post by Author: https://digi.ninja/p/projects/pipal.php
