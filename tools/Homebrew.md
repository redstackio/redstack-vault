---
url: 'https://brew.sh/'
tags:
  - package-manager
type: tool
platforms:
  - macOS
description: >-
  Package manager for macOS providing easy installation of software via command
  line.
id: ec050919-b28b-4e4b-a0df-56522396ab5b
created_at: '2025-12-14T17:27:29.695Z'
updated_at: '2025-12-14T17:27:29.695Z'
verified: false
validated: true
submitted: true
---
# Homebrew

**Status**: Unverified

## Overview

Homebrew is the missing package manager for macOS, used to install, update, and manage command-line tools like Toxiproxy in security testing setups.

## Description

It simplifies dependency management and service startup for offensive security operations, such as setting up local proxies for exploitation demos.

## Features

- Feature 1: Formula-based installations from taps like shopify/shopify
- Feature 2: Service management via launchd integration
- Feature 3: Easy updates and formula auditing

## Installation

### Requirements

- macOS with Xcode Command Line Tools

### Install Commands

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Basic Usage

```bash
brew --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| -v | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
brew install wget
```

### Example 2: Advanced Usage

```bash
brew tap shopify/shopify && brew install toxiproxy
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of /opt/homebrew/bin/brew process
- Log entries for brew service starts

## Related Procedures

- [[procedures/Install-and-Start-Toxiproxy-Service]]

## Related Tools

- [[tools/toxiproxy]]

## References

- Official documentation: https://docs.brew.sh/
