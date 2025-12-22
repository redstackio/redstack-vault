---
type: tool
description: >-
  Load balancing detector that identifies DNS and HTTP load balancing
  configurations by analyzing server responses and header inconsistencies.
verified: true
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - recon
  - load-balancing
  - dns
  - http
url: 'https://github.com/metac0de/lbd'
commands:
  - '[[commands/lbd-basic-load-balancing-detection]]'
  - '[[commands/lbd-verbose-load-balancing-detection]]'
  - '[[commands/lbd-ip-load-balancing-detection]]'
validated: true
---

# lbd

**Status**: Unverified

## Overview

lbd (Load Balancing Detector) is a lightweight tool designed for reconnaissance in security testing. It detects whether a domain employs DNS or HTTP load balancing by sending multiple HTTP requests and comparing Server and Date headers across responses to identify inconsistencies indicative of load-balanced setups.

## Description

lbd is particularly useful during the reconnaissance phase of penetration testing to map out infrastructure. It probes targets multiple times (default 10 attempts) and looks for variations in response headers that suggest multiple backend servers. This can reveal hidden architecture details, such as the presence of load balancers like HAProxy or nginx, aiding in further attack planning like bypassing WAFs or targeting specific backends.

## Features

- Feature 1: DNS load balancing detection via IP resolution variations
- Feature 2: HTTP load balancing detection through header analysis (Server, Date)
- Feature 3: Support for direct IP probing and custom ports/timeouts
- Feature 4: Verbose mode for detailed probe logging

## Installation

### Requirements

- Perl (for the original script)
- Git

### Install Commands

```bash
# On Kali/Ubuntu (pre-installed on Kali)
git clone https://github.com/metac0de/lbd.git
cd lbd
chmod +x lbd.pl
sudo ln -s $(pwd)/lbd.pl /usr/local/bin/lbd

# Or via apt on Debian-based
sudo apt update && sudo apt install lbd
```

For macOS:

```bash
brew install lbd
```

## Basic Usage

```bash
lbd --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v | Verbose output with detailed probe information |
| -i | Probe IP directly instead of domain |
| -p PORT | Specify HTTP port (default 80) |
| -t TIMEOUT | Set probe timeout in seconds (default 10) |

## Examples

### Example 1: Basic Usage

Use [[commands/lbd-basic-load-balancing-detection]] for standard domain probing:

```bash
lbd example.com
```

### Example 2: Advanced Usage

Use [[commands/lbd-verbose-load-balancing-detection]] for detailed analysis:

```bash
lbd -v -p 443 -t 5 example.com
```

### Example 3: IP Probing

Use [[commands/lbd-ip-load-balancing-detection]] for direct IP checks:

```bash
lbd -i 192.168.1.100
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual patterns of repeated HTTP requests from the same IP to the same endpoint
- Detection method 2: Log analysis for multiple identical probes within short timeframes
- Detection method 3: Network monitoring for header analysis tools (though lbd is lightweight and hard to signature)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nmap]]
- [[tools/cURL]]

## References

- Official GitHub: https://github.com/metac0de/lbd
- Man page: lbd --help
