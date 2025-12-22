---
id: 1f14e468-0176-43af-9795-d59576c46fa6
type: tool
verified: true
created_at: '2019-08-28T21:17:28.605318+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reconnaissance
  - osint
  - github
  - secrets
url: 'https://github.com/tomnomnom/GitHarvester'
validated: true
---

# GitHarvester

**Status**: Unverified

## Overview

GitHarvester is a command-line tool for reconnaissance on GitHub, similar to Google dorking but targeted at public repositories. It searches for mentions of specified domains (e.g., internal company domains) within GitHub code, helping identify leaked source code, configuration files, API keys, or other sensitive information exposed in public repos.

## Description

The tool queries the GitHub search API to find repositories and files containing user-provided domains or keywords. It's particularly useful in red teaming and OSINT for discovering misconfigurations where developers accidentally commit internal details to public repositories. Supports filtering for tokens/secrets and CSV output for further analysis.

## Features

- Feature 1: Domain-based GitHub repository searching
- Feature 2: Filtering for potential secrets and tokens
- Feature 3: CSV export for structured results
- Feature 4: High-volume searching via GitHub API (rate limit aware)

## Installation

### Requirements

- Go 1.13 or later
- GitHub API access (no auth required for basic use, but token recommended for higher limits)

### Install Commands

```bash
# Install via Go
GO111MODULE=on go install github.com/tomnomnom/Githarvester@latest

# Or clone and build
git clone https://github.com/tomnomnom/Githarvester.git
cd Githarvester
go build
```

For Kali/Ubuntu: Ensure Go is installed via `sudo apt install golang-go`.

## Basic Usage

```bash
githarvester --help
```

Prepare a domains.txt file with one domain per line, then run:

```bash
githarvester domains.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| -tokens | Filter results for potential API tokens and secrets |
| -csv | Output results in CSV format |
| -keys | Search specifically for keys (e.g., AWS, GitHub tokens) |

## Examples

### Example 1: Basic Usage

```bash
githarvester domains.txt
```

Searches for all domains in the file and lists matching GitHub URLs.

### Example 2: Advanced Usage

```bash
githarvester -tokens -csv domains.txt > results.csv
```

Searches for tokens related to domains and exports to CSV.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Social Media]] Search Open Websites and Services: Social Media
- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of GitHub API requests from a single IP (monitor GitHub logs)
- Detection method 2: Unusual searches for internal domains in public repos (alert on repo access patterns)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/GitRob]]
- [[tools/truffleHog]]

## References

- Official GitHub: https://github.com/tomnomnom/Githarvester
- Blog post by author: https://blog.tomnomnom.com/githarvesting

*Last updated: 2023-10-01*
