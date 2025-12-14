---
id: tool-pip-001
url: 'https://pip.pypa.io/en/stable/'
tags:
  - python
  - package-manager
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.667Z'
validated: true
submitted: true
---
# pip

**Status**: Unverified

## Overview

Pip is the Python package installer, used here to install Flask for the attacker-controlled webhook redirect server.

## Description

Standard tool for managing Python dependencies in PoC environments, enabling quick setup of web servers for SSRF.

## Features

- Feature 1: Install from PyPI
- Feature 2: Virtual environment support
- Feature 3: Dependency resolution

## Installation

### Requirements

- Python 3.6+

### Install Commands

```bash
# Usually bundled with Python
python -m ensurepip --upgrade
```

## Basic Usage

```bash
pip --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help |
| `--upgrade` | Upgrade package |

## Examples

### Example 1: Basic Usage

```bash
pip install Flask
```

### Example 2: Advanced Usage

```bash
pip install Flask==1.1.2 --user
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Tactics

- [[Execution]] Execution

## Detection

- Monitor pip installs for suspicious packages
- Restrict in air-gapped environments

## Related Procedures

- [[procedures/Setup-Attacker-Controlled-Redirect-Server]]

## Related Tools

- [[tools/Flask]]
- [[tools/poetry]]

## References

- Official documentation: https://pip.pypa.io/en/stable/
