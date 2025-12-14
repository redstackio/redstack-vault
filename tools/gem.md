---
id: tool-uuid-1
url: 'https://guides.rubygems.org/'
tags:
  - rubygems
  - cli
type: tool
verified: false
platforms:
  - Ruby
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.985Z'
validated: true
submitted: true
---
# gem

**Status**: Unverified

## Overview

The RubyGems CLI tool is the primary interface for managing Ruby libraries (gems), including building, installing, and serving them locally. In security testing, it's used to craft and deploy malicious gems exploiting vulnerabilities like stored XSS in the built-in server.

## Description

RubyGems provides commands for gem lifecycle management. Key for attacks: 'gem build' packages metadata, 'gem install' deploys it, and 'gem server' exposes a vulnerable web UI that renders unsanitized homepage links. Commonly used in Ruby environments for dependency management but exploitable for payload storage and delivery.

## Features

- Feature 1: Gem building from Gemspec files with metadata embedding
- Feature 2: Local installation and registry management
- Feature 3: Built-in HTTP server for browsing installed gems

## Installation

### Requirements

- Ruby 2.0+ installed

### Install Commands

```bash
# Typically bundled with Ruby
ruby -v  # Verify Ruby
```

## Basic Usage

```bash
gem --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --version | Display version |

## Examples

### Example 1: Basic Usage

```bash
gem list
```

### Example 2: Advanced Usage

```bash
gem server -p 8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'gem' executions
- Network logs for local port 8808 binds
- File system scans for unusual .gem files

## Related Procedures


## Related Tools


## References

- Official documentation: https://guides.rubygems.org/
- Related resources: RubyGems.org
