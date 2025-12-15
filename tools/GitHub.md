---
url: 'https://github.com'
tags:
  - vcs
  - discovery
type: tool
platforms:
  - Web
description: >-
  A web-based platform for version control and collaboration, often exploited
  for discovering exposed secrets in public repositories.
id: 20a48cf9-f816-40f4-a946-cec13a69f9e7
created_at: '2025-12-14T17:32:10.803Z'
updated_at: '2025-12-14T17:32:10.803Z'
verified: false
validated: true
submitted: true
---
# GitHub

**Status**: Unverified

## Overview

GitHub is a widely used platform for hosting and collaborating on code repositories. In security testing, it's commonly used to identify information disclosures, such as exposed API tokens committed to public repos without proper sanitization.

## Description

GitHub allows public access to code, making it a prime target for reconnaissance. Features like code search enable querying for sensitive strings across millions of repositories. In offensive operations, attackers browse or search public repos of target organizations to find credentials, which can lead to account compromise.

## Features

- Feature 1: Code search for keywords like 'token' or 'secret'
- Feature 2: Public repository browsing without authentication
- Feature 3: Integration with Git CLI for cloning and local analysis

## Installation

### Requirements

- Web browser for manual access
- GitHub CLI (gh) for automated searches

### Install Commands

```bash
# Install GitHub CLI (Linux/macOS)
brew install gh  # macOS
# or
sudo apt install gh  # Ubuntu
```

## Basic Usage

```bash
gh auth login
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--repo` | Specify repository for operations |

## Examples

### Example 1: Basic Usage

Browse to https://github.com/organization/repo and search files manually.

### Example 2: Advanced Usage

```bash
gh search code "api_token" --repo reverb/experimental
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor GitHub API rate limits for anomalous searches
- Audit repository access logs for suspicious queries
- Use secret scanning alerts from GitHub

## Related Procedures

- [[procedures/Discover-Exposed-Tokens-in-Public-GitHub-Repositories]]

## Related Tools

- [[Git]]

## References

- Official documentation: https://docs.github.com/en/search-github/searching-on-github
- Related resources: GitHub Security Lab reports
