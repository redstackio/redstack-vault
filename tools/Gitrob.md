---
url: 'https://github.com/michenriksen/gitrob'
tags:
  - recon
  - secrets
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.910Z'
id: 30568058-fb7a-4403-887b-a31a3d757a61
validated: true
submitted: true
---
# Gitrob

**Status**: Unverified

## Overview

Gitrob is a tool for scanning GitHub repositories for sensitive files and secrets, such as API keys, tokens, or configuration files like Rails secret_token.rb, aiding in reconnaissance for leaked credentials.

## Description

It clones repos, audits commits for patterns matching known sensitive file types, and outputs findings to a database for review. Commonly used in red teaming to find supply chain weaknesses. In this case, it identified the Algolia secret.

## Features

- Feature 1: Pattern-based detection of secrets in code
- Feature 2: Support for organization-wide scanning
- Feature 3: SQLite database for efficient querying

## Installation

### Requirements

- Go 1.13+
- GitHub personal access token

### Install Commands

```bash
# Clone and build
go install github.com/michenriksen/gitrob@latest
```

## Basic Usage

```bash
gitrob --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -commit-depth | Max commits to scan |
| -repo-group | Target org name |
| -db | Output database |

## Examples

### Example 1: Basic Usage

```bash
gitrob -repo-group algolia -db results.db
```

### Example 2: Advanced Usage

```bash
gitrob -commit-depth 1000 -export-json findings.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Credentials In Files]] Credentials In Files

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- High volume of GitHub API requests from a single IP
- Anomalous cloning of public repos
- Database files named gitrob.db on attacker systems

## Related Procedures

- [[procedures/Scan-GitHub-Repos-for-Secrets-with-Gitrob]]

## Related Tools

- [[TruffleHog]]
- [[Gitleaks]]

## References

- Official GitHub: https://github.com/michenriksen/gitrob
