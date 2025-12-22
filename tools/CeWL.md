---
id: 7fed5d70-8a5b-4e8d-bc6a-ce823ad21630
type: tool
verified: true
created_at: '2019-08-28T21:17:24.656285+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
commands:
  - '[[commands/cewl-generate-wordlist-from-website]]'
platforms:
  - Linux
  - Web
tags:
  - enumeration
  - web-applications
url: 'https://github.com/digininja/CeWL'
validated: true
---

# CeWL

**Status**: Unverified

## Overview

CeWL (Custom Word List generator) is a Ruby-based tool designed for offensive security testing. It crawls a specified website to a defined depth, optionally following external links, and extracts unique words from the content. These words can be used to build custom dictionaries for password cracking tools like John the Ripper or Hashcat. CeWL is particularly useful in web application enumeration phases to identify potential credentials or keywords specific to the target.

## Description

CeWL spiders the given URL, parsing HTML, JavaScript, and metadata to collect words. It supports options for minimum word length, depth limiting, email extraction, and meta-tempate parsing. The tool is lightweight and integrates well into reconnaissance workflows, helping generate targeted wordlists that improve brute-force success rates over generic dictionaries.

## Features

- Feature 1: Website spidering with configurable depth and link following.
- Feature 2: Word extraction with filters for length, case, and type (e.g., emails, meta data).
- Feature 3: Output to file in various formats suitable for cracking tools.
- Feature 4: Proxy support for anonymized crawling.
- Feature 5: Integration with other tools via pipeable output.

## Installation

### Requirements

- Ruby 2.0+ (with bundler for gem management).
- Internet access for gem installation.

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install cewl

# On Ubuntu/Debian (via gem)
sudo apt install ruby ruby-dev
sudo gem install cewl

# From source
git clone https://github.com/digininja/CeWL.git
cd CeWL
sudo gem build cewl.gemspec
sudo gem install cewl-*.gem
```

## Basic Usage

```bash
cewl --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -d, --depth | Set spidering depth (default: 2) |
| -m, --min_word_length | Minimum word length (default: 3) |
| -w, --write | Output words to file |
| --email | Extract email addresses |
| --meta | Parse meta tags for keywords |
| --lowercase | Convert words to lowercase |

## Examples

### Example 1: Basic Usage

```bash
cewl -d 2 -m 5 -w wordlist.txt http://example.com
```

### Example 2: Advanced Usage

```bash
cewl -d 3 --email --meta --lowercase -w advanced_wordlist.txt https://target.com
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials in Files]] Password Policy Discovery (for generating targeted wordlists).
- [[Brute Force]] Brute Force (preparation via custom dictionaries).

### Tactics

- [[Credential Access]] Credential Access.

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual HTTP requests from Ruby User-Agent strings (e.g., "CeWL") to web servers.
- Detection method 2: Web server logs showing systematic crawling of site depth.
- Detection method 3: Network traffic analysis for repeated GET requests to the same domain.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Tool: John the Ripper]] (for cracking generated wordlists).
- [[Tool: Hashcat]] (GPU-accelerated cracking).

## References

- Official GitHub: https://github.com/digininja/CeWL
- Usage guide: https://digininja.org/projects/cewl.php
