---
url: 'https://github.com/ajxchapman/researchersservers'
tags:
  - dns
  - rebinding
type: tool
platforms:
  - Linux
description: >-
  Custom DNS server for simulating rebinding attacks with alternating
  resolutions.
id: 479c21ff-4396-45c7-8f6f-bf0077273bc8
created_at: '2025-12-14T03:46:09.443Z'
updated_at: '2025-12-14T03:46:09.443Z'
verified: false
validated: true
submitted: true
---
# researchersservers

**Status**: Unverified

## Overview

A tool for running a custom DNS server that supports dynamic responses, used to craft rebinding scenarios for ToCToU exploits.

## Description

This project allows configuration of domains to return different IPs based on query timing or count, with low TTL for rapid changes. Configured via JSON for GitLab SSRF.

## Features

- Feature 1: Alternating A records
- Feature 2: TTL control (e.g., 0)
- Feature 3: Query-based response variation

## Installation

### Requirements

- Go or pre-built binary

### Install Commands

```bash
go get github.com/ajxchapman/researchersservers
```

## Basic Usage

```bash
./researchersservers -config 41_gitlab.json
```

### Common Options

| Option | Description |
|--------|-------------|
| -config | JSON config file |
| -port | DNS port (default 53) |

## Examples

### Example 1: Basic Usage

Start server with GitLab config for gitlabextssrf.webhooks.pw.

### Example 2: Advanced Usage

Customize JSON for more domains.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unauthorized DNS servers in network
- Queries to non-standard DNS ports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[dnsmasq]]
- [[bind]]

## References

- GitHub: https://github.com/ajxchapman/researchersservers
