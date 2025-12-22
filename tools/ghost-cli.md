---
url: 'https://github.com/TryGhost/Ghost#quickstart-install'
tags:
  - setup
  - cms-management
type: tool
platforms:
  - Node.js
  - Linux
  - macOS
  - Windows
description: >-
  Command-line interface for installing, configuring, and managing Ghost
  blogging platform instances
id: 3136ad81-d1ce-4312-8218-a35a024dea4c
created_at: '2025-12-14T04:39:09.639Z'
updated_at: '2025-12-14T04:39:09.639Z'
verified: false
validated: true
submitted: true
---
# ghost-cli

**Status**: Unverified

## Overview

Ghost CLI is the official tool for deploying and maintaining Ghost CMS, used here for local setup to test SSRF vulnerabilities.

## Description

It handles installation, updates, and server management for Ghost, supporting local, production, and Docker modes. In offensive security, it's essential for replicating vulnerable environments.

## Features

- Feature 1: Interactive setup wizards for databases and configs
- Feature 2: Start/stop/restart server commands
- Feature 3: Migration and backup utilities

## Installation

### Requirements

- Node.js v14+ and npm

### Install Commands

```bash
npm install ghost-cli@latest -g
```

## Basic Usage

```bash
ghost --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `--version` | Display CLI version |

## Examples

### Example 1: Basic Usage

```bash
ghost install local
```

### Example 2: Advanced Usage

```bash
ghost start --production
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques


### Tactics


## Detection

Indicators and methods for detecting this tool's usage:

- Presence of ghost-cli in npm global packages
- Running ghost processes on non-standard ports

## Related Procedures

- [[procedures/Install-Ghost-CLI-Globally]]
- [[procedures/Install-and-Setup-Ghost-Locally]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://ghost.org/docs/install/
