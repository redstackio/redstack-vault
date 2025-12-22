---
id: f083eb27-c8b3-49a0-82b1-06620b5e018d
type: tool
verified: true
created_at: '2019-08-28T21:17:40.278375+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - wordlist-generation
  - twitter-osint
  - credential-access
url: 'https://github.com/insidetrust/twofi'
validated: true
---

# Twofi

**Status**: Unverified

## Overview

Twofi is a specialized tool for generating custom wordlists from Twitter searches, enhancing standard dictionaries for password cracking. It automates the process of querying Twitter for keywords related to a target and extracting frequently occurring terms to create targeted lists.

## Description

Custom wordlists are essential for effective password cracking, as they incorporate context-specific terms that generic dictionaries might miss. Inspired by the “7 Habits of Highly Effective Hackers” blog, Twofi expands on the concept by allowing multiple search terms. It queries Twitter's API or search endpoints for results, processes the content to identify common words and phrases, and outputs a sorted wordlist (most frequent first). This is particularly useful in red teaming for tailoring attacks against organizations or individuals based on public social media data.

## Features

- Feature 1: Multi-keyword Twitter search integration for broad coverage.
- Feature 2: Automatic term extraction and frequency-based sorting.
- Feature 3: Configurable result limits to balance speed and comprehensiveness.
- Feature 4: Output in standard text format compatible with tools like Hashcat or John the Ripper.

## Installation

### Requirements

- Python 3.x
- Twitter API access (or fallback to web scraping, though API is recommended for reliability)
- pip and git

### Install Commands

```bash
# Clone the repository
git clone https://github.com/insidetrust/twofi.git
cd twofi

# Install dependencies
pip3 install -r requirements.txt

# For Kali/Ubuntu: Ensure Python and git are installed
sudo apt update && sudo apt install python3-pip git
```

## Basic Usage

```bash
twofi --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| --terms | Specify search keywords |
| --output | Define output file path |
| --limit | Set maximum search results |

## Examples

### Example 1: Basic Usage

Generate a wordlist from a single keyword search:

```bash
twofi --terms "company breach" --output breach_wordlist.txt
```

### Example 2: Advanced Usage

Use multiple terms with a limit:

```bash
twofi --terms "hacker password tips leak" --output custom_dict.txt --limit 150
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials (for generating wordlists to brute-force passwords)
- [[Gather Victim Host Information]] Gather Victim Identity Information (via OSINT from Twitter)

### Tactics

- [[Credential Access]] Credential Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for high-volume Twitter API requests from security testing environments.
- Detection method 2: Network logs showing connections to Twitter endpoints (api.twitter.com) from offensive tools.
- Detection method 3: Presence of generated wordlist files with Twitter-sourced terms in incident response forensics.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Cevo]] (similar OSINT wordlist generator)
- [[tools/Twint]] (Twitter scraping tool)

## References

- Official GitHub: https://github.com/insidetrust/twofi
- Original Blog Idea: “7 Habits of Highly Effective Hackers”

*Last updated: 2023-10-01*
