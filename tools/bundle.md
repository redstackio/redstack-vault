---
url: 'https://bundler.io/'
tags:
  - dependencies
type: tool
verified: false
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.310Z'
id: 8b671d79-12ac-46a6-8328-9920f3854bd6
validated: true
submitted: true
---
# bundle

**Status**: Unverified

## Overview

Bundler manages Ruby gem dependencies, used to install the vulnerable actionpack-page_caching gem.

## Description

Reads Gemfile to resolve and install gems securely.

## Features

- Feature 1: Dependency resolution
- Feature 2: Lockfile for reproducibility
- Feature 3: Group-specific installs

## Installation

### Requirements

- Ruby

### Install Commands

```bash
gem install bundler
```

## Basic Usage

```bash
bundle --help
```

### Common Options

| Option | Description |
|--------|-------------|
| install | Install gems |
| update | Update gems |

## Examples

### Example 1: Basic Usage

```bash
bundle install
```

### Example 2: Advanced Usage

```bash
bundle install --without development
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- Gemfile.lock changes

## Related Procedures

- [[procedures/Prepare-Rails-Environment-with-Vulnerable-Gem]]

## Related Tools

- [[tools/rails]]

## References

- Docs: https://bundler.io/man/bundle-install.1.html
