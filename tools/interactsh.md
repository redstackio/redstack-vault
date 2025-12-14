---
id: tool-interactsh
url: 'https://github.com/projectdiscovery/interactsh'
tags:
  - oob
  - ssrf
  - listener
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:45.998Z'
validated: true
submitted: true
---
# interactsh

**Status**: Unverified

## Overview

Interact.sh is an out-of-band interaction tool for detecting blind vulnerabilities like SSRF by generating unique domains and listening for DNS/HTTP callbacks from targets.

## Description

Designed for security testing, it creates disposable payloads for OOB communication, polling a server for interactions. Commonly used in web app pentests to confirm blind exploits without direct feedback, supporting HTTP, DNS, and SMTP interactions.

## Features

- Feature 1: Unique domain generation for each payload
- Feature 2: Real-time polling and logging of interactions
- Feature 3: Support for multiple protocols (HTTP, DNS)

## Installation

### Requirements

- Go 1.17+
- Git

### Install Commands

```bash
# Clone and build
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-server@latest
```

## Basic Usage

```bash
interactsh-client
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `-v` | Verbose mode |

## Examples

### Example 1: Basic Usage

```bash
interactsh-client -i
```

Generates payload and polls for interactions.

### Example 2: Advanced Usage

```bash
interactsh-client --payload abc123.oast.fun
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Anomalous DNS queries to interact.sh domains
- Outbound HTTP to unique OOB endpoints
- Network logs showing polling traffic

## Related Procedures


## Related Tools

- [[tools/Burp-Suite-Collaborator]]

## References

- Official documentation: https://docs.projectdiscovery.io/tools/interactsh
- Related resources: ProjectDiscovery docs
