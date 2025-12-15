---
url: 'https://github.com/tomnomnom/waybackurls'
tags:
  - reconnaissance
  - osint
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:30.739Z'
id: 3b1b8348-54df-47a5-a2bb-d2160bdc2d57
validated: true
submitted: true
---
# waybackurls

**Status**: Unverified

## Overview

Waybackurls is a command-line tool for retrieving and listing all URLs archived for a given domain from the Internet Archive's Wayback Machine, useful for reconnaissance and discovering hidden or deprecated endpoints in security testing.

## Description

It automates pulling historical web data to map a target's attack surface without direct interaction, commonly used in bug bounty hunting and penetration testing to find forgotten vulnerabilities like unprotected APIs.

## Features

- Feature 1: Fetches unique URLs from Wayback snapshots
- Feature 2: Supports domain-specific queries
- Feature 3: Outputs plain text for easy piping to other tools

## Installation

### Requirements

- Go 1.13 or higher

### Install Commands

```bash
# Installation command
go install github.com/tomnomnom/waybackurls@latest
```

## Basic Usage

```bash
waybackurls --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |

## Examples

### Example 1: Basic Usage

```bash
waybackurls liberapay.com
```

### Example 2: Advanced Usage

```bash
waybackurls example.com | sort -u
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to archive.org/api
- Command-line process named 'waybackurls'

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://github.com/tomnomnom/waybackurls
- Related resources: Internet Archive API docs
