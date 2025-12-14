---
id: tool-uuid-002
url: 'https://man7.org/linux/man-pages/man1/time.1.html'
tags:
  - timing
  - measurement
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Unix
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.218Z'
validated: true
submitted: true
---
# time

**Status**: Unverified

## Overview

'time' is a shell builtin or utility that measures the execution time of commands, crucial for detecting delays in time-based attacks like blind SQLi.

## Description

It reports real, user, and system time, allowing differentiation between normal responses and SLEEP-induced delays in SQL queries.

## Features

- Feature 1: Reports wall-clock (real) time for response delays
- Feature 2: Integrates seamlessly with other commands like curl
- Feature 3: Built-in on most shells, no installation needed

## Installation

### Requirements

- Available by default in bash/zsh

### Install Commands

```bash
# Usually pre-installed
# For standalone: apt install time
```

## Basic Usage

```bash
time command
```

### Common Options

| Option | Description |
|--------|-------------|
| None primary | Basic timing |
| `--verbose` | Detailed output |

## Examples

### Example 1: Basic Usage

```bash
time curl https://example.com
```

### Example 2: Advanced Usage

```bash
time curl --data "payload" https://target.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Not directly detectable; look for timed requests in logs
- Correlate with slow responses

## Related Procedures


## Related Tools

- [[tools/curl]]

## References

- Man page: https://man7.org/linux/man-pages/man1/time.1.html
