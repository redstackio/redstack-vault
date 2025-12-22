---
id: e4e7b0da-002f-411f-90f3-057f44fe6c2e
name: WhatWeb
type: tool
verified: true
created_at: '2019-08-28T21:17:27.639158+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Web
tags:
  - '[[Enumeration]]'
  - '[[Web Applications]]'
commands:
  - '[[commands/whatweb-basic-scan]]'
url: 'https://www.morningstarsecurity.com/research/whatweb'
validated: true
---

# WhatWeb

**Status**: Unverified

## Overview

WhatWeb is a web scanner that recognizes web technologies, including content management systems (CMS), blogging platforms, analytics packages, JavaScript libraries, web servers, and embedded devices. It is commonly used in reconnaissance phases of security assessments to fingerprint web applications and identify potential attack surfaces.

## Description

WhatWeb identifies technologies by matching patterns in HTTP responses, HTML, and other web content. It supports over 1800 plugins, each designed to detect specific software or features. The tool offers flexible scanning modes, from stealthy (aggressive=false) to comprehensive (with plugin aggression levels), making it suitable for both passive reconnaissance and detailed enumeration. It can scan single URLs, lists of targets, or even spider websites for deeper analysis.

## Features

- **Plugin-Based Detection**: Over 1800 plugins for identifying CMS, frameworks, servers, and more.
- **Aggression Levels**: Stealthy mode avoids aggressive probing; higher levels enable detailed checks.
- **Output Formats**: Supports JSON, XML, CSV, and grepable output for integration with other tools.
- **Plugin Development**: Easy to create custom plugins for new technologies.
- **Batch Scanning**: Handles multiple targets via files or ranges.

## Installation

### Requirements

- Ruby 1.9 or later (pre-installed on most pentesting distros).
- Internet access for initial plugin updates (optional).

### Install Commands

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install whatweb

# On Ubuntu/Debian
sudo apt update && sudo apt install whatweb

# From source (RubyGems)
gem install whatweb

# On macOS (using Homebrew)
brew install whatweb
```

## Basic Usage

```bash
whatweb --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-v, --verbose` | Increase verbosity level (up to 3 for debugging). |
| `-a, --aggression` | Set plugin aggression (1=stealthy, 3=aggressive, 4=heavy). |
| `-l, --log-json` | Log results to JSON file. |
| `--plugins` | List or specify plugins to use. |
| `-U, --user-agent` | Set custom User-Agent string. |

## Examples

### Example 1: Basic Usage

Scan a single website to identify technologies:

```bash
whatweb http://example.com
```

### Example 2: Advanced Usage

Perform an aggressive scan on multiple targets with JSON output:

```bash
targets.txt | whatweb -a 3 --log-json=results.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Software]] Software (identifies web server software and versions).
- [[Vulnerability Scanning]] Scanning IP Blocks (web-focused scanning).

### Tactics

- [[Reconnaissance]] Reconnaissance (gathers information on web technologies for targeting).

## Detection

- **Network Indicators**: HTTP requests with User-Agent strings matching WhatWeb (e.g., "WhatWeb/0.5.5").
- **Log Analysis**: Unusual probing patterns in web server logs, such as rapid requests for specific headers or paths.
- **Behavioral**: High volume of HEAD/GET requests from a single IP without follow-up exploitation.
- **Mitigation**: Web Application Firewalls (WAFs) can block based on User-Agent or request signatures; rate limiting on public-facing sites.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]] (for port scanning before web enumeration).
- [[tools/Wappalyzer]] (browser extension alternative for quick checks).

## References

- Official Website: https://www.morningstarsecurity.com/research/whatweb
- GitHub Repository: https://github.com/urbanadventurer/WhatWeb
- Documentation: https://morningstarsecurity.com/whatweb-documentation/
