---
id: tool-736522-authmagic-cli
url: 'https://www.npmjs.com/package/authmagic-cli'
tags:
  - cli
  - authmagic
  - setup
type: tool
verified: false
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.805Z'
validated: true
submitted: true
---
# authmagic-cli

**Status**: Unverified

## Overview

authmagic-cli is a command-line interface tool for initializing, installing, and running authmagic projects, used here to set up the example app with the vulnerable stateless core for JWT testing.

## Description

This npm package provides commands to scaffold authentication flows using authmagic modules. It installs dependencies like authmagic-timerange-stateless-core@0.0.9, which has the JWT validation flaw. Primarily for development, it's key for reproducing the vulnerability in a local environment.

## Features

- Feature 1: Project initialization with examples (-e flag)
- Feature 2: Dependency management (install command)
- Feature 3: Server startup (direct 'authmagic' invocation)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g authmagic-cli
```

## Basic Usage

```bash
authmagic --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `init` | Initialize project |
| `install` | Install deps |
| `-e` | Example mode |

## Examples

### Example 1: Basic Usage

```bash
authmagic init -e
```

### Example 2: Advanced Usage

```bash
authmagic install && authmagic
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- npm logs showing authmagic-cli installation
- Presence of authmagic project files in directories

## Related Procedures

- [[procedures/Initialize-and-Install-Authmagic-Example-App]]

## Related Tools

- [[tools/Burp-Suite]]

## References

- Official documentation: https://www.npmjs.com/package/authmagic-cli
- Related resources: Authmagic GitHub repo
