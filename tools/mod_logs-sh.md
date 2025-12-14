---
url: null
tags:
  - automation
  - shell-script
  - exfiltration
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.047Z'
id: 44f3ac21-0357-4fd3-a4df-e80de568c103
validated: true
submitted: true
---
# mod_logs-sh

**Status**: Unverified

## Overview

A shell script to automate fetching and paginating through Reddit moderator logs via the vulnerable GraphQL endpoint, outputting to a file for analysis.

## Description

This custom tool handles authentication, initial query, pagination loop, and data aggregation, simplifying the IDOR exploitation process for bulk log retrieval.

## Features

- Feature 1: Token and subreddit input validation
- Feature 2: Automatic pagination using endCursor
- Feature 3: JSON output to file (mod_log_out.txt)

## Installation

### Requirements

- bash shell
- curl and jq installed

### Install Commands

```bash
# Download or create script
wget https://example.com/mod_logs.sh
chmod +x mod_logs.sh
```

## Basic Usage

```bash
./mod_logs.sh --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -t, --token | Reddit bearer token |
| -s, --subreddit | Target subreddit name |
| -o, --output | Output file (default: mod_log_out.txt) |

## Examples

### Example 1: Basic Usage

```bash
./mod_logs.sh -t your_token -s target-subreddit
```

### Example 2: Advanced Usage

```bash
./mod_logs.sh -t your_token -s target-subreddit -o full_logs.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]
- [[Automated Collection]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for repeated GraphQL POSTs with varying 'after' parameters
- Log curl User-Agent patterns matching the script

## Related Procedures


## Related Tools


## References

- HackerOne Report #1658418
