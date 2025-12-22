---
id: tool-trufflehog-001
url: 'https://github.com/trufflesecurity/trufflehog'
tags:
  - secrets
  - scanning
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.848Z'
validated: true
submitted: true
---
# truffleHog

**Status**: Unverified

## Overview

truffleHog is an open-source tool for detecting secrets and credentials in Git repositories and filesystems, commonly used in security audits to find leaked API tokens and keys.

## Description

truffleHog scans codebases using high-entropy string detection and over 800 regex detectors for specific secret types, including API tokens. It's ideal for offensive security to hunt for exploitable leaks in public repos, as in the Mozilla FuzzManager case. Supports Git history scanning to catch removed but committed secrets.

## Features

- Feature 1: Entropy-based detection for unknown secret formats
- Feature 2: Regex matching for 800+ secret types (e.g., API tokens)
- Feature 3: Support for Git, filesystem, Docker, and S3 scans

## Installation

### Requirements

- Go 1.18+ installed
- Git for repository access

### Install Commands

```bash
# Installation command
go install github.com/trufflesecurity/trufflehog@latest
```

## Basic Usage

```bash
trufflehog --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--json` | Output in JSON format |
| `--only-verified` | Show only verified secrets |

## Examples

### Example 1: Basic Usage

```bash
trufflehog filesystem ./repo
```

### Example 2: Advanced Usage

```bash
trufflehog git https://github.com/target/repo.git --since-commit HEAD~5
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Hardware]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network requests to GitHub APIs from scanning patterns
- Process execution of 'trufflehog' binary
- Log entries for high-volume repo clones

## Related Procedures

- [[procedures/Discover-Leaked-API-Tokens-in-Public-GitHub-Repositories]]

## Related Tools

- [[tools/GitLeaks]]
- [[tools/Gitleaks]]

## References

- Official documentation: https://github.com/trufflesecurity/trufflehog
- Related resources: OWASP Secret Management Cheat Sheet
