---
id: tool-whois
url: 'https://www.whois.com/whois/doesfranshaveashell.com'
tags:
  - recon
  - domain
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.942Z'
validated: true
submitted: true
---
# Whois

**Status**: Unverified

## Overview

Whois is a protocol and tool for querying domain registration databases to retrieve ownership, expiration, and status information, essential for domain takeover reconnaissance.

## Description

Used in offensive security to check if domains are expired or available for hijacking. The web version at whois.com provides an easy interface; CLI version offers scripted queries. Common in pentests for supply chain attacks.

## Features

- Feature 1: Query domain status, expiration, and registrar
- Feature 2: Support for multiple TLDs
- Feature 3: Historical data access via some providers

## Installation

### Requirements

- Standard on Linux/macOS; install via package manager on Windows

### Install Commands

```bash
# Linux (Ubuntu)
apt install whois

# macOS
brew install whois
```

## Basic Usage

```bash
whois --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `-f file` | Read domains from file |

## Examples

### Example 1: Basic Usage

```bash
whois doesfranshaveashell.com
```

### Example 2: Advanced Usage

```bash
whois -h whois.com doesfranshaveashell.com | grep Expiration
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to whois servers (port 43)
- Logs of domain queries in SIEM

## Related Procedures

- [[procedures/Detect-Expired-Domain-Registration]]

## Related Tools

- [[tools/google-cache]]

## References

- Official: https://www.icann.org/resources/pages/whois-2013-05-03-en
- Whois.com: https://www.whois.com/
