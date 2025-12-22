---
id: tool-uuid-1
url: 'https://github.com/EdOverflow/can-i-take-over-xyz'
tags:
  - subdomain-takeover
  - recon
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:51:10.816Z'
validated: true
submitted: true
---
# can-i-take-over-xyz

**Status**: Unverified

## Overview

A curated repository documenting subdomain takeover vulnerabilities across cloud providers, including detailed techniques for AWS S3, Heroku, and others, used in offensive security for vulnerability assessment.

## Description

This tool provides a checklist and payloads for testing takeover feasibility on dangling DNS records. In offensive operations, it's referenced to confirm exploits like S3 bucket squatting, where deleted services leave CNAMEs vulnerable. Common use: Recon phase to validate attack paths.

## Features

- Feature 1: List of takeover-prone services with status (e.g., S3: Possible)
- Feature 2: Example payloads and verification steps
- Feature 3: Community-contributed updates on provider changes

## Installation

### Requirements

- Git
- Web browser or markdown viewer

### Install Commands

```bash
# Clone the repo
 git clone https://github.com/EdOverflow/can-i-take-over-xyz.git
 cd can-i-take-over-xyz
```

## Basic Usage

```bash
# No executable; browse README.md
 cat README.md | grep S3
```

### Common Options

| Option | Description |
|--------|-------------|
| N/A | Static repo; search/filter content |

## Examples

### Example 1: Basic Usage

Browse the repo and search for 'AWS S3' to find takeover instructions: Create bucket with exact CNAME name.

### Example 2: Advanced Usage

```bash
# Grep for specific providers
 grep -i 's3' services.md
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Git clone traffic to the repo URL
- References in scan logs to takeover checklists

## Related Procedures

- [[procedures/Confirm-and-Execute-S3-Bucket-Takeover]]

## Related Tools

- [[Related Tool: Subjack]]
- [[Related Tool: Takeover]]

## References

- Official GitHub: https://github.com/EdOverflow/can-i-take-over-xyz
- Related: AWS S3 documentation on bucket naming
