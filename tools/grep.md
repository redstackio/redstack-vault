---
url: 'https://www.gnu.org/software/grep/'
tags:
  - text-processing
  - filtering
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows (via Git Bash)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:12.163Z'
id: 1407f748-52ea-4a79-83e7-5836299b18f5
validated: true
submitted: true
---
# grep

**Status**: Unverified

## Overview

Grep is a command-line utility for searching plain-text data sets for lines matching a regular expression, commonly used in security testing to filter logs, responses, or outputs for specific patterns like error messages during reconnaissance or exploitation.

## Description

In offensive security, grep excels at parsing HTTP response logs from tools like Burp or curl to identify indicators such as error strings, success codes, or leaked information. It's lightweight, fast, and integrates into scripts for automated analysis, such as filtering invalid usernames from brute-force outputs in authentication attacks.

## Features

- Feature 1: Pattern matching with regex support for precise filtering
- Feature 2: Output control (e.g., invert match with -v to show non-matches)
- Feature 3: Recursive search (-r) for directories of log files

## Installation

### Requirements

- Standard Unix-like environment

### Install Commands

```bash
# On Debian/Ubuntu
apt install grep

# On macOS (pre-installed)
brew install grep  # For GNU version
```

## Basic Usage

```bash
grep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -i, --ignore-case | Ignore case distinctions
| -v, --invert-match | Select non-matching lines
| -n, --line-number | Prefix each line with its number

## Examples

### Example 1: Basic Usage

```bash
grep "error" log.txt
```

### Example 2: Advanced Usage

```bash
grep -v "Username does not exist" responses.log > valids.txt
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Account Discovery]] Account Discovery (for log filtering)

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for grep executions on sensitive logs
- Audit unusual file reads in security contexts

## Related Procedures

- [[procedures/Enumerate-Valid-Usernames-via-Error-Messages]]

## Related Tools

- [[awk]]
- [[sed]]

## References

- Official documentation: https://www.gnu.org/software/grep/manual/
- Related resources: Unix man pages
