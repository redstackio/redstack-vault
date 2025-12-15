---
id: tool-seq
url: 'https://man7.org/linux/man-pages/man1/seq.1.html'
tags:
  - bash
  - looping
type: tool
verified: false
platforms:
  - Linux
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.449Z'
validated: true
submitted: true
---
# seq

**Status**: Unverified

## Overview

seq is a bash utility that prints a sequence of numbers, commonly used in scripts for looping iterations, such as repeating exploit sends in DoS attacks.

## Description

Part of GNU coreutils, seq generates arithmetic progressions for for-loops, enabling controlled repetition in automation like sending multiple crafted requests.

## Features

- Feature 1: Simple numeric sequences
- Feature 2: Custom steps and formats
- Feature 3: Integration with backticks in bash

## Installation

### Requirements

- GNU coreutils

### Install Commands

```bash
# Pre-installed on most Linux; if not
apt install coreutils
```

## Basic Usage

```bash
seq 1 10
```

### Common Options

| Option | Description |
|--------|-------------|
| First Last | Start and end numbers |
| `-w` | Equal width padding |

## Examples

### Example 1: Basic Usage

```bash
for i in `seq 1 5`; do echo $i; done
```

### Example 2: Advanced Usage

```bash
seq 0 500 | while read x; do command $x; done  # Loop 501 times
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Script logs showing seq in loops
- High iteration counts in process args

## Related Procedures


## Related Tools

- [[Related Tool 1|tools/jot (BSD)]]
- [[Related Tool 2|bash for loops]]

## References

- Official documentation: man seq
- Related resources: GNU coreutils manual
