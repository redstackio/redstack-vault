---
id: d4e5f6g7-h8i9-0123-defg-456789012345
url: 'https://edoverflow.com/2017/github-recon/'
tags:
  - reconnaissance
  - github
  - dns
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:51:10.604Z'
validated: true
submitted: true
---
# GitHub Recon Techniques

**Status**: Unverified

## Overview

GitHub Recon Techniques is a methodology for discovering subdomain takeovers by mining GitHub repositories for leaked DNS configurations and secrets pointing to cloud services, enabling identification of dangling records.

## Description

This approach involves searching GitHub for target domain references in code, configs, and workflows to uncover CNAMEs to services like GitHub Pages or S3 buckets. It's used in offensive security for reconnaissance, particularly against domains with poor DNS hygiene, as seen in government site vulnerabilities. Features include manual search patterns and verification steps for takeovers.

## Features

- Feature 1: GitHub search queries for domain-specific configs
- Feature 2: Identification of claimable services via dangling CNAMEs
- Feature 3: Step-by-step validation for subdomain control

## Installation

### Requirements

- Web browser or GitHub CLI
- Access to GitHub search (no install needed for basic use)

### Install Commands

```bash
# No installation; use GitHub web interface or API
# Optional: Install GitHub CLI
brew install gh  # On macOS
```

## Basic Usage

```bash
gh search code {REDACTED}.data.gov --repo github
```

### Common Options

| Option | Description |
|--------|-------------|
| `-t, --type` | Search type (code, issues, repos) |
| `-l, --language` | Filter by language |

## Examples

### Example 1: Basic Usage

Search for domain in repositories:

```bash
gh search code --repo github "{REDACTED}.data.gov"
```

### Example 2: Advanced Usage

Filter for config files:

```bash
gh search code filename:.github "{REDACTED}.data.gov"
```

## Expected Output

List of repositories and code snippets containing DNS pointers; manually extract and verify with DNS queries.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous GitHub API queries from security scanners
- Increased searches for internal domains

## Related Procedures


## Related Tools

- [[dnsrecon]]
- [[subfinder]]

## References

- Official blog: https://edoverflow.com/2017/github-recon/
- GitHub API docs
