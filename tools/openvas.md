---
id: tool-001
url: 'https://www.openvas.org/'
tags:
  - scanner
  - vulnerability
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:36.706Z'
validated: true
submitted: true
---
# OpenVAS

**Status**: Unverified

## Overview

OpenVAS is an open-source vulnerability scanner used to probe services and identify issues like the Node.js HTTP2 DoS by running tests on server ports.

## Description

It performs vulnerability tests with configurations like Fast and Ultimate, including TCP-SYN pings to detect live services and scan for weaknesses in HTTP2 implementations.

## Features

- Feature 1: Comprehensive vulnerability database
- Feature 2: Network scanning with SYN pings
- Feature 3: Report generation for findings

## Installation

### Requirements

- Linux distribution (e.g., Kali)
- Greenbone services

### Install Commands

```bash
# Typically pre-installed on Kali; otherwise:
sudo apt update && sudo apt install openvas
```

## Basic Usage

```bash
gvm-setup
```

To initialize.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--scan` | Start a scan |

## Examples

### Example 1: Basic Usage

```bash
openvas --target=127.0.0.1 --port=50000
```

### Example 2: Advanced Usage

```bash
openvas --config=ultimate --tests=all --ping=tcp-syn
```

With full vuln tests.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network probes on unusual ports
- GVM logs on target

## Related Procedures


## Related Tools

- [[tools/Greenbone-Vulnerability-Manager]]
- [[tools/Nessus]]

## References

- Official documentation: https://www.openvas.org/docs
- Related resources: Greenbone community
